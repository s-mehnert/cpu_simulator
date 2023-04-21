# The code in this file will simulate the FETCH -> DECODE -> EXECUTE -> STORE instruction cycle a Central Processing Unit (CPU) performs

from collections import deque


class CPU:
    def __init__(self):
        self.program_counter = None
        self.instruction_register = None
        self.registers = {1 : None, 2 : None, 3 : None, 4 : None, 5 : None, 6 : None, 7 : None, 8 : None}
            
    def clear_instruction_register(self):
        self.instruction_register = None

    def reset_registers(self):
        for key, value in self.registers:
            self.registers[key] = None
    
    def fetch_instruction(self, instruction): # instructions will come in the form of a string
        print("\nFetching instruction:", instruction)
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
        print("\nDecoding instruction:", self.instruction_register)
        instruction = deque()
        for item in self.instruction_register:
            instruction.append(item)
        decoded_instruction = {
            "command" : None, 
            "dest_reg" : None, 
            "source_reg_1" : None, 
            "source_reg_2" : None, 
            "constant" : None, 
            "jump_to_reg" : None,
            "code" : None
            }
        command = instruction.popleft()
        decoded_instruction["command"] = command
        explanation = is_architecture[command]
        while instruction:
            if command == "J":
                jump_to_reg = instruction.popleft()
                decoded_instruction["jump_to_reg"] = jump_to_reg
                explanation += ": jumping to register " + jump_to_reg
            elif command == "HALT":
                instruction.popleft()
                explanation += ": terminating program execution"
            elif command == "CACHE":
                code = instruction.popleft()
                decoded_instruction["code"] = code
                explanation += ": modifying cache"
            elif command == "ADD":
                dest_reg = instruction.popleft()
                decoded_instruction["dest_reg"] = dest_reg
                source_reg_1 = instruction.popleft()
                decoded_instruction["source_reg_1"] = source_reg_1
                source_reg_2 = instruction.popleft()
                decoded_instruction["source_reg_2"] = source_reg_2
                explanation += ": adding numbers stored in registers, storing result in register"
            elif command == "ADDI":
                dest_reg = instruction.popleft()
                decoded_instruction["dest_reg"] = dest_reg
                source_reg_1 = instruction.popleft()
                decoded_instruction["source_reg_1"] = source_reg_1
                constant = instruction.popleft()
                decoded_instruction["constant"] = constant
                explanation += ": adding constant to number stored in register, storing result in register"
            else:
                explanation += ": instructions unclear"
                while instruction:
                    instruction.popleft()

        print("Decoding complete")
        print(explanation)
        print("Ready to pass instruction to ALU")
        
        self.clear_instruction_register()
        return decoded_instruction
        

        

    def pass_instruction_to_ALU(self):
        print("\nPassing instruction to ALU:", self.instruction_register)
        self.instruction_register = None # temporary solution for testing
        print("Clearing IR:", self.instruction_register)        

    def receive_result_from_ALU(self):
        pass

    def store_result(self):
        pass



