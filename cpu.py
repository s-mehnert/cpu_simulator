# The code in this file will simulate the FETCH -> DECODE -> EXECUTE -> STORE instruction cycle a Central Processing Unit (CPU) performs


class CPU:
    def __init__(self):
        self.registers = [] * 8
        self.program_counter = None
        self.instruction_register = None
    
    def fetch_instruction(self, instruction): # instructions will come in the form of a string
        instruction.split(",")
        if self.instruction_register == None:
            self.instruction_register = instruction
            print("Fetching instruction.", instruction)
            print("Loading instruction into IR", self.instruction_register)
            print("Ready for decoding.")
        else:
            print("Cannot fetch instruction as previous instruction is still waiting in line.")

    def decode_instruction(self):
        pass

    def pass_instruction_to_ALU(self):
        print("Passing instruction to ALU:", self.instruction_register)
        self.instruction_register = None # temporary solution for testing
        print("Clearing IR:", self.instruction_register)        

    def receive_result_from_ALU(self):
        pass

    def store_result(self):
        pass



