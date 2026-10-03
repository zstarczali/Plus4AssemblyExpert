# 6502 Addressing Modes

- Source: https://plus4world.powweb.com/plus4encyclopedia/500016
- Category: Programming/Assembly
- Keywords: addressing modes

**What are addressing modes?** Most CPU instructions deal with the memory. When you access the memory, you can refer to it in various ways. For example, LDA $1021 would load memory location $1021 into the "A" register. Directly referring to memory location $1021 in this case is an example of "Absolute addressing mode". However, we could also use LDX #$21, LDA $1000,X. The ",X" part tells the CPU to look up the "X"th ($21th in this case) memory address from $1000. So esentially this example also reads the same memory location, but we've used "Absolute,X addressing mode".

**The 6502 has the following 13 addressing modes:**

Implicit addressing mode
Accumulator addressing mode
[Immediate addressing mode](500018_immediate_addressing_mode.md)
Zero Page addressing mode
Zero Page,X addressing mode
Zero Page,Y addressing mode
Relative addressing mode
[Absolute addressing mode](500017_absolute_addressing_mode.md)
Absolute,X addressing mode
Absolute,Y addressing mode
Indirect addressing mode
Indexed Indirect addressing mode
Indirect Indexed addressing mode
