# RND Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500130
- Category: Reference/Commodore BASIC V3.5

RND(X)

This function returns a numeric value.

This function returns a RaNDom decimal number between 0 and 1.

If X is 1 (or any positive number), a random number is taken from the current seed. The seed is always the same when the computer is powered up/reset. Therefore, the first time the RND(1) function is called after starting up/resetting the computer, it will return 1.07870447E-03. If the computer is reset and RND(1) is called again, it will produce the exact same number.

If X is negative, the random number generator is re-seeded with that value.

If X is 0, the random number generator is re-seeded from the system clock. This should be used for the first random number in a program.

The RND function is often used in conjunction with the [INT function](500122_int_function.md) to produce whole numbers.

Examples
`INT(RND(1)*6+1)`  This allows for simulating the roll of a die. The INT function produces a whole number from the RND function. The random number is multiplied by 6, producing a random number between 0-5. To make this 1-6, +1 is added

Abbreviation
R SHIFT+N
