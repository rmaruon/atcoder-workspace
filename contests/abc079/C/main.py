#!/usr/bin/env python3
from itertools import product

s = input()
op_patterns = product(['+', '-'], repeat=3)

for operators in op_patterns:
    expression = f"{s[0]}{operators[0]}{s[1]}{operators[1]}{s[2]}{operators[2]}{s[3]}"
    if eval(expression) == 7:
        print(f"{expression}=7")
        break
