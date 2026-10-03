# CPU I/O Registers

- Source: https://plus4world.powweb.com/plus4encyclopedia/500290
- Category: Programming/Assembly

| Address | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 | Description |
|---|---|---|---|---|---|---|---|---|---|
| $0000 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | Data direction register (PDIR) |
| $0001 | 1* | 1* | 0 | 0* | 1 | 0 | 0 | 0 | 7 bit I/O port (PORT) |

The port data direction register (PDIR: $0000) is set to $00 when RESET is activated. (Configured for all port bit inputs.) However, the KERNAL RESET routine sets it to $0F and never changes it afterwards. (B7, B6, B4 remain inputs, B3, B2, B1, B0 will be outputs.)

7 bit I/O port (PORT: $0001):

- B7 / $80 : serial DATA in
- B6 / $40 : serial CLOCK in
- B5 / $20 : not implemented (always 0)
- B4 / $10 : datasette read in
- B3 / $08 : datasette motor out (0 = on, 1 = off)
- B2 / $04 : serial ATN out
- B1 / $02 : serial CLOCK out / cassette write
- B0 / $01 : serial DATA out

Notes:

- The values of the input bits also depend on the peripherals; the values marked with * are those that are readed in the "idle" state.
- B5 port bit is not implemented! When reading, both the PDIR and PORT registers are guaranteed to have B5 = 0; when writing, the value set for the bit does not matter.
- B4 is the datasette read signal. When the datasette motor is turned off, this bit usually reads 0. Warning: this port bit is only connected to the datasette! If no datasette is connected to the machine, this input is "floating." Normally, 0 is readed here, but this may change if the serial port is active!
- B1 is the serial bus CLOCK line control, and it is also the write signal to the datasette.
- B2/B1/B0 are used to control the serial port. These signals drive the serial port lines through an inverter. Therefore, a bit set to 1 switches the given line to low (0)! The current status of the serial lines can be read on B7/B6. (If the bit is 1, the given line is high.)
- The B3/B2/B1/B0 bits are only useful as outputs; there is no point in switching them to inputs. (The status of serial lines cannot be read when switched to input for these bits; therefore, the status of the ATN line cannot be read back!)
