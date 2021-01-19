# https://stackoverflow.com/questions/20831773/how-to-accept-input-without-the-need-to-press-enter-python-3
# https://code.activestate.com/recipes/134892/
# Ambiguos question - different calculators work in different ways
# was unable to get expected output
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


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
   getch = _Getch()
   buffer = []
   i = 0
   while True:
       d = getch()
       print(d)
       if d != '=':
           buffer.append(d)
           i += 1
           #print_buffer(buffer)
       else:
           print(calculate_result(buffer))
           break

calculator()
