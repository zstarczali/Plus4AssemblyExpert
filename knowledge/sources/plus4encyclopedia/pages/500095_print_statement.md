# PRINT# Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500095
- Category: Reference/Commodore BASIC V3.5

PRINT# *file#*,*print list*

This is similar to the [PRINT statement](500094_print_statement.md), but is used to print to other devices, which are accessed under files opened with the [OPEN statement](500089_open_statement.md).

The word PRINT# is followed by the file number, which is followed by a comma, and then the items to be printed. The items and symbols used are the same as in the PRINT statement. NOTE: The [SPC function](500147_spc_function.md) and [TAB function](500148_tab_function.md) may not work with some devices.

Warnings:
To send more than one datum with a PRINT# statement, you have to mind these rules:
a) INPUT# command always will read all the data between two CHR$(13), doesn't care any inside separator;
b) INPUT# command is able to read at max 88 characters at once;
c) If data inside list have no separator the result is an unique string (for example: PRINT#3,"ABC";"DEF" will be stored as "ABCDEF")
d) Legal separators are: "," or ":". A possible character $00 will stop the transfer of the following characters until next CHR$(13)
e) To insert a separator inside the list of data, you have to specifically declare it (for example to insert a "," type: PRINT#3,"ABC";**","**;"DEF" or "ABC,DEF")
f) If data of variables already contain separator characters inside, to correctly read them you have to use GET# command, in order to read one character a time. (Example: if A$="time 13:30" when saved it cannot be correctly read by an INPUT# because the ":")
g) Character ":" is a terminator character. If met during reading, no further characters will be assigned to the variable (even if stored).
h) Characters "," and ";" work in the same way than PRINT statement, that is:
- "," moves cursor to next tabulation (or inserts spaces);
- ";" does insert nothing, neither CHR$(13).
*Example1: PRINT# 2,8,2,"ABC","DEF" system will store "ABC_________________DEF". Example2: PRINT# 2,8,2,"ABC";"DEF" system will store "ABCDEF".*

Examples
`PRINT# 1,"HELLO",A$ `  Sends data of A$ to file 1
`PRINT# 1,"HELLO",A$;B$ `  Sends data of A$+B$ (unified string) to file 1
`PRINT# 1,"HELLO",A$;",";B$ `  Sends data of A$+","+B$ to file 1 (can be read by INPUT# 1,A$,B$ if total lenght is not greater than 88)

Abbreviation
P SHIFT+R
