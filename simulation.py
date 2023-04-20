from cpu import CPU
#from arithmetic_logic_unit import ALU
from collections import deque

load_instructions = deque()

with open("instruction_input.txt") as instructions:
    for line in instructions.readlines():
        load_instructions.append(line)

processor = CPU()

