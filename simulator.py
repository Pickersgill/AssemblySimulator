from assembler import Assembler
import sys
import numpy as np


class Simulator:
	
	def __init__(self, ass, slow=False):
		self.MEM_START = 0
		self.MEM_SIZE = 200
		self.PC = 0
		self.PROGRAMME_LEN = len(ass.lines)

		self.slow = slow

		self.var_table = {}
		
		self.func_map = dict(enumerate([self.set, 
			self.beq, self.add, self.sub, self.mul, self.div], start=1))
		self.assembled = ass

		self.init_memory()	

		print("BEGINNING RUN")

		self.run()

		print("RUN COMPLETE, MEMORY CONTENT:")
		print(self.memory)

	def run(self):
		while(self.PC < self.PROGRAMME_LEN):
			if self.slow:
				input()
			line = self.assembled.lines[self.PC]
			print("RUNNING LINE AT PC: %d" %  self.PC)
			print(line)
			args = line.args
			self.func_map[line.instruction_code](args)
		

	def get_var_mem_loc(self, var_name):
		if var_name in self.var_table.keys():
			return self.var_table[var_name]
		elif self.var_table.values():
			self.var_table[var_name] = max(self.var_table.values()) + 1
		else:
			self.var_table[var_name] = self.MEM_START

		return self.get_var_mem_loc(var_name)
		
	
	def init_memory(self):
		self.memory = np.zeros(self.MEM_SIZE, dtype=int)
	
	def set_mem(self, location, value):
		self.memory[int(location)] = value

	def mc(self, loc):
		return self.memory[self.get_var_mem_loc(loc)]

	def set(self, args):
		dst = self.get_var_mem_loc(args[0])
		k = args[1]
		self.set_mem(dst, k)
		self.PC += 1
		pass

	def beq(self, args):
		k = args[0]
		src1 = self.mc(args[1])
		src2 = self.mc(args[2])
		if src1 == src2:
			self.PC = int(k)
		else:
			self.PC += 1
		pass

	def add(self, args):
		dst = self.get_var_mem_loc(args[0])
		src1 = self.mc(args[1])
		src2 = self.mc(args[2])
		self.set_mem(dst, src1 + src2)
		self.PC += 1
		pass

	def sub(self, args):
		dst = self.get_var_mem_loc(args[0])
		src1 = self.mc(args[1])
		src2 = self.mc(args[2])
		self.set_mem(dst, src1 - src2)
		self.PC += 1
		pass

	def mul(self, args):
		dst = self.get_var_mem_loc(args[0])
		src1 = self.mc(args[1])
		src2 = self.mc(args[2])
		self.set_mem(dst, src1 * src2)
		self.PC += 1
		pass

	def div(self, args):
		dst = self.get_var_mem_loc(args[0])
		src1 = self.mc(args[1])
		src2 = self.mc(args[2])
		self.set_mem(dst, src1 // src2)
		self.PC += 1
		pass


if __name__ == "__main__":
	src = sys.argv[1]
	slow = False
	if len(sys.argv) > 2:
		slow = bool(sys.argv[2])
	ass = Assembler(src)
	sim = Simulator(ass, slow)


