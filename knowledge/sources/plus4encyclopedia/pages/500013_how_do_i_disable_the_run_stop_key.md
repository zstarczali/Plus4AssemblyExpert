# How Do I Disable The Run/Stop Key?

- Source: https://plus4world.powweb.com/plus4encyclopedia/500013
- Category: Programming/BASIC
- Keywords: disable run stop,disable run/stop,disable runstop,

The Run/Stop key is handled by the BASIC STOP vector, which is located at **$0326/$0327** (806/807). The default value of the vector is **$F265**.

Because BASIC execution is too slow to change both bytes of this vector, normally only the **low byte** ($0326/806) is changed. By analyzing all BASIC programs in our database, we found the following usage:

| POKE value | Number of programs | Example program(s) | Effects |
|---|---|---|---|
| 24 | 1 | [Quarterback](https://plus4world.powweb.com/software/Quarterback) | Works, noticeable slowdown in execution (1) |
| 32 | 2 | [Logi-Toli](https://plus4world.powweb.com/software/Logi-Toli), [Amiga Emu](https://plus4world.powweb.com/software/Amiga_Emu) | Works, noticeable slowdown in execution (1) |
| 35 | 2 | [Blokovnica](https://plus4world.powweb.com/software/Blokovnica), [Cokin Super](https://plus4world.powweb.com/software/Cokin_Super) | Works, noticeable slowdown in execution (1) |
| 101 | 7 | [Multi-disk Hungarian](https://plus4world.powweb.com/software/Multi-disk_Hungarian) | Enable only (restores the default value) |
| 103 | 57 | [Fantil](https://plus4world.powweb.com/software/Fantil), [Push Back](https://plus4world.powweb.com/software/Push_Back), [Varia](https://plus4world.powweb.com/software/Varia) | Works, unsafe (2) |
| 115 | 6 | [Popesys](https://plus4world.powweb.com/software/Popesys), [Directory Filer](https://plus4world.powweb.com/software/Directory_Filer) | Works, SOUND statement hangs (3) |
| 132 | 3 | [Pojmaj Slovo!](https://plus4world.powweb.com/software/Pojmaj_Slovo), [Európa (OKTA)](https://plus4world.powweb.com/software/Europa_OKTA) | Works, SOUND statement hangs (3) |
| 136 | 3 | [A Hős Lovag](https://plus4world.powweb.com/software/A_Hos_Lovag), [A Bűvös Gyűrű](https://plus4world.powweb.com/software/A_Buvos_Gyuru) | Works, SOUND statement hangs (3) |
| 237 | 1 | [Primus](https://plus4world.powweb.com/software/Primus) | Odd side effects, SOUND statement hangs (3) |

The ROM was not designed with this in mind; we're changing the $F265 address to another "random" address (from $F200-$F2FF, since only the low byte is changed), but none of them are fully suitable. Here is the breakdown of the side effects.

**(Group 1) 24 / 32 / 35**: these values work, but the BASIC program will run *noticeably slower*. The reason for this is that the vector is redirected to extra useless JSR statements. Not recommended; disabling the Run/Stop key is not worth the worsened performance.

**(Group 3) 115 / 132 / 136 / 237**: these values do not work if your program uses the [SOUND statement](500106_sound_statement.md). Example:

0 POKE806,115
1 VOL4:F=F+1:SOUND1,F,1:GOTO0

The program will hang as soon as it reaches the SOUND statement.

**103**: From the table, we can see that this is the **most common method** used by far. It does mostly work, however, it is "unsafe". The default code at $F265 starts with LDA $91 / CMP #$7F, which checks the location of $91 and compares it with $7F (127) to see if Run/Stop is pressed. This POKE points the vector to $F267, which "skips" the LDA statement. Therefore, the CMP statement will still execute, but the value that it compares it with is "undetermined" (whatever happened to be in the A register). If the rest of the code uses POKE or PEEK, and the value POKEd or PEEKed is 127, the program will stop. Here's an example:

0 POKE806,113
1 POKE3072,127:GOTO0

The program will stop in LINE 1. Note that if we omit the Run/Stop disabling POKE, it works fine.

You may be asking: can we "skip" the entire vector by pointing it to an RTS opcode, so that it does "nothing"? Unfortunately, this doesn't work *at all*. POKE 806, 114 would achieve this, but this causes the BASIC program not to run at all. The problem is, this vector must return with the zero flag *not set*.

What is a proper (doesn't slow down the code, allows SOUND statements, doesn't break for PEEK/POKEs)? One possible method is this: we POKE a short routine to any free memory area with the low byte being $65 - therefore only the high byte of the vector needs to be changed. Writing LDA #$01 / RTS to $0365 would work:

**POKE 869, 169 : POKE 870, 1 : POKE 871, 96 : POKE 807, 3**

A similar method has been used in the following programs:
[Pojmaj Slovo!](https://plus4world.powweb.com/software/Pojmaj_Slovo), [Európa (OKTA)](https://plus4world.powweb.com/software/Europa_OKTA), [Otritsanie](https://plus4world.powweb.com/software/Otritsanie) (earliest is 1986, by László Agócs) using 7 POKEs.
[Castle Matcher](https://plus4world.powweb.com/software/Castle_Matcher), [Felcsút Tycoon](https://plus4world.powweb.com/software/Felcsut_Tycoon), [The Librarian](https://plus4world.powweb.com/software/The_Librarian) (earliest is 2017, by RoePipi) using only a single POKE. The ML part cleverly hidden in the BASIC code and falls exactly to $1065.

Another alternative:
POKE 807, 228 : POKE 806, 13
This will redirect the vector to $E40D in two steps. The order matters; the high byte must be changed first.

Alternative #1
Use POKE 786,68 for the same effect. You can enable it with POKE 786,66. This also hangs the SOUND statement.

Alternative #2
Another method is using the combination of TRAP and RESUME NEXT BASIC commands.

For example:

```
10 TRAP 100
20 PRINT "HELLO"
30 GOTO 20
100 RESUME NEXT
```

However, the program can be stopped by pressing the Run/Stop key multiple times within short period of time.
