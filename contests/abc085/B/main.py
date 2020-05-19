#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
s = set()

for _ in range(N):
    d = int(readline())
    s.add(d)

print(len(s))
