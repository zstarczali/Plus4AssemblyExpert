# How To Display A Multicolor Bitmap

- Source: https://plus4world.powweb.com/plus4encyclopedia/500234
- Category: Programming/BASIC
- Keywords: Bitmap, Mulitcolor Credits George

Place a multicolor bitmap at any position (only character precision, not pixel precision) in Graphic mode 3 or 4.
The bitmaps have the only restriction, that they should not exceed 32 chars in width (wb <= 8*32 = 256)

Helpful background information:
1) A Mulitcolor Bitmap consist of 3 parts: The bitmap-data, color-data, luminance-data
2) Screen memory of bitmap-data starts at $2000
3) Screen memory of Luminance-data starts at $1800
4) Screen memory of color-data starts at $1C00

Precondition:
1)You have a bitmap file in any non full-screen size (width <= 32 chars).
2) Data is arranged in following order: Bitmap (w*h*8 Bytes), Color (w*h Bytes), Luminance (w*h Bytes) and loaded to the Cache address sa

Five input parameters:
Pointer to Cache-Start-Adress (sa),
Top-Left Position (x,y): 0 Bitmap dimensions Width, Height (w,h).

(Codeformat with no Codelines, but with Tags, please replace for yourself).

10 sa=DEC("6000") : REM Pointer to Cache-Startadresse
20 x=4:y=0 : REM Top-Left Position of Bitmap
30 w=32:h=10 : REM Dimension Chars width/height

100 wb=w*8: hf=h/2: ev=((hf)-int(hf)) :
110 if ev=0 then e=1:else e=0
120 if e=1 then hf=hf-1
130 q =sa : zi=8192 + x*8 + y*320
140 for k = 0 to hf
150 POKE192,((q ) and 255) : POKE193,(((q)/256) and 255)
160 POKE200,((zi) and 255) : POKE201,(((zi)/256)and 255)
170 if e=1 then q = q+wb : zi = zi + 320:else e=1
180 POKE169,((q ) and 255) : POKE170,(((q )/256) and 255)
190 POKE234,((zi) and 255) : POKE235,(((zi)/256) and 255)
200 q=q+wb : zi = zi + 320
210 POKE2024,wb-1:POKE2036,0:SYSDEC("DA4F")
220 next

230 k=0:q1 = sa+(w*h*8):q2=q1+(w*h) :
240 z1=DEC("1800")+x+y*40: REM Adress in LumanceMap
250 z2=z1+DEC("400"): REM Adress in ColorMap

260 ##COLLUMI
270 POKE192,(q1 and 255) : POKE193,((q1/256) and 255)
280 POKE200,(z1 and 255) : POKE201,((z1/256) and 255)
290 q1=q1+w : z1=z1+40 :
300 POKE169,(q2 and 255) : POKE170,((q2 /256) and 255)
310 POKE234,(z2 and 255) : POKE235,((z2 /256) and 255)
320 q2 = q2 + w: z2 = z2 + 40 :
330 POKE2024,w-1: POKE2036,0:SYSDEC("DA4F")
340 k = k+1:if k <=h then GOTO 260

For further information about how the code was developed look in the Forum at:
"Combining Text and freely placeable bitmaps on screen"
