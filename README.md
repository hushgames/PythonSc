# PythonSc
**Simpletron Shit**

**Operation Code Meaning**

**Input/Output Operations**

Read 	= 10		- Read a word from the keyboard into a specific location in memory

Write     = 11		- Write a word from a specific location in memory to the screen

**Load/Store Operations**

LoadM 	 = 20		- Load a word from a specific location in memory into the accumulator

Store	 = 21		- Store a word from the accumulator into a specific location in memory

LoadI     = 22		- Load an immediate value (00-99) into the accumulator.  The 2 digit operand becomes the immediate value to be loaded in the accumulator.

**Arithmetic Operations**

**operand comes from memory**

AddM 	= 30		- Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)

SubM   = 31		- Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)

DivM    = 32		- Divide the accumulator by the word from a specific location in memory (leave the result in the accumulator)

ModM  = 33		- Perform the modulo operation between the word in the memory location and the contents of the accumulator (leave the remainder in   the accumulator)

MulM    =34		- Multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)

**operand is immediate**

AddI   = 35		- Add the immediate operand represented by the next 2 digits to the word in the accumulator (leave the result in the accumulator)

SubI   = 36		- Subtract the immediate operand represented by the next 2 digits from the  word in the accumulator (leave the result in the accumulator)

DivI    = 37		- Divide the accumulator by the immediate operand represented by the next 2 digits (leave the result in the accumulator)

ModI  = 38		- Perform the modulo operation on the accumulator and the immediate operand represented by the next 2 digits(leave the result in the accumulator)

MulI    =39		- Multiply the immediate operand represented by the next 2 digits to the word in the accumulator (leave the result in the accumulator)

**Transfer of Control Operations**

JMP   = 40		- Jump to a specific location in memory

JN     = 41		- Jump to a specific location in memory if the accumulator is negative

JZ     = 42		- Jump to a specific location in memory if the accumulator is 0		

HALT = 43		- Halt - this program has completed its task

