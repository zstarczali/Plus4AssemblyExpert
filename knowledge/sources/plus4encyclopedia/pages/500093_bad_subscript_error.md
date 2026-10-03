# ?BAD SUBSCRIPT ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500093
- Category: Reference/BASIC Error Messages

This error occurs if a reference is made to an array element outside the boundaries of the array.

Examples
`PRINT A(-1)`  negative indexes are not allowed.
`PRINT A(11)`  will cause this error. Remember that arrays that are not explicitly declared with [DIM statement](500071_dim_statement.md) have elements from 0-10.
`10 DIM A$ (20):A$ (21) = "OOPS!"`  will cause this error, since 21 is outside the array boundary.

ERR$ error number
18
