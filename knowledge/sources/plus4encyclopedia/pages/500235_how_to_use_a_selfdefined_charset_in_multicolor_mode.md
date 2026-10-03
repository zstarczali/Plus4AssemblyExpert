# How To Use A Selfdefined Charset In Multicolor Mode

- Source: https://plus4world.powweb.com/plus4encyclopedia/500235
- Category: Programming/BASIC
- Keywords: Charset, Multicolor Credits George

If you want to use a selfdefined Charset in Multicolor Mode, be sure that your chars have 2x1 pixel width in the right position.

Precondition: You made a charset file (e.g Polybius) which load its content to address $1000 (or other free memory).

5 GRAPHIC 3,1
10 A=A+1
20 IF A=1 THEN LOAD"POLYBIUS",8,1
60 POKE 740,DEC("10")
80 CHAR 1,0,0,"A"
90 GETKEY A$

Background:
1) Make sure that you set Graphic mode before loading the charset.
2) the LOAD Command restarts the BASIC Programme, that's why we use the A as Flag.
