# DIM Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500071
- Category: Reference/Commodore BASIC V3.5

DIM *variable (subscripts)* [,*variable (subscripts)*]...

The DIM statement is used to establish the DIMensions of an array.

The statement DIM is followed by the variable name of the array. Then, enclosed in brackets, the number of elements in each dimension. The dimension values are seperated by commas. The number of dimensions is limited only by memory. Each array or dimension starts with element 0.

Arrays which are specified as integer arrays take up 2/5ths the space of floating point arrays.

Multiple arrays can be set with a single DIM statement by seperating the array names with commas.

If an array is referenced before it is defined by a DIM statement, BASIC automatically executes a DIM statement for that array with a dimension of 10.

The dimensions of an array can only be defined once. If a DIM statement is executed for the same array more than once (without a [CLR statement](500066_clr_statement.md)), a [?REDIM'D ARRAY ERROR](500175_redim_d_array_error.md) occurs.

Examples
`DIM A$(40)`  Dimensions the array A$ with 41 elements.
`DIM A$(40),B1(30),CC%(20)`  Dimensioning of multiple arrays
`DIM A1(5,6)`  Two-dimensional array containing a total of 42 elements
`DIM B2(4,4,4)`  Three-dimensional array containing 125 elements

Abbreviation
D SHIFT+I
