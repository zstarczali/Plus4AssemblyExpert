# Zifra / Her Turbo Tape Format

- Source: https://plus4world.powweb.com/plus4encyclopedia/500273
- Category: Reference/TAP files, Programming/General

Description of the turbo tape format produced by Zifra Software and also popularly known as Her Turbo. The source code for the tape mastering software was published in [Your Commodore February 1986](https://plus4world.powweb.com/publications/Your_Commodore_February_1986).

Data is encoded using short (bit 0) and long (bit 1) wave cycles of inverted (hi-lo) polarity, using a timer threshold of $0178 (+19 CPU cycles for timer handling) to determine wave cycle length. Bits are loaded in MSb->LSb order.

A data block starts with the sync section, which begins with a continuous repetition of seven short cycles and one long cycle, which is synchronized to bit pattern %00010000 (16).* This is followed with the byte $5A ('Z').

The next two bytes are the start address, followed by two bytes for the end address. The addresses are in lo-hi order.

The program data follows. Each byte is XORed with the check digit, initialized as $00. A check digit verification byte is loaded after the end of the program data.

Approximate loading speeds are:
Minimum: 212 bytes/second (all bits=1)
Maximum: 495 bytes/second (all bits=0)

*As a trivia note, the C64 version of this tape format (published in 'The Commodore 64 Kernal and Hardware Revealed' and reprinted in Your Commodore November 1985) synchronizes to bit pattern %01000000 (64).

Variations
As this tape turbo was published as source code, variations of the original format have appeared.

[Elite Systems](https://plus4world.powweb.com/groups/Elite_Systems_Ltd)
This is a variant found on the later [Elite Systems](https://plus4world.powweb.com/groups/Elite_Systems_Ltd) games [Airwolf 2](https://plus4world.powweb.com/software/Airwolf_2) and [Ikari Warriors](https://plus4world.powweb.com/software/Ikari_Warriors). It is functionally identical to the regular version, except that it runs at approximately half speed, using a timer value of $02F0.

[Finders Keepers](https://plus4world.powweb.com/software/Finders_Keepers)
This is a variant found on the [Finders Keepers](https://plus4world.powweb.com/software/Finders_Keepers) tape. It is mostly identical to the regular version, with the following differences: the address bytes are included in the check digit calculation (they are omitted in the regular version), and the second pair of address bytes specify the length of data to be loaded, instead of an explicit end address.
