# Microdeal Tape Formats

- Source: https://plus4world.powweb.com/plus4encyclopedia/500277
- Category: Reference/TAP files, Programming/General

Description of two tape formats used by [Microdeal](https://plus4world.powweb.com/groups/Microdeal) games. One format is used by [Arena 3000](https://plus4world.powweb.com/software/Arena_3000), [Cuthbert Enters The Tombs Of Doom](https://plus4world.powweb.com/software/Cuthbert_Enters_The_Tombs_Of_Doom) and [Cuthbert In Space](https://plus4world.powweb.com/software/Cuthbert_In_Space). The other, used by [Cuthbert In The Cooler](https://plus4world.powweb.com/software/Cuthbert_In_The_Cooler), is completely different and is probably unique to that game.

[Arena 3000](https://plus4world.powweb.com/software/Arena_3000), [Cuthbert Enters The Tombs Of Doom](https://plus4world.powweb.com/software/Cuthbert_Enters_The_Tombs_Of_Doom), [Cuthbert In Space](https://plus4world.powweb.com/software/Cuthbert_In_Space)
Bits are encoded using short (bit 0) and long (bit 1) wave cycles of normal (lo-hi) polarity, using a timer threshold of $00EB (+12 CPU cycles for timer handling) to determine wave cycle length. Bits are loaded in LSb->MSb order.

The data block consists of a leader section of continuous long cycles, followed by the data section, which in turn is split into a series of mini-blocks, each of which contain data bytes and an error correction byte. In the single release versions of the above games, there are 2 data bytes per mini-block, and in the [Super Hits From Microdeal](https://plus4world.powweb.com/software/Super_Hits_From_Microdeal) versions, there are 16 data bytes per mini-block.

Each mini-block is separated by five long cycles. Each byte in the mini-block is preceded by two long cycles and one short cycle. The byte consists of eight data bits and a parity bit. Each data bit is XORed with the parity check, which is initialized as 0. The parity check is then XORed with the parity bit. If the result is zero, then the parity check passes. If it fails, the faulty byte is saved to memory and it's location recorded. Only one error is permitted per mini-block.
Each data byte is XORed to the error correction check digit, which is initialized as $00. After the data bytes are loaded, the error correction byte is loaded and XORed to the error correction check digit. If there was no error, the result is zero. Otherwise, the result is then XORed to the faulty byte and saved back to memory. Note that the error correction byte also includes a parity bit, but it is not checked by the loader routine.

The first mini-block contains the high bytes of the load addresses. The first byte is the start address high byte-$08, and the second byte is the end address high byte-$08. The address low bytes are preset to zero. The remaining mini-blocks contain the program data.

[Cuthbert In The Cooler](https://plus4world.powweb.com/software/Cuthbert_In_The_Cooler)
Bits are encoded using short (bit 0) and long (bit 1) wave cycles of normal (lo-hi) polarity, using a timer threshold of $00EA (+23 CPU cycles for timer handling) to determine wave cycle length. Bits are loaded in MSb->LSb order.

The tape consists of two data blocks, the first is hard-coded to load to $1100-$2200, and the second to $3300-$3F00.

Each data block consists of a leader section of continuous long cycles, followed by one short cycle. The program data follows. There is no error checking. The datasette motor is left on when the loader finishes.
