# BASIC Tricks

- Source: https://plus4world.powweb.com/plus4encyclopedia/500203
- Category: Programming/BASIC

1) IF A<>0 can be reduced to IF A (warning: this trick must not be applied with multiple variables, es. IF A% AND B%)
2) GOTO 0 can be reduced to GOTO.
3) ....: GOTO 1000: here any string as comment is accepted without a REM (also works with ....: RETURN)
3b) DATA ... , ... :here any string as comment is accepted without a REM
4) NEXT x,y can be entered as NEXT: NEXT (runs faster)
5) IF ... THEN GOTO 2000 can be reduced to IF ... THEN 2000
6) ? FRE(n) is useful to pack string area by eliminating old useless strings (not a real trick)
7) To check if a file is existing: "RENAME a$ TO a$" (a$=filename). Results DS=62 file does not exist; DS=63 file exists.
8) CHAR ,x,y,"[CLR]" to clear screen and cancel all possible windows (x,y any legal value)
9) "IF ev = 0 THEN e= -1: ELSE e = 0" can be reduced to: "e=ev=0"
10) Flip 0<->1 in a variable. "IF a%=1 then a%=0: ELSE a%=1" can be reduced to: "a%=abs(a%-1)"

Credits
SVS
