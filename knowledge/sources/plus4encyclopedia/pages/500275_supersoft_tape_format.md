# Supersoft Tape Format

- Source: https://plus4world.powweb.com/plus4encyclopedia/500275
- Category: Reference/TAP files, Programming/General

Description of the tape format produced by [Supersoft](https://plus4world.powweb.com/groups/Supersoft), widely used by [Kingsoft](https://plus4world.powweb.com/groups/Kingsoft), and also used by other publishers. A tape mastering routine was released as [Turbo Tape](https://plus4world.powweb.com/software/Turbo_Tape).

Bits are encoded using short (bit 0) and long (bit 1) cycles of inverted (hi-lo) polarity, using a timer threshold of $0194 (+10 CPU cycles for timer handling) to determine wave cycle length. Bits are loaded in MSb->LSb order.

A data block starts with the sync section, which begins with a continuous repetition of four short cycles and four long cycles, which is synchronized to bit pattern %00001111 ($0F). This is followed by a series of countdown bytes, counting down from $0E to $00, which completes the sync section.

The first two bytes are the start address, followed by two bytes for the end address, both addresses in lo-hi order.

The program data follows. Each byte is added in succession to the check digit, initialized as $00. A check digit verification byte is loaded after the end of the program data.

Variations
There are a small number of variations, most of which only differ from the Kingsoft blue/yellow border effect and are functionally identical.

An early version is used for [Music Master](https://plus4world.powweb.com/software/Music_Master), with no border effects.

Some copies of [Master Chess](https://plus4world.powweb.com/software/Master_Chess) use a version with a different border effect, with NOPs filling the gaps formerly occupied by the previous border effect code.

Another variant was used for [Spore](https://plus4world.powweb.com/software/Spore), [Storm](https://plus4world.powweb.com/software/Storm) and on some releases of [The Way Of The Exploding Fist](https://plus4world.powweb.com/software/The_Way_Of_The_Exploding_Fist) and [Megabolts](https://plus4world.powweb.com/software/Megabolts). It is similar to the Master Chess variant, but further modified so that the loader code is contained in a subroutine before the program execution address (in the regular version, the program execution address *immediately* follows the check digit verification). This modification makes the loader routine more suitable for use as a multi-part loader.

[Turbo Plus](https://plus4world.powweb.com/software/Turbo_Plus)
The [Turbo Plus](https://plus4world.powweb.com/software/Turbo_Plus) cartridge uses a variation of the tape format, intended for use only when the cartridge is installed. Turbo tapes saved with Turbo Plus cannot be loaded with the KERNAL loader.

This format consists of two blocks, a header block followed by the data block.

The header block is hard-coded to load to $0332-0372. It begins with the regular sync section, followed by the byte $F0. No address bytes are loaded. The header data is loaded, using the regular check digit calculation and verification.

The contents of the header data consists of the start address, followed by the end address (both in lo-hi format), followed by the filename (if specified). The remainder is filled with spaces ($20).

The header block is followed by the data block, which begins with the regular sync section, followed by the byte $0F. Again, no address bytes are loaded, the addresses from the header data are used instead. Data is then loaded, using the regular check digit calculation and verification.
