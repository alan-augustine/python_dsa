# Ambiguos question

import os

def print_buffer(data):
   for i in range(len(data)):
       print(data[i], end=' ')

def perform_operation(a, b, op):
       if op == '+':
           result = a + b
       elif op == '-':
           result = a - b
       elif op == '*':
           result = a * b
       elif op == '/':
           result = a / b
       return result

def calculate_result(data):
    result = float(data[0])
    operation = data[1]
    for i in range(2, len(data)):
        if data[i] in '+-*/':
            operation = data[i]
        else:
            result = perform_operation(result, float(data[i]), operation)
    return result


def calculator():
   buffer = []
   i = 0
   while True:
       d = input(':')
       if d != '=':
           buffer.append(d)
           i += 1
           print_buffer(buffer)
       else:
           print(calculate_result(buffer))
           break

calculator()