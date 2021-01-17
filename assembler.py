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
		self.MEM_START = 0
		self.MEM_SIZE = 200

		self.var_table = {}

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
		args = self.assemble_args(line[1:])
		return Instruction([instruction] + args)


	def assemble_args(self, arg_list):
		for i, arg in enumerate(arg_list):
			if not arg.isnumeric():
				arg_list[i] = self.get_var_mem_loc(arg_list[i])
			else:
				arg_list[i] = arg

		return arg_list

	def get_var_mem_loc(self, var_name):
		if var_name in self.var_table.keys():
			return self.var_table[var_name]
		elif self.var_table.values():
			self.var_table[var_name] = max(self.var_table.values()) + 1
		else:
			self.var_table[var_name] = self.MEM_START

		return self.get_var_mem_loc(var_name)
	

	def get_instr(self, instruction):
		return INSTR_MAP[instruction[0]]


if __name__ == "__main__":
	if len(sys.argv) > 1:
		src = sys.argv[1]
		Assembler(src)


