#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(read())

for i in range(1, 10):
    if N % i == 0 and N / i <= 9:
        print('Yes')
        break
else:
    print('No')
