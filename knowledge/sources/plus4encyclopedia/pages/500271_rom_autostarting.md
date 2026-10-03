# ROM Autostarting

- Source: https://plus4world.powweb.com/plus4encyclopedia/500271
- Category: Programming/Assembly
- Keywords: banking,autostarting

ROM autostarting:

The Plus/4 can have 8 ROMs, 4 high and 4 low. The low ROMs run from $8000 to $BFFF, and the high from $C000 to $FFFF. The ROMs can be paged out completely by using the ROM and RAM select registers located at $FF3E and $FF3F respectively. Writing to $FF3F switches out the ROMs and writing to $FF3E switches them back in. Commodore's BASIC V3.5 is able to get over 60k of memory free by switching the ROMs in and out. Basic achieves this by transferring some of its ROM down into RAM. From address $0373 to address $04E6 you'll find various routines for banking out the ROMs to read the RAM underneath. The TED chip is however not paged out.

To select one of the 8 ROMs (BASIC and the KERNALl being 2 of them), you write to locations $FDD0 to $FDDF. The lower 2 bits are used to select the low ROMs, and bits 2 and 3 are used to select the high ROMs. To select the BASIC and KERNAL ROMs (numbers 0 and 4), you write to location $FDD0. This enables ROM number 0 and 4 (both 2 bit combos are 0). To enable the 3-Plus-1 built in ROMs, you would write to location $FDD5 to enable bit pattern %0101, or ROM number 1 and 5. When you are paging ROMs, locations $FC00 to $FCFF remain unpaged.

This is where the KERNAL does its "Check 8-ROM" routine ($FC1F, KERNAL routine SPKPAT).
PAT = Physical Address Translation (PAT) table.

From memory locations $FC1E to $FCFF, are taken up with ROM banking routines.

ROMs have the following structure:

```

$8000 jmp cold_start
$8003 jmp warm_start
$8006 device / module number (empty = 0, autostart = 1, other = module number)
$8007 "CBM" signature

```

Coldstart:
If you look at the KERNAL routine at $FC1E you'll notice it checks for $43 $42 $4d at locations $8007 and if found it jumps to $8000. It's here you can set up a KEY to jump to your ROM routine.

```

;  ** spkpat **   fixes:  babbling speech module
;
spkpat
       lda #$09
       sta $fd20       	;shut up
       ora #$80
       sta $fd20       	;shut up now (texans think this way...)
       jmp poll
;
;***********************************************************************
;
;                 software supporting banking hardware
;
;  *******  this code must fit *entirely* between $fc00-$fcff  *******
;
;
; set up each of the four possible slots, and test if there is a
; device in that slot. if so, store that devices number in the cor-
; responding entry in the physical address translation (pat) table.
; if a device is found to have a number of '1', it will be logged in the
; table, and a jump to that devices cold-start routine will be performed.
;
;***********************************************************************

poll
       ldx #3
       stx xsav
       lda #0
poll10
       sta pat,x       	;first zero out all pat entries
       dex
       bpl poll10

poll20			;set up and test each bank
       ldx xsav
       lda dblx,x      	;set up both upper & lower banks
       tax
       sta bnksel,x
       ldy #2
poll30
       lda $8007,y     	;test for 'cbm' (in ascii)
       cmp cbmmsg,y
       bne poll50      	;no match
       dey
       bpl poll30      	;keep looking

       lda $8006       	;it's 'cbm'...now get device number
       ldx xsav
       sta pat,x
       cmp #1          	;autostart?
       bne poll50      	;no
       stx curbnk      	;yes, give them the bank configuration,
       jsr $8000       	;.. then go to cold start routine.

poll50
       dec xsav
       bpl poll20
       rts

cbmmsg .byte 'CBM'
dblx   .byte %00000000,%00000101,%00001010,%00001111

```

1) The coldstart routine sets up a function KEY.
2) The coldstart routine sets up a function routine in RAM at $05f5-$065f.
3) The coldstart routine typically prints a message below COMMODORE BASIC V3.5 60671 BYTES FREE.

Example for 3 cartridges (without 3-Plus-1):

```

 COMMODORE BASIC V3.5 60671 BYTES FREE  
 CARTRIDGE 3 ON F3                      
 CARTRIDGE 2 ON F2                      
 CARTRIDGE 1 ON F1                      
                                        
READY.                                  
KEY                                     
KEY 1,"SYS1525:CART 1"                  
KEY 2,"SYS1545:CART 2"                  
KEY 3,"SYS1564:CART 3"                  
KEY 4,"SCNCLR"+CHR$(13)                 
KEY 5,"DSAVE"+CHR$(34)                  
KEY 6,"RUN"+CHR$(13)                    
KEY 7,"LIST"+CHR$(13)                   
KEY 8,"HELP"+CHR$(13)                   
                                        
READY.                                  

```

Warmstart:
The warmstart routine is typically the entry point to the main cartridge routine (SpeedScript, Script/Plus).

Module:
If device / module number = 0, the cartridge is ignored.
If device / module number = 1, the cartridge is autostarted.
If device / module number > 1, the cartridge is cold-started only.

Signature:
The CBM signature is mandatory so that the ROM is recognized.

ROMs are checked (after hard reset) in the following order:

```

0f: 00 00 11 11 (cartridge #3) External 2
0a: 00 00 10 10 (cartridge #2) External 1
05: 00 00 01 01 (cartridge #1) Internal (3-Plus-1 / 3-Plus-1)
00: 00 00 00 00 (cartridge #0) BASIC / KERNAL

```

ROMs are cold started in the following order (see BASIC / KERNAL is not): slots 3, 2, 1 - ext2, ext1, internal.

```

;*************************************************
;
; call every active cartridges cold start routine.
;
;*************************************************

phenix
       sei
       ldx #3
phen2
       lda pat,x
       beq phen3       	;no cartridge in this slot if 0

       txa
       pha
       lda dblx,x      	;select low and high rom
       tax
       sta bnksel,x
       stx curbnk
       jsr $8000       	;call it's cold start routine
       pla
       tax
phen3
       dex
       bne phen2       	;do slots 3,2,1 - ext2, ext1, int

       sta bnksel      	;set up system bank
       stx curbnk      	;..as current bank
       cli
       rts

```

Comments:
Some ROMs are badly coded and work only in slot 2 (cartridge ext1).
Some ROMs do not check for other ROMs present and blindly assign KEY 1 or 2.
Many ROMs only copy code from ROM to RAM and execute code in RAM, thus do not save precious memory (for example 3-Plus-1 copies its code from $1000 to $7000.

The 3-Plus-1 KERNAL routine copies some data into the function key area and also a start up section allowing you to run your program.

[Partially adapted from Mike Dailly].
