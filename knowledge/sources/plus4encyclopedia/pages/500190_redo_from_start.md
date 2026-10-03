# ?REDO FROM START

- Source: https://plus4world.powweb.com/plus4encyclopedia/500190
- Category: Reference/BASIC Error Messages

The ?REDO FROM START error message is not a standard error, but only occurs when using the [INPUT statement](500082_input_statement.md). It occurs when an attempt is made to enter string data when INPUT is expecting numeric data (similar to [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md)).

Unlike normal error messages, program execution is not stopped when this error occurs.

When this error occurs, a new input prompt is shown, and data entry restarts at the first variable specified in the INPUT statement.

ERR$ error number
N/A
