# ?EXTRA IGNORED

- Source: https://plus4world.powweb.com/plus4encyclopedia/500191
- Category: Reference/BASIC Error Messages

The ?EXTRA IGNORED error message is not a standard error, but only occurs when using the [INPUT statement](500082_input_statement.md). It occurs when entering multiple items on a single INPUT prompt (seperated by commas) and too many items are entered.

It will also occur if a colon character is entered in a prompt for a single variable, or (when entering for multiple variables) the last variable.

Unlike normal error messages, program execution is not stopped when this error occurs.

When this error occurs, all items entered after the first excess comma or colon are ignored, and program execution continues after the INPUT statement.

ERR$ error number
N/A
