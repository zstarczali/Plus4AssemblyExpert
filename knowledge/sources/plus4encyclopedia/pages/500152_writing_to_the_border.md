# Writing To The Border

- Source: https://plus4world.powweb.com/plus4encyclopedia/500152
- Category: Glossary/Demos, Programming/Assembly
- Keywords: Border, sideborder

The border of the screen by default is an area that programs cannot write to. It's a solid color, specified by TED register $FF19. This has been overcome by clever programmers.

The **upper/lower border** was the first one. The first program to do this was probably 1987's [Summer Events](https://plus4world.powweb.com/software/Summer_Events) by [Udo Gertz](https://plus4world.powweb.com/members/Udo_Gertz). [The Mad](https://plus4world.powweb.com/members/The_Mad) also did this in his games: [Invincible](https://plus4world.powweb.com/software/Invincible), [Digital Ball](https://plus4world.powweb.com/software/Digital_Ball) (upscroller), [Godzilla](https://plus4world.powweb.com/software/Godzilla) (intro screen).

The **sideborder** is a completely different story. All effects are done with $FF1E writing, with the exception of Five Magics.

- First ever side border effect: Master Computing in [MC Demo](https://plus4world.powweb.com/software/MC_Demo) then TCFS in [Dynamix](https://plus4world.powweb.com/software/Dynamix) intro (single file version). They were released about the same time, but TCFS admits that the idea is from MC. This effect is pretty weird, it uses a side effect of the monitor display (that's why YAPE can't emulate it properly).

- [Five Magics](https://plus4world.powweb.com/software/Five_Magics) (1998) is the first real one by Crown. It extends the sideborder by one char in each direction. The effect is rather limited though. However it's the only HIRES one so far. This effect uses $FF07.

- [Chaos](https://plus4world.powweb.com/software/Chaos) (2005): Larry's SAS (=eagle) routine (which was spread to many people) is finally released publicly. It extends the screen by a total of 3 characters, has to be multicolor by the nature of the effect. The colour map disappears, which allows 3 colors only ($FF15, $FF16 and black).

- [Crackers Demo 4](https://plus4world.powweb.com/software/Crackers_Demo_4) (2005): Essentially the same effect as in Chaos, but interlaced. This allows for 7 colors.

- [Rockstar Ate My Border](https://plus4world.powweb.com/software/Rockstar_Ate_My_Border) (2009): This 512 byte demo technically extends the screen by 5 characters (making it the widest so far), but also takes advantage of a strange effect, which allows for *every* character on the border to have pattern. This means there's no sideborder at all. There's no color map, so only 3 colors can be used ($FF15, $FF16 and black).
