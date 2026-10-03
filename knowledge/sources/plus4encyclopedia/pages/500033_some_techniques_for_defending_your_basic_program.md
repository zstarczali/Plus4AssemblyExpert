# Some Techniques For Defending Your BASIC Program

- Source: https://plus4world.powweb.com/plus4encyclopedia/500033
- Category: Programming/BASIC
- Keywords: list,defend See Also [How do I disable the Run/Stop key?](https://plus4world.powweb.com/kb.php?id=500013), [How do I disable SAVE function?](https://plus4world.powweb.com/kb.php?id=500034)

There are some suggestions if you wanna protect your BASIC code from abuse.

Typing POKE 772,22 a ?SYNTAX ERROR message will be printed out when you enter a command.
Typing POKE 772,77 a ?OUT OF MEMORY ERROR message will be printed out when you enter a command.
Typing POKE 772,44 the computer stucks when you enter a command.

You can hide a BASIC code with POKE 774,255. Reveal it back with POKE 774,110.
