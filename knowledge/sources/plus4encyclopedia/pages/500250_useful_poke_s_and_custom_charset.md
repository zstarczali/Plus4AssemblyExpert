# Useful POKE's And Custom Charset

- Source: https://plus4world.powweb.com/plus4encyclopedia/500250
- Category: Programming/BASIC

With the following POKEs, you can switch the auto reverse, multicolor and 38/40 columns on custom charset:

poke65287,peek(65287)and64or0:rem ...auto-revers on, multicolor off, 38 colums
poke65287,peek(65287)and64or8:rem ...auto-revers on, multicolor off, 40 columns
poke65287,peek(65287)and64or16:rem ...auto-revers on, multicolor on, 38 colums
poke65287,peek(65287)and64or24:rem ...auto-revers on, multicolor on, 40 columns
poke65287,peek(65287)and64or128:rem ...auto-revers off, multicolor off, 38 colums
poke65287,peek(65287)and64or136:rem ...auto-revers off, multicolor off, 40 columns
poke65287,peek(65287)and64or144:rem ...auto-revers off, multicolor on, 38 colums
poke65287,peek(65287)and64or152:rem ...auto-revers off, multicolor on, 40 columns

On 38 columns it shows only 38 chars per row. The 2 others are behind the border!

0 rem ...copy charset from rom to ram at $4800...
1 restore:fora=832to849:readb:pokea,b:next:sys832
2 data162,0,189,0,208,157,0,72,189,0,209,157,0,73,202,208,241,96

The 8th byte (72 / $48) and the 14th byte (73 / $49) are the destination addresses to copy the charset to.

10 rem ...edit the copied chars (see above)...
20 fora=18944to18999:readb:pokea,b:next
30 poke65298,peek(65298)and251:poke65299,peek(65299)and3or72
40 data255,102,195,195,102,255,0,0,126,102,126,102,126,102,126,102
50 data60,126,135,215,215,255,255,219,60,126,225,235,235,255,255,219
60 data14,24,126,223,255,255,255,126,54,36,126,195,235,255,247,126
70 data108,36,126,195,215,255,239,126

Line 30: switch from standard charset to the custom at address 72 ($4800)

poke65301,x(x=0-127): rem background color
poke65302,x(x=0-127): rem multicolor #1
poke65303,x(x=0-127): rem multicolor #2
poke65305,x(x=0-127): rem border color
poke65286,0:rem ...screen off (the program runs ca. 20% faster)...
poke65286,27:rem ...screen on...

With the following snippet, you can simulate keystrokes:

10 printchr$(147)"print"chr$(34)"a little test"chr$(34)
20 poke1319,19:rem ...1 x home...
30 poke1320,13:rem ...1 x return...
40 poke 239,2:rem ...2 keys to play...
