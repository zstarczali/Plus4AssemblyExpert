# TAP Files

- Source: https://plus4world.powweb.com/plus4encyclopedia/500247
- Category: Reference/TAP files, Programming/General
- Keywords: TAP

This topic contains (will contain) all information about TAP files. (For now it's just an information dump, but feel free to add anything you know.)

[-->clik here for C64 info](http://c64tapes.org/dokuwiki/doku.php?id=loaders:rom_loader)

The TAP format, also known as the Raw-Tape format, was originally designed in 1995-1997 by Per Håkan Sundell for the CCS64 emulator, with the v2 format being added by Markus Brenner in 2000. It attempts to duplicate the content of Commodore cassette tapes by measuring the individual wave periods on the tape, and representing these durations as single bytes.

A TAP file starts with the header, which is 20 bytes long ($00-$13). The header is structured as follows:

| $00-$0B | "xxx-TAPE-RAW", where xxx = C16 or C64 |
|---|---|
| $0C | TAP format version (0, 1, 2) |
| $0D | Machine (0 = C64, 1 = VIC, 2 = C16) |
| $0E | Video standard (0 = PAL, 1 = NTSC) |
| $0F | Unused (0) |
| $10-$13 | File size, not including header, in low-to-high format. |

The rest of the file contains the timing data. Each value represents the duration measured by the number of clock cycles of the specified machine, divided by 8. For the C16/Plus4, clock cycles are counted at single clock rate. On TAP versions 0 and 1, each byte represents a complete low-high cycle and assumes a 50% duty cycle. On version 2, each byte represents half of a wave cycle, which allows for the measuring of both low-high and high-low (inverted) waves.

A value of $00 represents an overflow. For v0 TAP files, this is defined as 20000 clock cycles. For v1 and v2 TAP files, a $00 value is followed by 3 bytes containing the actual duration measured in clock cycles (not divided by 8). These 3 bytes are in low-high format.

Commodore KERNAL tape loader

Waveform polarity: Normal

TAP file nominal values:
V1 wholewave:
$35,$6A,$D4
V2 halfwave:
$1A,$35,$6A

The Commodore KERNAL loader uses three pulse lengths. These pulse lengths are described in the TED KERNAL source code as short, long and word (or byte), sometimes described elsewhere as short, medium and long.

The TED KERNAL source code gives times for the pulse widths as 240us, 480us and 960us (proportional ratio 2:4:8) and records waveforms with a 50% duty cycle. Therefore, complete cycles have the following frequencies:
Short: 2083Hz
Long: 1042Hz
Word: 521Hz

The KERNAL ROM version 318004-01 (found on the prototype 264 and 232 machines) uses shorter pulse widths, with the approximate frequencies:
Short: 2500Hz, TAP values $2D (wholewave), $16 (halfwave)
Long: 1250Hz, TAP values $5A (wholewave), $2D (halfwave)
Word: 625Hz, TAP values $B4 (wholewave), $5A (halfwave)

The 2:4:8 proportional ratio of pulse lengths differs from other Commodore computers, which use a proportional ratio of approximately 2:3:4. This is the reason why C16/Plus4 tapes cannot normally be read by other Commodore computers and vice-versa.

Data is represented by pairs of pulses, in the following sequences:
Short, Long: Bit 0
Long, Short: Bit 1
Word, Long: Word marker (or byte marker)

Each byte consists of a word marker, 8 data bits and a parity bit. The parity bit calculation starts at 1, and is XORed by each data bit. Data bits are read in LSb->MSb order.

Data blocks are recorded twice. If there are errors on the first pass (up to a maximum of 30), these will be checked against the second pass.

A data block starts with the leader section, which is a continuous stream of short pulses. On the first pass, 16382 pulses are written. On the second pass, 243 pulses are written.
To achieve synchronization with tape speed, the loader routine first listens for 10 consecutive short pulses, then on every 2nd pulse, measures the duration of the pulse, which is repeated 16 times to determine tape speed.
The speed calculation involves setting the X register to zero, then incrementing the X register in a loop which uses 10 CPU cycles per increment at double-clock speed. These increments continue until the end of the pulse. The X register is then added to a grand total and reset to zero. This repeats until all 16 measurements are complete. This total is then divided by 4 to produce the timer value for the short pulse, and is then doubled for the long pulse timer value.
In practice, the TAP values for short pulses can range from $26/$13 to $40/$20, with the long and word pulses in proportion to the 2:4:8 ratio.
The leader section is followed by nine countdown bytes. These run from values $89 to $81 on the first pass, and $09 to $01 on the second pass.
The countdown bytes are followed by the type byte, which is one of the following values:
$01: File header for relocatable program (normally used for BASIC programs)
$02: SEQ data
$03: File header for non-relocatable program (normally used for machine code)
$04: File header for SEQ data
$05: End-of-tape (EOT) marker
If the data block is program data, there is no type byte, and this step is skipped. When saving a block of program data, the type variable is set to $00 for use by the tape routines.
The next step is the data to be loaded into memory. If the data being loaded is either a file header, SEQ data, or an EOT marker, it is loaded into the cassette buffer at $0333-$03F1 (191 bytes).
The final step is the checksum byte. The checksum is calculated by starting with the type byte, or $00 for program data, then is XORed by each following byte in turn.
The data block ends with a single long pulse and 194 short pulses.

The data loaded into memory from a file header consists of:
For program headers (types 1 and 3), the first two bytes are the start address, followed by two bytes for the end address. When a file header is written, the start address is retrieved from memory locations $B2-$B3 (stal+stah) and the end address from $9D-$9E (eal+eah).
If the header is a SEQ file header (type 4), these address bytes are still written, but they are not used. The OPEN statement does not change these addresses, and the tape routines simply write the previously used values.
The addresses are followed by the filename, which is 16 bytes long. Unused characters are filled with spaces ($20).
The remainder of the file header is normally filled with spaces ($20).

An EOT marker (type 5) fills the cassette buffer entirely with spaces ($20).

The loading speed for the KERNAL loader is approximately 63 bytes/second per pass.

KERNAL Tape Routines

The KERNAL loading and saving routines expect the screen to be blanked during operation. The KERNAL includes routines for screen blanking and the datasette motor, which are as follows:

| Routine address | Routine name | Description |
|---|---|---|
| $E364 | faster | Sets interrupt flag, blanks screen, disables raster interrupts and enables Timer 1 interrupts. |
| $E378 | slower | Sets interrupt flag, enables screen, disables Timer 1 interrupts and enables raster interrupts, then clears interrupt flag. |
| $E38D | moton | Enables datasette motor and clears cassette write bit*, then pauses for approximately 480ms. |
| $E3B0 | motoff | Disables datasette motor. |

*Note that some individual routines for writing to tape (listed below) expect the cassette write bit (bit 1 of $01) to be set high for normal waveform recording.

This is a list of the individual routines for saving to tape, which may be used to create custom headers/data.

| Routine address | Routine name | Description | Prerequisites |
|---|---|---|---|
| $E413 | wttt <br> (Wait for Timer to Toggle Twice) | Writes a single pulse to tape. | Call setupb, setups or setupl (listed below) to set the default pulse lengths. These do not need to be called again, except when changing the pulse length. <br> Or set t1pipe ($07C8-$07C9) with timer value for custom pulse length. <br> This routine assumes that the tape is already recording. <br> Set bit 1 of $01 (cassette write) high for normal waveform recording. |
| $E447 | setupb | Configures wttt for word (byte) pulses. | N/A |
| $E452 | setups | Configures wttt for short pulses. | N/A |
| $E45D | setupl | Configures wttt for long pulses. | N/A |
| $E468 | write0 | Writes pulse sequence for bit 0. | This routine assumes that the tape is already recording. <br> Set bit 1 of $01 (cassette write) high for normal waveform recording. |
| $E474 | write1 | Writes pulse sequence for bit 1. | This routine assumes that the tape is already recording. <br> Set bit 1 of $01 (cassette write) high for normal waveform recording. |
| $E480 | writew | Writes pulse sequence for word marker. | This routine assumes that the tape is already recording. <br> Set bit 1 of $01 (cassette write) high for normal waveform recording. |
| $E48C | wrbyte | Writes byte to tape, including word marker and parity bit. | Load accumulator with byte to be written. <br> This routine assumes that the tape is already recording. <br> Set bit 1 of $01 (cassette write) high for normal waveform recording. |
| $E4BA | welemb <br> (Write ELEMental Block) | Writes a single pass of data to tape. | Set type ($F8). <br> Set wrbase ($BA-$BB) with start address of data. <br> Set wrlen ($03F3-$03F4) with negated length of data to be saved. <br> Set pass ($F7), $80 for first pass, $00 for second pass. <br> This routine assumes that the tape is already recording. |
| $E535 | wfblok <br> (Write Fixed Block) | Saves the contents of the cassette buffer to tape, both passes. | Set type ($F8). <br> The entire contents of the cassette buffer can be set freely. |
| $E56C | tphead | Creates a file header and saves to tape. | Set type ($F8). <br> Set stal+stah ($B2-$B3) with start address of target file data, can be omitted for SEQ file headers. <br> Set eal+eah ($9D-$9E) with end address of target file data, can be omitted for SEQ file headers. <br> Set fnadr ($AF-$B0) with the address of the filename text. <br> Set fnlen ($AB) with the length of the filename. This can extend up to the end of the cassette buffer (#$BC). |
| $E5B0 | wvblok <br> (Write Variable Block) | Saves the contents of any memory area to tape. | Set type ($F8). <br> Set stal+stah ($B2-$B3) with start address of data. <br> Set eal+eah ($9D-$9E) with end address of data. |
| $E5F0 | wreot | Saves an end-of-tape (EOT) marker to tape. | N/A |
