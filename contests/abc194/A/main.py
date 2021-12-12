#!/usr/bin/env python3

A, B = [int(x) for x in input().split()]

無脂乳固形分 = A
乳脂肪分 = B
乳固形分 = 無脂乳固形分 + 乳脂肪分

if 乳固形分 >= 15 and 乳脂肪分 >= 8:
    print(1)
elif 乳固形分 >= 10 and 乳脂肪分 >= 3:
    print(2)
elif 乳固形分 >= 3:
    print(3)
else:
    print(4)
