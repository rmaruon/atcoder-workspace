#!/usr/bin/env python3
from decimal import Decimal
import math

A, B = input().split()

answer = math.floor(Decimal(A) * Decimal(B))
print(answer)
