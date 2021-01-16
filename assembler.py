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
		self.VAR_MEM_START = 0
		self.lines = []
		self.var_table = {}
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

	def replace_vars(self, var_list):
		new_var_list = []
	
		for arg in var_list:
			if not arg.isnumeric():
				if arg not in self.var_table:
					mem_loc = self.get_next_av_mem()
					self.var_table[arg] = mem_loc
					new_var_list.append(mem_loc)
				else:
					new_var_list.append(self.var_table[arg])
			else:
				new_var_list.append(int(arg))

		return new_var_list

	def get_next_av_mem(self):
		if self.var_table.values():
			return max(self.var_table.values()) + 1
		else:
			return self.VAR_MEM_START

	def get_instr(self, instruction):
		return INSTR_MAP[instruction[0]]


if __name__ == "__main__":
	if len(sys.argv) > 1:
		src = sys.argv[1]
		Assembler(src)


