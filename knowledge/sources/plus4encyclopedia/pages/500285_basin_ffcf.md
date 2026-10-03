# BASIN ($FFCF)

- Source: https://plus4world.powweb.com/plus4encyclopedia/500285
- Category: Programming/Assembly, Reference/KERNAL

The routine is used to enter data via the keyboard or via a device that was previously defined with CHKIN ($FFC6). The input is comparable to the [INPUT statement](500082_input_statement.md) in Basic.

When called, the character is loaded into the accumulator and also displayed on the screen.

Here is an example until the RETURN key is pressed:

```
loop
. JSR $FFCF
. CMP #$0D
. BNE LOOP
. RTS
```
