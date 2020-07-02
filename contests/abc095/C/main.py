#!/usr/bin/env python3
A, B, C, X, Y = map(int, input().split())

patterns = [0] * 4
patterns[0] = A * X + B * Y
patterns[1] = C * max(X, Y) * 2
patterns[2] = C * Y * 2 + A * (X - Y) if X > Y else float('inf')
patterns[3] = C * X * 2 + B * (Y - X) if X < Y else float('inf')

print(min(patterns))
