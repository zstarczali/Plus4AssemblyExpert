# How To Simulate Keystrokes

- Source: https://plus4world.powweb.com/plus4encyclopedia/500154
- Category: Programming/BASIC

The keyboard buffer is from address 1319 ($527). By [POKE](500091_poke_statement.md)-ing to this address, it is possible to simulate keystrokes. The number of keystroker still in the keyboard buffer is at address 239 ($EF).
Keyboard buffer can hold up to 10 characters.

By placing keystrokes into the buffer and ENDing a basic program, it is possible to perform BASIC commands (or MONITOR commands) in direct mode.

Examples
POKE 1319,13 : POKE 239,1  REM this places a keystroke 13 (=return key) into the buffer.
A$="HELLO" : FOR I = 1 TO LEN(A$) : POKE 1318+I, ASC(MID$(A$,I)) : NEXT I : POKE 239, LEN(A$)  REM types the word HELLO
