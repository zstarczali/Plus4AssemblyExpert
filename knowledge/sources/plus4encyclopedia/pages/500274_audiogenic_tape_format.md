# Audiogenic Tape Format

- Source: https://plus4world.powweb.com/plus4encyclopedia/500274
- Category: Reference/TAP files, Programming/General

Description of the tape format found mostly on [Audiogenic](https://plus4world.powweb.com/groups/Audiogenic) releases, but has also appeared on a few other titles.
(The name of this format should be regarded as provisional)

Bits are encoded using short (bit 0) and long (bit 1) cycles of normal (lo-hi) polarity. There is also an extra-long cycle used only for the synchonizing sequence. The routine begins a cycle measurement by loading the timer. When the falling edge of a cycle is detected, the high byte of the timer is loaded and inverted. In the resulting value, bit 1 determines if 0 or 1 is loaded. If bit 2 is on, then an extra-long cycle occured.

There are at least three speed variants, using the following timer start points (+14 CPU cycles for timer handling):
$FF80 (fastest)
$FFFF
$0120 (slowest)

Data is loaded in 256-byte blocks to individual memory pages. There are no partial blocks, or blocks starting part-way in a memory page. The only exception to this is the very first block, which is hard-coded to load to $05EC-$06EC. This block contains the error handling routine, which prompts the user the stop, rewind and re-play a section of the tape if an error is detected.

A data block starts with the sync sequence, which consists of 31 extra-long cycles followed by three long cycles. The routine will scan for 5 extra-long cycles in succession, then wait for the three long cycles.

The first byte indicates the target memory page to be loaded to. The loader expects memory pages to be loaded sequentially. If this byte is out of sequence, an error is flagged. Values $00,$01 and $02 are reserved for the following:
$00=Run BASIC program, or return to running program
$01=End current memory page sequence and wait for new sequence. This is also used after the first block containing the error handling routine.
$02=As $00, but resets BASIC vectors first.

The block of program data then follows. Each byte is XORed with the check digit, initialised as $00. A check digit verification byte is loaded after the end of the data block.

Note that if the memory page byte was $00, $01 or $02, a data block and check digit is still included, but is not read.

[Thrust](https://plus4world.powweb.com/software/Thrust)
A variant of this loader is used for [Thrust](https://plus4world.powweb.com/software/Thrust). It is mostly the same, using the fastest timer value $FF80.

The differences are:
The first block containing the error handling routine no longer requires a '$01' block immediately following it.
Reserved values $01 and $02 are no longer used, therefore all page sequence interruptions require a return to the BASIC loader routine.
It is no longer possible to load to memory page $FFxx.
