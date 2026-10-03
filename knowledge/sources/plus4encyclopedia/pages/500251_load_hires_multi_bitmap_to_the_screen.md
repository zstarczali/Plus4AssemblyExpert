# Load HIRES/MULTI Bitmap To The Screen

- Source: https://plus4world.powweb.com/plus4encyclopedia/500251
- Category: Programming/BASIC
- Keywords: load gfx Credits MMS (idea by gerliczer)

Time to time there were some discussions how you can load a Title Bitmap graphics in BASIC without interrupting the code.
(it is possible to simply LOAD a bitmap from BASIC, but then the program restarts. It requires special code (restart handling) and results a not structured spaghetti code)

This was created for the starters like me.
Our code was set to load a **standard bitmap graphics from $1800 onwards from Drive 8. It can be HIRES or MULTI.** It will be done with the help of KERNAL.

Details on the gfx format, parts and the lenght of the parts can be found at the end of the description.

Further possibilities:
1) It can be modified to be a more general code, that can load anything (charset, music, text, etc) to any required memory address.
For that please change at line 3080 the upper and lower memory address values in DEC("") function.
This targetted memory location could be handled via two variables (upper and lower address) you can set before calling the Subroutine
2) It could be combined with George's gfx copy code. [How To Display A Multicolor Bitmap](https://plus4world.powweb.com/kb.php?id=500234)
You may load a full bitmap to an other (non visible/not used) high memory area with this subroutine, and later copy only a section of it anywhere on the standard GFX screen with Geroge's Subroutine.

Below the loader Subroutine, that can be called without restarting the main BASIC program (straightforward examples below)

```
3000 REM -= GFX Loader routine by MMS/gerliczer/George =- 
3010 SA=DEC("07f2"):SX=SA+1:SY=SX+1:SR=SY+1
3020 TB=DEC("0333"):DRV=8
3030 REM put the file name into FI$ eg.FI$="examplepic" BEFORE calling the Subroutine 
3040 FI=LEN(FI$)
3050 FORI=1TOFI:POKETB-1+I,ASC(MID$(FI$,I,1)):NEXT: REM filename to TB store
3060 POKESA,0:POKESX,DRV:POKESY,0:SYSDEC("ffba"): REM DRIVE 8
3070 POKESA,FI:POKESX,TBAND255:POKESY,TB/256:SYSDEC("ffbd"): REM filename KERNAL 
3080 POKESA,0:POKESX,DEC("0"):POKESY,DEC("18"):SYSDEC("ffd5"): REM Load from $1800
3090 RETURN
3100 REM -= EOR GFX loader = 
```

How to use? Simple examples

```
2000 REM -= Load HIRES Graphics screen =-
2010 scnclr:graphic1,1:                      REM Erase screen 
2020 color0,2,4: color 4,1:                 REM set the colors
2030 FI$="hiresgfx1": GOSUB 3000:  REM set the filename; call the subroutine
2040 getkey A$:                               REM wait for keypress after picture loaded and shown

2200 REM -= Load MULTI Graphics screen =-
2210 scnclr:graphic3,1:                      REM Erase screen   
2220 color0,2,3: color 4,1: color 3,1:  REM set the multi colors
2230 FI$="multigfx": GOSUB 3000:    REM set the filename; call the subroutine
2240 getkey A$:                                REM wait for keypress after picture loaded and shown
```

Good loading time!

Helpful background information (from George):
1) A standard Mulitcolor Bitmap consist of 3 parts: bitmap-data, color-data, luminance-data
2) Screen memory of color-data starts at $1800 (this is our starting address) till $1BE7
3) Screen memory of luminance-data starts at $1C00 till $1FE7
4) Screen memory of bitmap-data starts at $2000 and continues till $3F3F (practically $3FFF)

To get a bitmap graphics:
- save it from the memory with S command (MONITOR) S "gfxscreen", 8, 1800, 4000 ($4000 byte will be not saved)
- just save one gfx from Botticelli or MultiBotticelli (originally between $7800 and $9F3F), and load it to $1800 with the routine.
