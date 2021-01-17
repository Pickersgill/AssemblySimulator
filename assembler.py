import sys
import re

src = None

INSTR_MAP = {v : k for k, v in (enumerate(["set", "beq", "add", "sub", "mul", "div"], start=1))}

class Instruction:
	def __init__(self, line_arr):
		self.instruction_code = None
		self.args = None
		self.decompose(line_arr)

	def decompose(self, words):
		self.instruction_code = words[0]
		self.args = words[1:]

	def __str__(self):
		return "%d " % self.instruction_code + ", ".join(str(a) for a in self.args)


class Assembler:
	
	def __init__(self, file_src):
		self.lines = []
		content = open(file_src)
		
		for line in content:
			if len(line) > 1 and line[0] != "%":
				self.lines.append(self.make_instruction(line.split()))

		print("FOLLOWING PROGRAM CONSTRUCTED")
	
		for i, line in enumerate(self.lines, start=1):
			print("LINE %d: " % i + str(line))
		

	def make_instruction(self, line):
		instruction = self.get_instr(line)
		args = line[1:]
		return Instruction([instruction] + args)


	def get_instr(self, instruction):
		return INSTR_MAP[instruction[0]]


if __name__ == "__main__":
	if len(sys.argv) > 1:
		src = sys.argv[1]
		Assembler(src)


