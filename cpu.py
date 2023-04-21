# The code in this file will simulate the FETCH -> DECODE -> EXECUTE -> STORE instruction cycle a Central Processing Unit (CPU) performs

from collections import deque


class CPU:
    def __init__(self):
        self.program_counter = None
        self.instruction_register = None
        self.registers = {1 : None, 2 : None, 3 : None, 4 : None, 5 : None, 6 : None, 7 : None, 8 : None}
            
    def fetch_instruction(self, instruction): # instructions will come in the form of a string
        print("Fetching instruction:", instruction, )
        if instruction == None:
            print("No instruction to be fetched.")
            return
        instruction = instruction.strip().split(",")
        if self.instruction_register == None:
            self.instruction_register = instruction
            print("Loading instruction into IR:", self.instruction_register)
            print("Ready for decoding.")
        else:
            print("Cannot fetch instruction as previous instruction is still waiting in line.")

    def decode_instruction(self, is_architecture):
        print("Decoding instruction:", self.instruction_register)
        instruction = deque()
        for item in self.instruction_register:
            instruction.append(item)
        
        command = instruction.popleft()
        decoded_instruction = is_architecture[command]
        print(decoded_instruction)
        if not instruction:
            return decoded_instruction
        if command == "J":
            fetch_from_register = instruction.popleft()
            self.fetch_instruction(self.registers[int(fetch_from_register)])
            decoded_instruction += ": jumping to register " + fetch_from_register

        print("So far decoded:", decoded_instruction)
        print("Now decoding rest of instruction:", instruction)
        destination_register = ""
        source_register_1 = ""
        source_register_2 = ""
        constant = 0
        
        print("Ready to pass instruction to ALU", self.instruction_register)

    def pass_instruction_to_ALU(self):
        print("Passing instruction to ALU:", self.instruction_register)
        self.instruction_register = None # temporary solution for testing
        print("Clearing IR:", self.instruction_register)        

    def receive_result_from_ALU(self):
        pass

    def store_result(self):
        pass



