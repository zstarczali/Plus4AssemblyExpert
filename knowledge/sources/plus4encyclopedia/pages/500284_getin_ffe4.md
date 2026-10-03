# GETIN ($FFE4)

- Source: https://plus4world.powweb.com/plus4encyclopedia/500284
- Category: Programming/Assembly, Reference/KERNAL

With GETIN you get a character from the keyboard buffer. This means that the routine queries the keyboard. The entered character is passed to the accumulator. GETIN waits until a key is pressed and this works like the Basic [GET statement](500076_get_statement.md).

As an example, wait until a key is pressed and output character:

loop
. JSR $FFE4
. BEQ loop
. JSR $FFD2
