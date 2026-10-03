# USR Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500135
- Category: Reference/Commodore BASIC V3.5

USR(X)

This function returns a numeric value.

When this function is called, a machine language routine is executed at the memory location specified at location 1281-1282 ($0501-$0502, low byte-high byte format).

The location of the routine must be entered with the [POKE statement](500091_poke_statement.md) into locations 1281-1282. If no values have been entered, calling the USR function will cause an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md).

When the USR function is called, the value of X is placed into floating point accumulator #1 ($61-$66). When an RTS instruction (outside of a JSR subroutine) is executed, program execution returns to BASIC and the value in floating point accumulator #1 is returned by the USR function.

For immediate execution of a machine language program from BASIC, use the [SYS statement](500110_sys_statement.md).

Abbreviation
U SHIFT+S
