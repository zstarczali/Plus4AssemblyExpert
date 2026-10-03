# I/O Area Map

- Source: https://plus4world.powweb.com/plus4encyclopedia/500249
- Category: Hardware
- Keywords: io map

Copied from Solder's home page:

```
  $FD00-$FD0F    ACIA-chip (6551/8551)
    $FD00-$FD03    Effective range for ACIA
    $FD03-$FD0F    Mirrors of $FD00-$FD03
  $FD10-$FD1F    Userport 6529B-chip (original)
    $FD10          Effective adress for 6529B (original)
    $FD10-$FD1F    Mirrors of $FD10 (original)
  $FD10-$FD1F    Userport-area (plus/4 with expansion)
    $FD10          6529B-chip from userport
    $FD11-$FD12    Centronics-printerport
    $FD13-$FD14    Low-/high-switching for OS96
    $FD15          Register for CSORY-RAM-expansion
    $FD16          Register for Hannes-RAM-expansion
    $FD17          Register for EPROM-/sRAM-expansion
    $FD18-$FD1F    Free (best for internal expansion)
  $FD20-$FD2F    Used by different hardware, decoded by PLA (pin 18)
  $FD30-$FD3F    6529B for keyboard
    $FD30          Effective adress for this 6529B
    $FD31-$FD3F    Mirrors of $FD30
  $FD40-$FD5F    SID-card, area for SID-chip
    $FD40-$FD5D    SID-chip
    $FD5E          DAC on digiblaster add-on
    $FD5F          ADC on digiblaster add-on
  $FD60-$FD7F    Area for expansion-userport
    $FD60-$FD63    ACIA on card 1
    $FD64-$FD67    ACIA on card 2
    $FD68-$FD6B    ACIA on card 3
    $FD6C-$FD6F    ACIA on card 4
  $FD70-$FD73    6529B-emulation on card 1
    $FD70          Effective adress for 6529B-emulation
    $FD71-$FD73    Mirrors of $FD70
  $FD74-$FD77    6529B-emulation on card 2
    $FD74          Effective adress for 6529B-emulation
    $FD75-$FD77    Mirrors of $FD74
  $FD78-$FD7B    6529B-emulation on card 3
    $FD78          Effective adress for 6529B-emulation
    $FD79-$FD7B    Mirrors of $FD78
  $FD7C-$FD7F    6529B-emulation on card 4
    $FD7C          Effective adress for 6529B-emulation
    $FD7D-$FD7F    Mirrors of $FD7C
  $FD80-$FD8F    Joyport on SID-card
    $FD80          Effective adress for joyport
    $FD81-$FD8F    Mirrors of $FD80
  $FD90-$FDCF    Free
  $FDD0-$FDDF    Area for ROM-banking
  $FDE0-$FDE1    MIDI-interface
  $FDE2-$FDEF    Free
  $FDF0-$FDFD    Free
  $FDFE          Register on EPROM-card
  $FDFF          Register on sRAM-card
  $FE00-$FE7F    Free (best usage for a RAM-drive...)
  $FE80-$FE9F    SID-card, mirror from $FD40... for hungarian-compatibility
    $FE80-$FE9D    SID-chip
    $FE9E          DAC on digiblaster add-on
    $FE9F          ADC on digiblaster add-on
  $FEA0-$FEBF    Free (?)
  $FEC0-$FECF    Floppy 1551, device 9
  $FED0-$FEEF    Free (?)
  $FEF0-$FEFF    Floppy 1551, device 8
```
