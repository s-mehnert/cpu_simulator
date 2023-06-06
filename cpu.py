# The code in this file will simulate the FETCH -> DECODE -> EXECUTE -> STORE instruction cycle a Central Processing Unit (CPU) performs

from collections import deque
from arithmetic_logic_unit import ALU


class CPU:
    def __init__(self):
        self.program_counter = None
        self.instruction_register = None
        self.registers = {"R1" : 6, "R2" : 5, "R3" : None, "R4" : None, "R5" : None, "R6" : None, "R7" : None, "R8" : "ADDI,R5,R1,7"}
            
    def clear_instruction_register(self):
        self.instruction_register = None

    def reset_registers(self):
        for key, value in self.registers:
            self.registers[key] = None
    
    def fetch_instruction(self, instruction): # instructions will come in the form of a string
        print("\nFetching instruction:", instruction)
        if not instruction:
            print("No instruction to be fetched.")
            return
        instruction = instruction.strip().split(",")
        if not self.instruction_register:
            self.instruction_register = instruction
            print("Loading instruction into IR:", self.instruction_register)
            print("Ready for decoding.")
        else:
            print("Cannot fetch instruction as previous instruction is still waiting in line.")

    def decode_instruction(self, is_architecture):
        if not self.instruction_register:
            print("Instruction register empty. Aborting command.")
            return
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
                jump_to_reg = "R" + instruction.popleft()
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
                val_source_reg_1 = self.registers[decoded_instruction["source_reg_1"]]
                decoded_instruction["val_source_reg_1"] = val_source_reg_1
                source_reg_2 = instruction.popleft()
                decoded_instruction["source_reg_2"] = source_reg_2
                val_source_reg_2 = self.registers[decoded_instruction["source_reg_2"]]
                decoded_instruction["val_source_reg_2"] = val_source_reg_2
                explanation += ": adding numbers stored in registers, storing result in register"
            elif command == "ADDI":
                dest_reg = instruction.popleft()
                decoded_instruction["dest_reg"] = dest_reg
                source_reg_1 = instruction.popleft()
                decoded_instruction["source_reg_1"] = source_reg_1
                val_source_reg_1 = self.registers[decoded_instruction["source_reg_1"]]
                decoded_instruction["val_source_reg_1"] = val_source_reg_1
                constant = int(instruction.popleft())
                decoded_instruction["constant"] = constant
                explanation += ": adding constant to number stored in register, storing result in register"
            else:
                explanation += ": instructions unclear"
                while instruction:
                    instruction.popleft()

        print("Decoding complete")
        print("Decoded instruction:", decoded_instruction)
        print(explanation)
        self.clear_instruction_register()
        print("Clearing IR:", self.instruction_register) 
        print("Preparing for execution")
        self.execute_command(decoded_instruction, is_architecture)
        
    def execute_command(self, decoded_instruction, is_architecture):
        command = decoded_instruction["command"]
        if command == "J":
            self.fetch_instruction(self.registers[decoded_instruction["jump_to_reg"]])
            self.decode_instruction(is_architecture)
        elif command == "HALT":
            print("Terminating program now. Bye-bye.")
            return
        elif command == "CACHE":
            print("Cache command pending to be added later")
            return
        else:
            print("Preparing to pass instruction to ALU")
            self.pass_instruction_to_ALU_and_store_result(decoded_instruction)
    

    def pass_instruction_to_ALU_and_store_result(self, decoded_instruction):
        print("\nPassing instruction to ALU:", decoded_instruction)
        alu = ALU(decoded_instruction)
        alu.execute_instruction()
        result_of_operation = alu.result
        decoded_instruction["val_dest_reg"] = result_of_operation
        print(f"Storing result {result_of_operation} in destination register {decoded_instruction['dest_reg']}...")
        self.registers[decoded_instruction["dest_reg"]] = result_of_operation



