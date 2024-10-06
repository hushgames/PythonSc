from os import system, sys, path

class Memory:
    def __init__(self, size: int):
        self.memory = ['0000'] * size
        self.size = size
        self.accumulator = 0
        self.instruction_counter = 0

    def getitem(self, address: int) -> str:
        return self.memory[address]

    def setitem(self, address: int, value: str) -> None:
        self.memory[address] = value

    def execute(self):
        while True:
            instruction = int(self.memory[self.instruction_counter])
            operation_code = instruction // 100
            operand = instruction % 100
            
            print(f"Executing instruction at address {self.instruction_counter}: {instruction}")
            
            if operation_code == 10:  # Read
                self.accumulator = int(input("Enter a value: "))
                self.setitem(operand, f"{self.accumulator:04}")
            elif operation_code == 11:  # Write
                print(f"Output: {self.getitem(operand)}")
            elif operation_code == 20:  # LoadM
                self.accumulator = int(self.getitem(operand))
            elif operation_code == 21:  # Store
                self.setitem(operand, f"{self.accumulator:04}")
            elif operation_code == 22:  # LoadI
                self.accumulator = operand
            elif operation_code == 30:  # AddM
                self.accumulator += int(self.getitem(operand))
            elif operation_code == 31:  # SubM
                self.accumulator -= int(self.getitem(operand))
            elif operation_code == 32:  # DivM
                self.accumulator //= int(self.getitem(operand))
            elif operation_code == 33:  # ModM
                self.accumulator %= int(self.getitem(operand))
            elif operation_code == 34:  # MulM
                self.accumulator *= int(self.getitem(operand))
            elif operation_code == 35:  # AddI
                self.accumulator += operand
            elif operation_code == 36:  # SubI
                self.accumulator -= operand
            elif operation_code == 37:  # DivI
                self.accumulator //= operand
            elif operation_code == 38:  # ModI
                self.accumulator %= operand
            elif operation_code == 39:  # MulI
                self.accumulator *= operand
            elif operation_code == 40:  # JMP
                self.instruction_counter = operand
                continue
            elif operation_code == 41:  # JN
                if self.accumulator < 0:
                    self.instruction_counter = operand
                    continue
            elif operation_code == 42:  # JZ
                if self.accumulator == 0:
                    self.instruction_counter = operand
                    continue
            elif operation_code == 43:  # HALT
                print("Operation: HALT. Program halted.")
                break
            
            self.instruction_counter += 1
            
            # Display registers and memory
            self.display_registers()

    def display_registers(self):
        print("\nREGISTERS:")
        print(f"accumulator:\t\t+{self.accumulator:04}")
        print(f"programCounter:\t\t{self.instruction_counter:02}")
        print(f"instructionRegister:\t+{self.memory[self.instruction_counter]:04}")
        print(f"operationCode:\t\t{int(self.memory[self.instruction_counter]) // 100:02}")
        print(f"operand:\t\t{int(self.memory[self.instruction_counter]) % 100:02}")
        
        print("\nMEMORY:")
        print("\t", end="")
        for i in range(10):
            print(f"{i:02}\t", end="")
        print()
        for i in range(0, 100, 10):
            print(f"{i:02}\t", end="")
            for j in range(10):
                if i + j < self.size:
                    print(f"+{self.memory[i + j]:04}", end="\t")
            print()
        print('-' * 100)

def dump(mem: list) -> None:
    print("DUMP:")
    for i in range(0, len(mem), 10):
        print(f"{i:02d} ", end="")
        for j in range(10):
            if i + j < len(mem):
                print(f"+{mem[i + j]:04}", end="\t")
        print()
    print('-' * 100)

def loader(filename: str) -> list:
    program = []
    if path.exists(filename):
        with open(filename) as file:
            program = file.readlines()
    return program

def main() -> None:
    system('cls')
    m = Memory(100)
    filename = str(sys.argv[1])  # Command line argument for program file
    program = loader(filename)
    
    for item in program:
        instruction = item.strip().split("\t")
        address = int(instruction[0])
        command = instruction[1]
        m.setitem(address, command)
        
    dump(m.memory)
    m.execute()

if __name__ == "__main__":
    main()
