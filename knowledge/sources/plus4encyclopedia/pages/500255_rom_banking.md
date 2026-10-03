# ROM Banking

- Source: https://plus4world.powweb.com/plus4encyclopedia/500255
- Category: Programming/Assembly
- Keywords: banking

The banking of RAM or ROM is determined by writing to the "shadow registers" at $FF3E/$FF3F.

$FF3E: writing any value to this address causes the ROM to be accessible.
$FF3F: writing any value to this address causes the RAM to be accessible.

When ROM is accessible, the banking can be controlled as follows:
LO ROM ($8000-$BFFF) and HI ROM ($C000-$FBFF / $FF40-$FFFF) are determined by writing to the appropriate ROM LATCH address.

| Bank | ROM latch | LO ROM | HI ROM |
|---|---|---|---|
| $00 | $FDD0 | BASIC | KERNAL |
| $01 | $FDD1 | (FUNCTION LO) | KERNAL |
| $02 | $FDD2 | CARTRIDGE 1 LO | KERNAL |
| $03 | $FDD3 | CARTRIDGE 2 LO | KERNAL |
| $04 | $FDD4 | BASIC | (FUNCTION HI) |
| $05 | $FDD5 | (FUNCTION LO) | (FUNCTION HI) |
| $06 | $FDD6 | CARTRIDGE 1 LO | (FUNCTION HI) |
| $07 | $FDD7 | CARTRIDGE 2 LO | (FUNCTION HI) |
| $08 | $FDD8 | BASIC | CARTRIDGE 1 HI |
| $09 | $FDD9 | (FUNCTION LO) | CARTRIDGE 1 HI |
| $0A | $FDDA | CARTRIDGE 1 LO | CARTRIDGE 1 HI |
| $0B | $FDDB | CARTRIDGE 2 LO | CARTRIDGE 1 HI |
| $0C | $FDDC | BASIC | CARTRIDGE 2 HI |
| $0D | $FDDD | (FUNCTION LO) | CARTRIDGE 2 HI |
| $0E | $FDDE | CARTRIDGE 1 LO | CARTRIDGE 2 HI |
| $0F | $FDDF | CARTRIDGE 2 LO | CARTRIDGE 2 HI |

Notes:

- Function LO/HI marked with parentheses above are not available on C16.
- The memory area between $FC00-$FCFF will **always** be the KERNAL ROM, regardless of the values written to $FDDx.

If the upper memory area is also switched to a different ROM, the interrupt vector will also come from the newly mapped bank. For this reason, if you want to use interrupts in the switched period, you have to set the appropriate vector in the $FFFE/$FFFF addresses in the ROM. For simplicity, this can be the vector of the original KERNAL interrupt routine: $FCB3. This is located directly in the memory space that is always KERNAL ROM. The original interrupt routine takes care of paging of KERNAL and then paging back the selected bank at the end.

At the end of the interrupt You should jump to $FCBE as it restores the original ROM bank (using zero page variable $FB to make an indexed write $FDD0,X) so it's important to set $FB to your ROM bank too.

Example:

```
LDX #$nn  for the values, see above table
STX $FDD0,x
STX $FB
```

The KERNAL provides the following helper functions for calling subroutines (long jump) and reading data (long fetch) from other ROM banks:

| Address | Name | Operation |
|---|---|---|
| $FCF7 | Long fetch | Read data from other ROM bank <br> Inputs: <br> - X: bank to read from <br> - A: bank to return <br> - $BE: address to read from <br> - Y: index to read from (LDA ($BE),Y) <br> Outputs: <br> - A: byte read from the other bank <br> Registers overwritten: X |
