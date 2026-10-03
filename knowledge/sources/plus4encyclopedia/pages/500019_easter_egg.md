# Easter Egg

- Source: https://plus4world.powweb.com/plus4encyclopedia/500019
- Category: Programming/General
- Keywords: easter egg

On any 264-series machine, enter SYS 52651 ($CDAB) to display some of the names of the 264 project engineers:
- F.Bowen (displayed in inverse)
- J.Cooper
- B.Herd
- T.Ryan (displayed flashing)

The full names are Fred Bowen, John Cooper, Terry Ryan and [Bil Herd](https://plus4world.powweb.com/members/Bil_Herd).

Note: The hex address for 52651 is $CDAB. Also, the names are encrypted (XOR $55) in the RAM, so they won't show up in the memory dump.

More names:
Type MONITOR and press return at the prompt.
Type MBC20 and press return.
Three names will be visible in the memory dump:
- Fred B.
- Terry R.
- Mike I.
Note: Fred Bowen and Terry Ryan appear in both lists. This one is not encrypted.
