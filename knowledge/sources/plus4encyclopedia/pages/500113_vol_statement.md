# VOL Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500113
- Category: Reference/Commodore BASIC V3.5

VOL *volume level*

Sets the volume level for the [SOUND statement](500106_sound_statement.md).

The volume level is a value between 0-8 (8: maximum volume, 0: off). Negative values or values larger than 8 will result in an [?Illegal quantity error](500171_illegal_quantity_error.md). Decimal values are rounded down, therefore **VOL7.999** and **VOL7** will have the same effect.

VOL affects all SOUND voices.

The machine language equivalent would be adjusting the [$FF11](500024_ted_registers.md#FF11) TED register.

Examples
`VOL 8`  Sets volume to maximum
`VOL 0`  Turns off sound

Abbreviation
V SHIFT+O

Basic Token
$DB
