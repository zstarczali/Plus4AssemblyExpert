# ?OUT OF DATA ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500170
- Category: Reference/BASIC Error Messages

This error occurs when a [READ statement](500099_read_statement.md) is executed after all values in [DATA statement](500069_data_statement.md)s have been already read, or if there are no DATA statements at all in a program.

To re-read DATA statements, use the [RESTORE statement](500101_restore_statement.md).

In most cases, this error is caused indirectly by errors elsewhere in the program, such as READ statements nested within too many FOR loops, or DATA statements that are either misspelled, missing or wrongly entered.

Example
`10 FOR A = 1 TO 5:READ B(A):NEXT
20 DATA 1,2,3,4`
The error will occur in this program, as the FOR loop will execute the READ statement 5 times, but there are only 4 DATA items. The error may be corrected either by reducing the number of FOR loops to 4, or by adding a 5th DATA item

ERR$ error number
13
