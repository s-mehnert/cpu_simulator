from cpu import CPU
from collections import deque

load_instructions = deque()

with open("instruction_input.txt") as instructions:
    for line in instructions.readlines():
        load_instructions.append(line)

instruction_set_architecture = {
    "CACHE": "Cache Command",
    "ADDI": "Addition Operation",
    "ADD": "Addition Operation",
    "J": "Jump Command",
    "HALT": "Terminate Execution Command"
}

processor = CPU()


while load_instructions:
    processor.fetch_instruction(load_instructions.popleft())
    processor.decode_instruction(instruction_set_architecture)

print("\nAll instructions processed.")
