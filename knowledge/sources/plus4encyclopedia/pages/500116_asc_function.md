# ASC Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500116
- Category: Reference/Commodore BASIC V3.5

ASC(X$)

This function returns a numeric value.

This function returns the CHR$ code of the **first character** in X$. If X$ is an empty string, zero is returned. It is the opposite of the [CHR$ function](500137_chr_function.md).

Examples
?ASC("A")  Prints 65
?ASC("FIRST ONLY")  Prints 70
IF ASC(A$) >= 48 AND ASC(A$) <= 57 THEN ?"DIGIT"  Prints "digit" if A$ contains a digit

Abbreviation
A SHIFT+S

Basic Token
$C6
