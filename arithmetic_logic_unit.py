# The code in this file will simulate the arithmetic and logic operations an arithmetic and logic unit (ALU) performs

class ALU:
    def __init__(self, instruction):
        self.instruction = instruction
        self.result = None
    
    def execute_instruction(self):
        if self.instruction["command"] == "ADD":
            print(f"Adding {self.instruction['val_source_reg_1']} to {self.instruction['val_source_reg_2']}...")
            self.result = self.instruction["val_source_reg_1"] + self.instruction["val_source_reg_2"]
            print("Result:", self.result)
            
        elif self.instruction["command"] == "ADDI":
            print(f"Adding {self.instruction['val_source_reg_1']} to {self.instruction['constant']}...")
            self.result = self.instruction["val_source_reg_1"] + self.instruction["constant"]
            print("Result:", self.result)
        else:
            print("Unknown command:", self.instruction["command"], "--> Operation aborted.")
    
        