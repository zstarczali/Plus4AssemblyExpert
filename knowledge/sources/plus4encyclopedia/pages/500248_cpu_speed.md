# CPU Speed

- Source: https://plus4world.powweb.com/plus4encyclopedia/500248
- Category: Hardware

| crystal | FF07 #6 | FF06 #4 | FF13 #1 | FPS | TED freq | CPU freq | % PALC64 |
|---|---|---|---|---|---|---|---|
| PAL | PAL | TRUE | FALSE | 49.86075967 | 1,773,448 | 1,147,196 | 116% |
| PAL | PAL | TRUE | TRUE | 49.86075967 | 1,773,448 | 779,523 | 79% |
| PAL | PAL | FALSE | FALSE | 49.86075967 | 1,773,448 | 1,695,665 | 172% |
| PAL | PAL | FALSE | TRUE | 49.86075967 | 1,773,448 | 886,724 | 90% |
| PAL | NTSC | TRUE | FALSE | 74.22021478 | 2,216,809 | 1,303,159 | 132% |
| PAL | NTSC | TRUE | TRUE | 74.22021478 | 2,216,809 | 948,831 | 96% |
| PAL | NTSC | FALSE | FALSE | 74.22021478 | 2,216,809 | 2,119,581 | 215% |
| PAL | NTSC | FALSE | TRUE | 74.22021478 | 2,216,809 | 1,108,405 | 113% |
| NTSC | PAL | TRUE | FALSE | 40.25579172 | 1,431,818 | 926,205 | 94% |
| NTSC | PAL | TRUE | TRUE | 40.25579172 | 1,431,818 | 629,359 | 64% |
| NTSC | PAL | FALSE | FALSE | 40.25579172 | 1,431,818 | 1,369,019 | 139% |
| NTSC | PAL | FALSE | TRUE | 40.25579172 | 1,431,818 | 715,909 | 73% |
| NTSC | NTSC | TRUE | FALSE | 59.92274340 | 1,789,773 | 1,052,124 | 107% |
| NTSC | NTSC | TRUE | TRUE | 59.92274340 | 1,789,773 | 766,052 | 78% |
| NTSC | NTSC | FALSE | FALSE | 59.92274340 | 1,789,773 | 1,711,274 | 174% |
| NTSC | NTSC | FALSE | TRUE | 59.92274340 | 1,789,773 | 894,886 | 91% |

Same table with monospaced formatting:

```

crystal   FF07 #6   FF06 #4   FF13 #1   FPS         TED freq    CPU freq    % PALC64
---------+---------+---------+---------+-----------+-----------+-----------+---------+
PAL       PAL       TRUE      FALSE     49.86075967   1,773,448   1,147,196      116%
PAL       PAL       TRUE      TRUE      49.86075967   1,773,448     779,523       79%
PAL       PAL       FALSE     FALSE     49.86075967   1,773,448   1,695,665      172%
PAL       PAL       FALSE     TRUE      49.86075967   1,773,448     886,724       90%
PAL       NTSC      TRUE      FALSE     74.22021478   2,216,809   1,303,159      132%
PAL       NTSC      TRUE      TRUE      74.22021478   2,216,809     948,831       96%
PAL       NTSC      FALSE     FALSE     74.22021478   2,216,809   2,119,581      215%
PAL       NTSC      FALSE     TRUE      74.22021478   2,216,809   1,108,405      113%
NTSC      PAL       TRUE      FALSE     40.25579172   1,431,818     926,205       94%
NTSC      PAL       TRUE      TRUE      40.25579172   1,431,818     629,359       64%
NTSC      PAL       FALSE     FALSE     40.25579172   1,431,818   1,369,019      139%
NTSC      PAL       FALSE     TRUE      40.25579172   1,431,818     715,909       73%
NTSC      NTSC      TRUE      FALSE     59.9227434    1,789,773   1,052,124      107%
NTSC      NTSC      TRUE      TRUE      59.9227434    1,789,773     766,052       78%
NTSC      NTSC      FALSE     FALSE     59.9227434    1,789,773   1,711,274      174%
NTSC      NTSC      FALSE     TRUE      59.9227434    1,789,773     894,886       91%
```

CPU frequencies in modes where the display enable ("border") bit is is set are lowest guaranteed. Actual frequencies can be 1-3 cycles more per bad/DMA line depending on whether or not the CPU is executing write cycles. This has a theoretical upside potential of an additional 50 × 3 = 150 cycles per frame. The reference C64 CPU frequency is the maximum frequency with all - character as well as sprite - DMA off.

How long does one CPU cycle take?

| double clock | 1 CPU cycle ~= 0.5 µs | 1 NOP (2 cycles) ~= 1 µs |
|---|---|---|
| single clock | 1 CPU cycle ~= 1.0 µS | 1 NOP (2 cycles) ~= 2 µS |
