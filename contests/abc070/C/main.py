#!/usr/bin/env python3
import math
from functools import reduce


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm, numbers)


N = int(input())
T = [int(input()) for _ in range(N)]
print(lcm_list(T))
