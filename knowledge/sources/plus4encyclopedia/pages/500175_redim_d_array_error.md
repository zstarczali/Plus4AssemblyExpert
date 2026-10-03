# ?REDIM'D ARRAY ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500175
- Category: Reference/BASIC Error Messages

Arrays can only have their dimensions set once. This error occurs if a [DIM statement](500071_dim_statement.md) is used on an array for a second time, or if a DIM statement is used on a previously referenced array (BASIC automatically executes DIM statements for such arrays, with a default dimension of 10). An array can only be redimensioned after a [CLR statement](500066_clr_statement.md) (which resets all variables) is executed first.

Examples
`10 DIM A(20)
20 A(15)=1
30 DIM A(25)`  Causes the error

`10 A(5)=5
20 DIM A(15)`  Causes the error

ERR$ error number
19
