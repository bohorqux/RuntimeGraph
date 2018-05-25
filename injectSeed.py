#!/usr/bin/python3
from random import *

def injectRandList(bytecode, size):
	rand_list = [randint(1, 1000000) for i in range(size)]
	bytecode = bytecode.replace('"TARGET"', str(rand_list))
	return bytecode