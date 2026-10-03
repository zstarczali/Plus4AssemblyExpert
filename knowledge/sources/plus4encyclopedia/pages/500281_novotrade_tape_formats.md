# Novotrade Tape Formats

- Source: https://plus4world.powweb.com/plus4encyclopedia/500281
- Category: Reference/TAP files, Programming/General

Description of several turbo tape formats used on [Novotrade Magyarország](https://plus4world.powweb.com/groups/Novotrade_Magyarorszag), [Octasoft](https://plus4world.powweb.com/groups/Octasoft) and [DELTASoft](https://plus4world.powweb.com/groups/Deltasoft) releases.

First Tape Format
This is used on a large number of Novotrade and Octasoft releases, particularly on the earlier releases.

Bits are encoded using short (bit 0) and long (bit 1) wave cycles of inverted (hi-lo) polarity, using a timer threshold to determine cycle length (+27 CPU cycles for timer handling).

The timer value varies between different releases. Known values are:
$00E0 (fastest)
$00E2 (slowest)

Bits are loaded in LSb->MSb order.

The format consists of a header block, followed by a program data block.

The header block starts with the sync section, which begins with a continuous repetition of the byte $8D, followed with a series of countup bytes from $00 to $FF, followed by $00 again. After the sync section, the first two bytes are both $00. The next 16 bytes are the filename characters, loaded in reverse order. The next two bytes are the program execution address, followed by two bytes for the end address, followed by two bytes for the start address. All adddresses are loaded in hi-lo (reverse) order. The loaded filename is checked against the preset filename in the loader routine. If it matches, the data block is loaded; otherwise, it will search for another header block.

The program data block starts with the same sync section as the header block. The program data follows. Each byte is XORed with the check digit, initialized as $00. A check digit verification byte is loaded after the end of the program data.

Second Tape Format
Used on some later releases. It is mostly the same as the previous format, with the following differences:
The timer value is $018E.
In the header block, the two $00 bytes between the sync section and the filename characters are omitted.
A check digit calculation is also performed on the header block, and a check digit verification byte follows the load addresses. If the check fails, the routine will search for another header block.

Oddly, although this loader routine loads the check digit verification byte at the end of the program data block, it doesn't actually check it.

Turbó-15
This format is also used on a large number of Novotrade, Octasoft and [IHB](https://plus4world.powweb.com/groups/IHB) releases. Used by tape mastering programs [Turbó-15](https://plus4world.powweb.com/software/Turbo-15) and [Szuperturbo](https://plus4world.powweb.com/software/Szuperturbo).

Bits are encoded using short (bit 0) and long (bit 1) wave cycles of normal (lo-hi) polarity, using a timer threshold to determine cycle length (+17 CPU cycles for timer handling).

The timer value varies between different releases. Known values are:
$00EA (fastest)
$00FE
$0112
$012D (slowest)

On most commercial releases and on tapes mastered with Szuperturbo, bits are loaded in LSb->MSb order. However, tapes mastered with Turbó-15 and some commercial releases load bits in MSb->LSb order.

Load addresses are preset in the loader routine.

A data block starts with the sync section, which begins with a continuous repetition of seven short cycles and one long cycle, which is synchronized to bit pattern %00000010 ($02). This is followed with a series of countdown bytes from $09 to $00.

The program data follows. There is no error checking.

DELTALoad (Turbo 16 version)
This is used on most DELTASoft releases. Used by the tape mastering program [Turbo 16](https://plus4world.powweb.com/software/Turbo_16). The name 'DELTALOAD' is found in the filename on some releases of [Hidra](https://plus4world.powweb.com/software/Hidra).

Bits are encoded using long (bit 0) and short (bit 1) wave cycles, which is opposite to most turbo loaders. Wave cycles are of normal (lo-hi) polarity. A timer threshold is used to determine cycle length (+25 CPU cycles for timer handling). Bits are loaded in LSb->MSb order.

The timer value varies between different releases. Known values are:
$0100 (fastest)
$0110
$0140 (slowest)
[Headjust](https://plus4world.powweb.com/software/Headjust) uses a one-off timer value of $0400.

The data block starts with the sync section, which consists of a continuous stream of short cycles, followed by a byte. On commercial releases, this byte is $8A. On tapes mastered with Turbo 16, this byte is $A8.

The data block is comprised of five segments. The byte loaded in the sync section preceeds the first segment, and following segments are separated by a byte of the same value as the sync byte. Before loading a segment, the check digit is initialised as $00, and each subsequent byte is XORed to the check digit.

The first two bytes of a segment indicate the load address, and the next two bytes indicate the data length+$0200. Each of these values is loaded in hi-lo order. This is followed by a check digit verification byte, which is XORed to the check digit; the check passes if the result is zero. This is followed by program data. On every factor of 256 bytes remaining, a check digit verification byte is loaded and checked in the same manner. Another verification byte is loaded at the end of program data. Each verification byte is copied to $FF0F, resulting in white noise sounds in commercial releases, and tone sounds in Turbo 16 tapes.

The first segment contains the main program.

The second segment is loaded to $0100 onwards. Because the DELTALoad routine is loaded into $0100-$0200, it overwrites the default BASIC cursor colour values at $0113-$0123. This segment restores those values and may also alter the program execution address in the routine. Most commercial releases load this segment to $0100-$0150, while Turbo 16 tapes only load up to $0123, restoring the colour codes only. The overwritten DELTALoad routines are no longer required at this stage.

The third segment loads to $2B-$3B, setting up BASIC pointers.

The fourth segment loads commands into the keyboard buffer at $0527.

The fifth and final segment loads the keyboard buffer character quantity at $EF.

The final segment is followed by a $00 byte.

DELTALoad (variant)
This is also used on some DELTASoft releases, and differs from the Turbo 16 version as follows:

Bits are encoded the opposite way round (short=0, long=1).
Timer values are either $0100 (fastest) or $0180 (slowest).
The sync byte and separator bytes are $10. This value is also used for initialising the check digit.
There is an additional byte preceeding each separator byte. It's only function is to indicate to the loader routine whether another segment is to be loaded (not zero=load another, zero=end). In the Turbo 16 version, this function is performed by the separator byte.
The segment containing the main program is the last to be loaded, instead of the first.

[Rabló-Rulett](https://plus4world.powweb.com/software/Rablo-Rulett)
This is a one-off variant of DELTALoad, using the short=0/long=1 bit encoding, timer value of $0100, sync byte of $A8, and initialises the check digit with $00, which is calculated in the same manner.

Only one segment is loaded, containing the main program. There are no address bytes loaded, it is hard-coded to load to $0200-$4000.

The program data is divided into blocks, with each block starting with a byte loaded to $FF0F, followed by 256 bytes of program data, and ends with a check digit verification byte (the $FF0F byte is included in the check digit calculation). The bytes loaded to $FF0F allow for music to play while loading.

[Championship Wrestling](https://plus4world.powweb.com/software/Championship_Wrestling) Tape Format
This format is used on [Championship Wrestling](https://plus4world.powweb.com/software/Championship_Wrestling), [Karate](https://plus4world.powweb.com/software/Karate), [Ufo Vadász](https://plus4world.powweb.com/software/Ufo_Vadasz) and some releases of [Newton Almája](https://plus4world.powweb.com/software/Newton_Almaja).

Bits are encoded using short (bit 0) and long (bit 1) wave cycles of normal (lo-hi) polarity, with an extra-long cycle used as a byte marker between bytes.
The loader routine does not use a timer for measuring wave cycles. Instead, the screen is blanked, and the routine uses increments of the X register in a loop of 8 CPU cycles per increment.

There are two speed versions of this format. A byte marker is detected with an X register value greater than $40 (faster version) or $5A (slower version). Bits are determined by an X register value greater (bit 1) or less (bit 0) than $2D (faster version) or $50 (slower version).
The time between detecting the byte marker and starting measurement on the first bit is 12 CPU cycles. The time between the end of a bit and starting measurement on the next bit is 44 CPU cycles.

The data loaded by the KERNAL loader includes the loader routine and a small program, which initialises the loader routine by loading the X and Y registers with the load start address, and loading the accumulator with the ID number of the data block to be loaded.

By default, the first data block has the ID number $09, and other blocks may have other IDs. For example, Championship Wrestling uses the first block ($09) for the title screen, followed by $0A for the menu screen, $0B, $0C and $0D for game data, $01-$08 for wrestler data (only the data blocks of the selected wrestlers are loaded), and $0E for game data.

A data block starts with the sync section, which consists of a continuous repetition of the block's ID byte, followed by a $00 byte. The block's ID must match the ID expected by the loader routine for the block to be loaded. The routine will check for 256 consecutive matches of the ID byte, then waits for the $00 byte.

After the sync section, all subsequent bytes are XORed with the check digit, initialised with the value $B2. The first two bytes contain the block data length in lo-hi order. The program data follows. A check digit verification byte is loaded after the end of the program data.

Oddly, the loader routines in Championship Wrestling and Newton Almája (64K version) do not perform error checking, even though the tapes include the check digit verification byte, which is loaded and discarded.
