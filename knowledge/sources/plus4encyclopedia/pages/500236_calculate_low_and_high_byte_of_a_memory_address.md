# Calculate Low And High-Byte Of A Memory Address

- Source: https://plus4world.powweb.com/plus4encyclopedia/500236
- Category: Programming/BASIC
- Keywords: high byte, low byte Credits George (Edited by gerliczer @2012-08-15)

Sometimes you need to extract the Highbyte and the Lowbyte as Integer of an Integer 16Bit Address.
Example $2001
$20 is the Highbyte
$01 is the Lowbyte

q=DEC("2001") : REM DEC Converts an HEX to an INT
Low-Byte = q and 255
High-Byte = (q/256) and 255
