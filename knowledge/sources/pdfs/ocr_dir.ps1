# OCR every PNG in a folder with the built-in Windows OCR engine; writes <name>.txt next to each image.
# Windows PowerShell 5.1 is required (WinRT projection). Usage: powershell -File ocr_dir.ps1 <folder> [lang]
param([string]$Dir, [string]$Lang = "")

Add-Type -AssemblyName System.Runtime.WindowsRuntime
[void][Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime]
[void][Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation, ContentType = WindowsRuntime]
[void][Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
[void][Windows.Globalization.Language, Windows.Globalization, ContentType = WindowsRuntime]

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
        $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
        $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
function Await($op, [Type]$t) {
    $task = $asTaskGeneric.MakeGenericMethod($t).Invoke($null, @($op))
    $task.Wait() | Out-Null
    $task.Result
}

if ($Lang) {
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new($Lang))
} else {
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
}
if (-not $engine) { Write-Error "No OCR engine"; exit 1 }

Get-ChildItem -Path $Dir -Filter *.png | Sort-Object Name | ForEach-Object {
    $out = [IO.Path]::ChangeExtension($_.FullName, ".txt")
    if (Test-Path $out) { return }
    $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($_.FullName)) ([Windows.Storage.StorageFile])
    $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    # one OCR line per output row: top, left, height, text (rows are re-assembled by the caller)
    $lines = $result.Lines | ForEach-Object {
        $words = @($_.Words | ForEach-Object { $_ })
        $r = $words[0].BoundingRect
        $h = ($words | ForEach-Object { $_.BoundingRect.Height } | Measure-Object -Maximum).Maximum
        "{0:F0}`t{1:F0}`t{2:F0}`t{3}" -f [double]$r.Y, [double]$r.X, [double]$h, $_.Text
    }
    [IO.File]::WriteAllText($out, ($lines -join "`n"), [Text.Encoding]::UTF8)
    $stream.Dispose()
    Write-Output $_.Name
}
