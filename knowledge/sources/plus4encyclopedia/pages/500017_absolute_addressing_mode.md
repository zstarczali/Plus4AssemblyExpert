# Absolute Addressing Mode

- Source: https://plus4world.powweb.com/plus4encyclopedia/500017
- Category: Programming/Assembly

The absolute addressing mode means that the operation is done on an address (memory location) that is specified as an absolute (non-relative, or otherwise modified) address. An example would be "STA $FF15". The address here is $FF15, the value of A will be stored exactly on that address (memory location).

The address itself is stored in low byte / high byte or **little-endian** format. Example: "STA $FF15" is stored as $8D $15 $FF, where $8D is the opcode for STA, $15 is the low byte, $FF is the high byte of the absolute address.

See Also
6502 addressing modes
