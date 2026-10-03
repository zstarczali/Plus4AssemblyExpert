# Disable C= + Shift

- Source: https://plus4world.powweb.com/plus4encyclopedia/500202
- Category: Programming/General

To disable C= + Shift (which switches between uppercase and lowercase font):

?CHR$(8)
or
POKE1351,128  from basic
>0547 80  from monitor

This function is also automatically disabled when 256 character font is used.

To re-enable: CTRL-I
