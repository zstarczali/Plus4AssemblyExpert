# Frequency Table

- Source: https://plus4world.powweb.com/plus4encyclopedia/500243
- Category: Programming/Audio
- Keywords: Freq table

| Note | Frequency (Hz) | NTSC TED Value | NTSC TED Value (hex) | PAL TED Value | PAL TED Value (hex) |
|---|---|---|---|---|---|
| A6 | 1760 | 960 | $03C0 | 961 | $03C1 |
| G#6 | 1661 | 957 | $03BD | 957 | $03BD |
| G6 | 1568 | 953 | $03B9 | 953 | $03B9 |
| F#6 | 1480 | 948 | $03B4 | 949 | $03B5 |
| F6 | 1397 | 944 | $03B0 | 945 | $03B1 |
| E6 | 1319 | 939 | $03AB | 940 | $03AC |
| D#6 | 1245 | 934 | $03A6 | 935 | $03A7 |
| D6 | 1175 | 929 | $03A1 | 930 | $03A2 |
| C#6 | 1109 | 923 | $039B | 924 | $039C |
| C6 | 1047 | 917 | $0395 | 918 | $0396 |
| B5 | 988 | 911 | $038F | 912 | $0390 |
| A#5 | 932 | 904 | $0388 | 905 | $0389 |
| A5 | 880 | 897 | $0381 | 898 | $0382 |
| G#5 | 831 | 889 | $0379 | 891 | $037B |
| G5 | 784 | 881 | $0371 | 883 | $0373 |
| F#5 | 740 | 873 | $0369 | 874 | $036A |
| F5 | 698 | 864 | $0360 | 865 | $0361 |
| E5 | 659 | 854 | $0356 | 856 | $0358 |
| D#5 | 622 | 844 | $034C | 846 | $034E |
| D5 | 587 | 834 | $0342 | 835 | $0343 |
| C#5 | 554 | 822 | $0336 | 824 | $0338 |
| C5 | 523 | 810 | $032A | 812 | $032C |
| B4 | 494 | 798 | $031E | 800 | $0320 |
| A#4 | 466 | 784 | $0310 | 786 | $0312 |
| A4 | 440 | 770 | $0302 | 772 | $0304 |
| G#4 | 415 | 755 | $02F3 | 757 | $02F5 |
| G4 | 392 | 739 | $02E3 | 741 | $02E5 |
| F#4 | 370 | 722 | $02D2 | 724 | $02D4 |
| F4 | 349 | 704 | $02C0 | 707 | $02C3 |
| E4 | 330 | 685 | $02AD | 688 | $02B0 |
| D#4 | 311 | 664 | $0298 | 668 | $029C |
| D4 | 294 | 643 | $0283 | 646 | $0286 |
| C#4 | 277 | 620 | $026C | 624 | $0270 |
| C4 | 262 | 596 | $0254 | 600 | $0258 |
| B3 | 247 | 571 | $023B | 575 | $023F |
| A#3 | 233 | 544 | $0220 | 548 | $0224 |
| A3 | 220 | 516 | $0204 | 520 | $0208 |
| G#3 | 208 | 485 | $01E5 | 490 | $01EA |
| G3 | 196 | 453 | $01C5 | 458 | $01CA |
| F#3 | 185 | 419 | $01A3 | 425 | $01A9 |
| F3 | 175 | 383 | $017F | 389 | $0185 |
| E3 | 165 | 345 | $0159 | 351 | $015F |
| D#3 | 156 | 305 | $0131 | 311 | $0137 |
| D3 | 147 | 262 | $0106 | 269 | $010D |
| C#3 | 139 | 217 | $00D9 | 224 | $00E0 |
| C3 | 131 | 169 | $00A9 | 177 | $00B1 |
| B2 | 123 | 118 | $0076 | 126 | $007E |
| A#2 | 117 | 64 | $0040 | 73 | $0049 |
| A2 | 110 | 7 | $0007 | 16 | $0010 |

Generating this table
The values in this table can be printed with the following BASIC program:
`0 D=1.0594631:F=440*4
1 V=1024-(111860.781/F)
2 PRINTINT(F+.5);INT(V+.5);
3 F=F/D
4 IFF>=110THEN1`

Notes
Note: change 111860.781 is the NTSC value. Use 110840.4375 for PAL.

The formula was taken from [Commodore Plus/4 User's Manual](https://plus4world.powweb.com/publications/Commodore_Plus4_Users_Manual), page 204, where a similar table appears. The value for PAL is mistakenly printed as "111840" instead of "110840".

Usage
You can use these values in the [SOUND statement](https://plus4world.powweb.com/kb.php?id=500106). For example, to play a C major chord (consisting of notes C, E, G - or do, mi, sol) on an NTSC machine, type the following:
VOL8:SOUND1,810,3:SOUND1,854,3:SOUND1,881,3
