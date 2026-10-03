# BASIC Format

- Source: https://plus4world.powweb.com/plus4encyclopedia/500211
- Category: Programming/BASIC

This topic explains how BASIC lines and variables are stored in memory.

How BASIC lines are stored in memory:

[lo][hi]: pointer to next line's address in memory
[lo][hi]: line number hex equivalent of (0-63999)
[tokenized BASIC line]
[$00]: end of line marker

After the last line, the next "line" has $00 $00 as the next line memory address.

How variables are stored:
Single variables (non-arrays) are stored on 7 bytes:
2 bytes: variable name and flags, indicating type.
5 bytes: variable value, dependent on variable type.

| Variable type | Example name | Flags | Value |
|---|---|---|---|
| Floating point number | A | $00 $00 | See below |
| String | A$ | $00 $80 | (len)(hi)(lo)($00)($00) Length of the string, address pointing to the string, 2 bytes unused |
| Function | FNA(0) | $80 $00 | (lo)(hi)(lo)(hi)(hh) 16 bit address of text in BASIC line containing the expressing, 16 bit address to value of local variable used in DEF FN, last byte contains the first character after "=" in DEF FN |
| Integer number | A% | $80 $80 | (hi)(lo)($00)($00)($00) Signed 16 bit value, 3 bytes unused |

Note: the variable names alone are not unique, the name + type is unique. That is, in BASIC you can have for variables called "A": A (floating point), A% (integer), A$ (string) and FNA(0) (function), each with it's own independent value.

Name examples:
$41 $00 = A (floating point)
$42 $80 = B$ (string)
$C3 $00 = FNC (function)
$C4 $80 = D% (integer)

Arrays:
[lo][hi][S][hi E][lo E]

[lo][hi] is a 16 bit number the specifies the size of the entire array data structure. (2 for variable name + 5 for the array variable + (elements)*(size).
[S] is an 8 bit number, the Start index of the array plus 1.
[hi E][lo E] Finally we have another 16 bit number, the End index of the array plus 1.

Example: for an array that has the default dimensions of 11 elements, starting with element zero (e.g. A(0)=0 would declare this array), this would be:
3E 00 01 00 0B (This is followed by the array variable values.)

The array size $3E = 62. 11 elements * 5 bytes = 55, +5 + 2 = 62.

Floating Point Numbers

Floating point numbers take up 5 bytes like other variables. Here's the breakdown of what those bytes mean:
[ee][m1][m2][m3][m4]

[ee] is the 8-bit exponent. If zero, the whole number is zero, regardless of the mantissa. The exponent is stored with +129 bias so that any number will appear in standard positive form as 1.XXXX... x 2^e.
[NOTE: It is important to see that the standard form is binary rather than decimal, and each place represents a power of 2. So a number such as 1.011 = 1 x 2^0 + 0 x 2^-1 + 1 x 2^-2 + 1 x 2^-3 = 1 + .25 + .125 = 1.375]

[m1-m4] is the 32-bit mantissa. Two important things to note: the highest bit of [m1] is the sign bit (0 = positive number, 1 = negative number). The mantissa, minus the leading sign bit, is the fractional part of the standard form ( the .XXXXX... )

Let's see an example:

3 is stored as $82 $40 $00 $00 $00. This means the exponent is 1 ($82 = 130, 130 - 129 = 1).

It's a positive number (highest bit of mantissa is not set).

(In what follows, we'll drop the 24 trailing 0s [m2][m3][m4] for brevity.)
Placing the mantissa in standard form means (1) dropping the sign bit [ $40 in binary 01000000 becomes 1000000] (2) adding the implied "1" to the left of the binary point[ 1000000 becomes 11000000] The mantissa represents a number in standard form so we need only insert the binary point giving 1.1000000.

Putting it all together, we have to add the exponent calculated earlier to get everything in the standard form of
(sign) x 1.XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX x 2^e =
+ 1.1 x 2^1 = (2^0 + 2^-1) x 2 = 1.5 x2 =3.
