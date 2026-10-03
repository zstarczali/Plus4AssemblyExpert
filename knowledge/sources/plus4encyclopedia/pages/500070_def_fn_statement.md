# DEF FN Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500070
- Category: Reference/Commodore BASIC V3.5

DEF FN*name (variable)* = *expression*

AKA DEFine FunctioN. Allows the definition of a complex calculation as a function. Once defined, the function can be used as a substitute for a long formula used repeatedly, which saves time and space.

This statement can only be used within a program. If it is used in direct mode, an [?ILLEGAL DIRECT ERROR](500160_illegal_direct_error.md) will occur.

A function must be defined before it is referenced in a program. Otherwise, an [?UNDEF'D FUNCTION ERROR](500182_undef_d_function_error.md) will occur.

The function name must start with FN, followed by a standard FP-numeric variable name. This is followed by a set of brackets () which enclose a FP-numeric variable. This is followed by an equal sign, followed by the formula to be defined. The purpose of the variable enclosed in brackets is to provide a means of manipulation of the formula. If this variable name is used within the formula, the value of this variable can be changed whenever the function is called. See example below:

Examples
`10 DEF FNA(X)=12*(34.75-X/.3)+X`
`20 PRINT FNA(7)`  When the function is called in this manner, the variable X is replaced with 7 in all instances of the variable name, so that the formula becomes: 12*(34.75-7/.3)+7
`30 B=5`
`40 PRINT FNA(B)`  The formula becomes: 12*(34.75-B/.3)+B

*** Note: The variable (X in the example) used in DEF FN() is only for referring, that is: a real variable with the same name could be used in other parts of programs without being affected by the DEF FN declaration. The same for the name (A in the example).

Abbreviation
D SHIFT+E
