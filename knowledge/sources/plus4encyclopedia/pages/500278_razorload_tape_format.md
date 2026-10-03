# Razorload Tape Format

- Source: https://plus4world.powweb.com/plus4encyclopedia/500278
- Category: Reference/TAP files, Programming/General

Description of the Razorload tape format used for [Razorsoft](https://plus4world.powweb.com/groups/Razorsoft) releases and on some copies of [Gnasher](https://plus4world.powweb.com/software/Gnasher). Some remnants of the tape mastering routine can be found in [Mail Trail](https://plus4world.powweb.com/software/Mail_Trail) at $3DF3.

Bits are encoded using only the low states of each cycle. A short low state equals bit 1, and a long low state equals bit 0. Bits are separated by high states of short length. The end of the last bit and the start of the first bit are separated by an extra-long high state, which marks the start of a byte. Bits are loaded in LSb->MSb order.

```

         Byte marker             Bit gaps            Byte marker
             │       ┌───┬─────┬───┬┴────┬───┬─────┐     │
             │       │   │     │   │     │   │     │     │
 Tape     ┌─────┐   ┌─┐ ┌─┐   ┌─┐ ┌─┐   ┌─┐ ┌─┐   ┌─┐ ┌─────┐ 
signal   ─┘     └───┘ └─┘ └───┘ └─┘ └───┘ └─┘ └───┘ └─┘     └─
         │      │-0-│ │1│ │-0-│ │1│ │-0-│ │1│ │-0-│ │1│      │
       End of     (LSb ─────────────────────────> MSb)    Start of
    previous byte        (Byte %10101010, $AA)            next byte

```

The loader routine does not use a timer for measurements. Instead, the screen is blanked, and the routine uses increments of the Y register in a loop of 10 CPU cycles per increment.
The byte marker is detected with a Y register value of $28 or greater. Bits are determined by a Y register value greater (bit 0) or less (bit 1) than $20.
The time between detecting the byte marker and starting measurement on the first bit is 63 CPU cycles. The time between the end of a bit separator and starting measurement on the bit is 23 CPU cycles. The time between finishing measurement on the last bit and starting measurement on the next byte marker can be between 81-113 CPU cycles, depending on the state of the loader routine.

The data block starts with the sync section, which consists of 256 $AA bytes. This is followed by eight bytes loaded to $0FF8-$0FFF. These appear to be address bytes, but the loader routine is preset on all games to load to $1000-$3FF8, and so these first eight bytes serve no function other than to end the sync section.

The program data follows. There is no error checking.
