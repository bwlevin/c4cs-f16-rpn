#!/usr/bin/env python3

def calculate(myarg1):
	stack = list()
	for token in myarg1.split():
		if token == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		else:
			stack.append(int(token))
		print(stack)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()
