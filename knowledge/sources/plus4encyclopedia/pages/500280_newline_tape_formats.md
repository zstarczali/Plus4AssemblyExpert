# NewLine Tape Formats

- Source: https://plus4world.powweb.com/plus4encyclopedia/500280
- Category: Reference/TAP files, Programming/General

Description of two tape formats released by [NewLine Hardware/Software](https://plus4world.powweb.com/groups/NewLine).
The first format is used to create standalone tapes which can be started with the KERNAL loader, and can be mastered using [Turbo Former](https://plus4world.powweb.com/software/Turbo_Former).
The second format is a very different, all-turbo format which requires the turbo software to be already present, and is used by [Turbo Tape 16](https://plus4world.powweb.com/software/Turbo_Tape_16).
The [Turbo 16 (NewLine)](https://plus4world.powweb.com/software/Turbo_16_NewLine) cartridge can create tapes in both versions.

Turbo Former
Bits are encoded using short (bit 0) and long (bit 1) wave cycles of inverted (hi-lo) polarity, using a timer threshold of $014A (+30-33 CPU cycles for timer handling). Bits are loaded in MSb->LSb order.

Load addresses are preset in the loader routine.

The data block starts with the sync section, which consists of a continuous repetition of the byte $16 and ends with a $C5 byte.

The program data follows. Each byte is XORed with the check digit, initialized as $00. A check digit verification byte is loaded after the end of the program data.

Turbo Tape 16
Bits are encoded using biphase space encoding. Each bit starts with a change in the signal level, at which point the timer is started ($00C0 for normal turbo speed, or $004C for super turbo speed). When the timer expires, the signal level is checked. If there is a change in level, a 0 is returned; if there is no change, a 1 is returned. The routine then waits for the next change in the signal level before restarting the timer. Bits are loaded in MSb->LSb order.

```

 Tape    ┌───┐ ┌─┐   ┌─┐ ┌───┐ ┌─┐   ┌─┐ ┌─
signal  ─┘   └─┘ └───┘ └─┘   └─┘ └───┘ └─┘
         │-1-│-0-│-1-│-0-│-1-│-0-│-1-│-0-│
        (MSb ────────────────────────> LSb)
               (Byte %10101010, $AA)

```

Because this method checks for ***changes*** in signal level rather than the state of the signal level, it can still be loaded if the tape signal is inverted (such as from tape copying).

The tape format consists of two blocks, a header block followed by the data block. The header block is always saved at normal turbo speed.

The header block starts with the sync section, which consists of a continuous repetition of the byte $E1 and ends with a $52 byte.

The header data follows, and is hard-coded to load to $0332-0372. The check digit is initialized as $00, and is incremented each time a 1 bit is loaded. A check digit verification byte is loaded at the end of the data.

The first byte of the header indicates the loading mode. If bits 0-3 are clear, then the program data is loaded at the start of the BASIC memory area. If bit 7 is on, then the data block wil be loaded at super turbo speed, otherwise it will be loaded at normal turbo speed.

The next two bytes are the start address, followed by two bytes for the end address (in lo-hi order). If the program is to be loaded to the start of BASIC, then the start address is ignored and the addresses used to calculate the program size. The remaining bytes contain the filename (if applicable), followed by spaces.

The data block follows, using a sync section consisting of a continuous repetition of the byte $E1 and ends with a $A6 byte. Program data is then loaded, using the aforementioned check digit method.
