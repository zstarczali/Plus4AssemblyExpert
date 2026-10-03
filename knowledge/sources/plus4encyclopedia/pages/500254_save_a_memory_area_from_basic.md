# Save a memory area from BASIC

- Source: https://plus4world.powweb.com/plus4encyclopedia/500254
- Category: Programming/BASIC
- Keywords: Save, basic

Saves a memory area from BASIC.

The example saves the graphic-screen from $1800-$3FFF which is set in line 3080.

3000 REM -= GFX Save Routine by MMS/gerliczer/George =-
3010 SA=DEC("07F2"):SX=SA+1:SY=SX+1:SR=SY+1
3020 TB=DEC("0333"):DR=8
3030 REM put the file name into FI$ e.g. FI$="DATA" BEFORE calling the Subroutine
3040 FI$="DATA":FI=LEN(FI$)
3050 FORI=1TOFI:POKETB-1+I,ASC(MID$(FI$,I,1)):NEXT: REM filename to TB store
3060 POKESA,0:POKESX,DR:POKESY,0:SYSDEC("FFBA"): REM DRIVE 8
3070 POKESA,FI:POKESX,TBAND255:POKESY,TB/256:SYSDEC("FFBD"): REM filename KERNAL
3080 POKEDEC("D1"),0:POKEDEC("D2"),DEC("18"):POKESY,DEC("3F"):POKESX,DEC("FF")
3090 POKESA,DEC("D1"):SYSDEC("FFD8")
3100 REM -= EOR GFX Saver =-
