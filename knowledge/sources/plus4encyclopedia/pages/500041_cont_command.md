# CONT Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500041
- Category: Reference/Commodore BASIC V3.5

CONT

AKA CONTinue. Restarts execution of a BASIC program after pressing the STOP key, or after a [STOP statement](500109_stop_statement.md) or [END statement](500074_end_statement.md) within the program.

CONT will not work if lines are added, removed or reentered; if the program stopped due to an error; or if an error is caused in direct mode before restarting. In this case, a [?CAN'T CONTINUE ERROR](500181_can_t_continue_error.md) message will be displayed.

This command should only be used in direct mode. Technically it can also be used in a BASIC program, but a CONT statement will cause an infinite loop.

Abbreviation
C SHIFT+O
