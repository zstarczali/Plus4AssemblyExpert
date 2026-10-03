# Novaload Tape Format

- Source: https://plus4world.powweb.com/plus4encyclopedia/500272
- Category: Reference/TAP files, Programming/General

Description of the Novaload tape format.

Novaload encodes data using short (bit 0) and long (bit 1) wave cycles of normal (lo-hi) polarity, using a timer threshold of $018F (+12 CPU cycles for timer handling) to determine wave cycle length. Bits are loaded in LSb->MSb order.

A Novaload data block starts with the sync section, which begins with a continuous stream of short cycles, followed by a single long cycle. After receiving this long cycle, the routine reads a byte from the tape. If this byte is $AA (%10101010), then the sync section is complete. Otherwise, the sequence will restart.

After completing the sync section, all subsequent bytes are added in succession to the check digit, which is initialized as $00.

The next bytes to be loaded are for the Novaload filename (not to be confused with the on-screen KERNAL filename). The first byte loaded indicates the length of the filename. This is then followed by the filename characters. If the filename length is zero, no filename characters are loaded. By default, the first block of Novaload data has a filename length of $04, followed by the filename 'NOVA'.

The next set of 6 bytes indicate the loading addresses in lo-hi order. The first and second bytes are the start address-$0100, the third and fourth bytes are the end address, and the fifth and sixth bytes indicate the data length+$0100. For example, for a program loading to $1001-$4000, these bytes will be $01,$0F,$00,$40,$FF,$30.

The next byte is a check digit verification. If it matches, then loading continues. The check digit verification byte will then itself be added to the check digit.

The program data follows. After every 256 bytes, or at the end of program data, a check digit verification byte is loaded. If it matches, it is itself added to the check digit.

Approximate loading speeds are:
Minimum: 175 bytes/second (all bits=1)
Maximum: 460 bytes/second (all bits=0)
