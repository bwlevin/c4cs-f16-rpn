#!/usr/bin/env python3

import types
import operator
import readline
import sys
from termcolor import cprint

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod
}

def color_print(current_stack):
	for item in current_stack:
		if type(item) is int:
			if item < 0:
				cprint(item, 'red', attrs=['bold'])
			elif item == 0:
				cprint(item, 'yellow', attrs=['bold'])
			else:
				cprint(item, 'green')
		else:
			cprint(item, 'blue')

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			cprint(token, 'blue', 'on_white')
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		color_print(stack)
		print("\n")
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print("Result: ", result)

if __name__ == '__main__':
	main()
