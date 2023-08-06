#!/bin/python3

import re

sin = {0: 0, 30: 1/2, 45: 0.70, 60: 0.86, 90: 1}

def sine(degree):
    return sin[degree]

def cos(degree):
    degree = int(degree)
    if degree > 45:
        return sin[90 - degree]
    elif degree < 45:
        if degree == 30:
            return sin[60]
        elif degree == 0:
            return sin[90]
        else:
            return sin[45]

def tan(degree):
    d = sine(degree) / cos(degree)
    return "{:.2f}".format(d)

def cot(degree):
    return 1 / float(tan(degree))

def sec(degree):
    return 1 / cos(degree)

def csec(degree):
    return "{:.2f}".format(1 / sine(int(degree)))

S = input("> ")
S = re.split(r'([*+-/()])', S)
S = [s for s in S if s != '']

print(S)

storing = None
for i in range(len(S)):
    if S[i].isdigit():
        storing = int(S[i])
    else:
        if S[i][:4] == "csec":
            degree = S[i][4:]
            if degree.isdigit():
                S[i] = csec(degree)
            else:
                S[i] = S[i]
        else:
            degree = S[i][3:]
            if S[i][:3] == "sin":
                if degree.isdigit():
                    S[i] = sine(int(degree))
                else:
                    S[i] = S[i]
            elif S[i][:3] == "cos":
                if degree.isdigit():
                    S[i] = cos(int(degree))
                else:
                    S[i] = S[i]
            elif S[i][:3] == "tan":
                if degree.isdigit():
                    S[i] = tan(int(degree))
                else:
                    S[i] = S[i]
            elif S[i][:3] == "cot":
                if degree.isdigit():
                    S[i] = cot(int(degree))
                else:
                    S[i] = S[i]
            else:
                if degree.isdigit():
                    S[i] = sec(int(degree))
                else:
                    S[i] = S[i]


def calculate_expression(arr):
    stack = []
    operators = {'+', '-', '*', '/'}

    for item in arr:
        if isinstance(item, (int, float)):
            stack.append(item)
        elif item in operators:
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()

                if item == '+':
                    result = num1 + num2
                elif item == '-':
                    result = num1 - num2
                elif item == '*':
                    result = num1 * num2
                elif item == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        raise ValueError("Division by zero is not allowed.")
                
                stack.append(result)
            else:
                raise ValueError("Invalid expression format.")

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid expression format.")

# Example usage:
result = calculate_expression(S)
print(result)


