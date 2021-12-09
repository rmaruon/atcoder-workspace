#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

_ = readline()
S = input()

print(S.count("ABC"))
