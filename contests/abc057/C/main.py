#!/usr/bin/env python3
import math
N = int(input())

square_root = math.floor(math.sqrt(N))

for a in range(square_root, 0, -1):
    if N % a == 0:
        b = int(N / a)
        print(len(str(b)))
        exit()
