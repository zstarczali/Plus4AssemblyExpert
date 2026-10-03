# Image File Formats

- Source: https://plus4world.powweb.com/plus4encyclopedia/500289
- Category: Programming/General
- Keywords: file format, graphics, petscii, hires, multicolor, fli, mcfli

Glossary

Attribute Cell

The screen is divided into 40 x 25 = 1000 attribute cells. Each cell is 8 x 8 pixels in size (8 x 2 px in the MCFLI graphics mode) and it determines the color of foreground pens (pen 0 and pen 1) in the cell area.

Background Pen

| Pen Number | TED Register | Description |
|---|---|---|
| 0 | $ff15 | Screen background color |
| 1 | $ff17 | Screen programmable color number 1 |
| 2 | $ff18 | Screen programmable color number 2 |
| 3 | $ff16 | Screen programmable color number 3 |

Foreground Pen

| Pen Number | Description |
|---|---|
| 0 | Attribute cell color 0 |
| 1 | Attribute cell color 1 |

PAR

Pixel Aspect Ratio

Image File Formats

File Formats for Character Graphics
Standard PETSCII Image

File Formats for Bitmap Graphics
Standard Bitmap Image
Botticelli
Multi Botticelli
MCFLI

Standard PETSCII Image

**Graphic mode:** High-Resolution Character Mode
**Attribute Cell Size:** 8 x 8 px

| Name | Size (Hex) | Size (Dec) | Offset (Hex) | Offset (Dec) | Description |
|---|---|---|---|---|---|
| LOAD ADDRESS | $02 | 2 | $00 | 0 | Load address: $00, $08 |
| COLOR DATA | $03e8 | 1000 | $02 | 2 | Character color data |
| PADDING | $18 | 24 | $03ea | 1002 | Padding to adjust to kB boundary |
| CHAR DATA | $03e8 | 1000 | $0402 | 1026 | Character data |
| PADDING | $18 | 24 | $07ea | 2026 | Padding to adjust to kB boundary |

**Note:** Background color is not saved.
**Load address:** $0800 (2048)
**File Size:** 2050 bytes

Standard Bitmap Image

**Graphic mode:** High-Resolution Bitmap Mode (320 x 200 px, PAR 1:1)
**Attribute Cell Size:** 8 x 8 px

| Name | Size (Hex) | Size (Dec) | Offset (Hex) | Offset (Dec) | Description |
|---|---|---|---|---|---|
| LOAD ADDRESS | $02 | 2 | $00 | 0 | Load address: $00, $18 |
| LUMINANCE MAP | $03e8 | 1000 | $02 | 2 | Foreground pen 0 (**) and 1 (*) luminance |
| PADDING | $18 | 24 | $03ea | 1002 | Padding to adjust to kB boundary |
| COLOR MAP | $03e8 | 1000 | $0402 | 1026 | Foreground pen 0 (*) and 1 (**) color |
| PADDING | $18 | 24 | $07ea | 2026 | Padding to adjust to kB boundary |
| BITMAP | $1f40 | 8000 | $0802 | 2050 | Bitmap data |

(*) Low nibble, (**) High nibble

**Load address:** $1800 (6144)
**File size:**10050 bytes

Botticelli

**Graphic mode:** High-Resolution Bitmap Mode (320 x 200 px, PAR 1:1), Multicolor Bitmap Mode (160 x 200 px, PAR 2:1)
**Attribute Cell Size:** 8 x 8 px

| Name | Size (Hex) | Size (Dec) | Offset (Hex) | Offset (Dec) | Description |
|---|---|---|---|---|---|
| LOAD ADDRESS | $02 | 2 | $00 | 0 | Load address: $00, $78 |
| LUMINANCE MAP | $03e8 | 1000 | $02 | 2 | Foreground pen 0 (**) and 1 (*) luminance |
| PADDING | $16 | 22 | $03ea | 1002 | Padding to adjust to kB boundary |
| BACKGRND 3 | $01 | 1 | $0400 | 1024 | Background pen 3 color, value stored to TED + $16 |
| BACKGRND 0 | $01 | 1 | $0401 | 1025 | Background pen 0 color, value stored to TED + $15 |
| COLOR MAP | $03e8 | 1000 | $0402 | 1026 | Foreground pen 0 (*) and 1 (**) color |
| PADDING | $18 | 24 | $07ea | 2026 | Padding to adjust to kB boundary |
| BITMAP | $1f40 | 8000 | $0802 | 2050 | Bitmap data |

(*) Low nibble, (**) High nibble

**Note:** The BACKGRND 3 & BACKGRND 0 colors are stored in reverse nibble order, so the lower and upper 4 bits must be swapped before you set the value to the TED.
**Load address:** 30720 ($7800)
**File size:** 10050 bytes

Multi Botticelli

**Graphic mode:** High-Resolution Bitmap Mode (320 x 200 px, PAR 1:1), Multicolor Bitmap Mode (160 x 200 px, PAR 2:1)
**Attribute Cell Size:** 8 x 8 px

| Name | Size (Hex) | Size (Dec) | Offset (Hex) | Offset (Dec) | Description |
|---|---|---|---|---|---|
| LOAD ADDRESS | $02 | 2 | $00 | 0 | Load address: $00, $78 |
| LUMINANCE MAP | $03e8 | 1000 | $02 | 2 | Foreground pen 0 (**) and 1 (*) luminance |
| PADDING | $12 | 18 | $03ea | 1002 | Padding to adjust to kB boundary |
| SIGNATURE | $04 | 4 | $03fc | 1020 | "MULT": $4d, $55, $4c, $54 |
| BACKGRND 3 | $01 | 1 | $0400 | 1024 | Background pen 3 color, value stored to TED + $16 |
| BACKGRND 0 | $01 | 1 | $0401 | 1025 | Background pen 0 color, value stored to TED + $15 |
| COLOR MAP | $03e8 | 1000 | $0402 | 1026 | Foreground pen 0 (*) and 1 (**) color |
| PADDING | $18 | 24 | $07ea | 2026 | Padding to adjust to kB boundary |
| BITMAP | $1f40 | 8000 | $0802 | 2050 | Bitmap data |

(*) Low nibble, (**) High nibble

**Note:** The BACKGRND 3 & BACKGRND 0 colors are stored in reverse nibble order, so the lower and upper 4 bits must be swapped before you set the value to the TED.
**Load address:** 30720 ($7800)
**File size:** 10050 bytes

MCFLI

**Graphic mode:** Multicolor FLI Mode (160 x 200 px, PAR 2:1)
**Attribute Cell Size:** 8 x 2 px

| Name | Size (Hex) | Size (Dec) | Offset (Hex) | Offset (Dec) | Description |
|---|---|---|---|---|---|
| LOAD ADDRESS | $02 | 2 | $00 | 0 | Load address: $00, $20 |
| LUMINANCE MAP 0 | $03e8 | 1000 | $02 | 2 | Luminance map 0 for foreground pens 0 (**) & 1 (*) |
| UNUSED | $18 | 24 | $03ea | 1002 | Unused |
| COLOR MAP 0 | $03e8 | 1000 | $0402 | 1026 | Color map 0 for foreground pens 0 (*) & 1 (**) |
| UNUSED | $18 | 24 | $07ea | 2026 | Unused |
| LUMINANCE MAP 1 | $03e8 | 1000 | $0802 | 2050 | Luminance map 1 for foreground pens 0 (**) & 1 (*) |
| UNUSED | $18 | 24 | $0bea | 3050 | Unused |
| COLOR MAP 1 | $03e8 | 1000 | $0c02 | 3074 | Color map 1 for foreground pens 0 (*) & 1 (**) |
| UNUSED | $18 | 24 | $0fea | 4074 | Unused |
| LUMINANCE MAP 2 | $03e8 | 1000 | $1002 | 4098 | Luminance map2 for foreground pens 0 (**) & 1 (*) |
| UNUSED | $18 | 24 | $13ea | 5098 | Unused |
| COLOR MAP 2 | $03e8 | 1000 | $1402 | 5122 | Color map 2 for foreground pens 0 (*) & 1 (**) |
| UNUSED | $18 | 24 | $17ea | 6122 | Unused |
| LUMINANCE MAP 3 | $03e8 | 1000 | $1802 | 6146 | Luminance map 3 for foreground pens 0 (**) & 1 (*) |
| UNUSED | $18 | 24 | $1bea | 7146 | Unused |
| COLOR MAP 3 | $03e8 | 1000 | $1c02 | 7170 | Color map 3 for foreground pens 0 (*) & 1 (**) |
| UNUSED | $18 | 24 | $1fea | 8170 | Unused |
| BITMAP | $1f40 | 8000 | $2002 | 8194 | Bitmap data |
| BACKGRND 0 & 3 | $01c8 | 456 | $3f42 | 16194 | Background pen 0 & 3 colors for each pixel line, values to be written to TED + $15 and TED + $16 |
| UNUSED | $38 | 56 | $410a | 16650 | Unused |

(*) Low nibble, (**) High nibble

**Note:** BACKGRND 0 & 3 array contains color register values for $ff15 and $ff16. The 1st value is for $ff15, 2nd for $ff16, 3rd for $ff15, 4th for $ff16, and so on.
**Load address:** $2000 (8192)
**File size:** 16706 bytes
