#!/usr/bin/env python3
from collections import Counter
import itertools
import copy
from itertools import product


def count_black(array):
    flatten = itertools.chain.from_iterable(array)
    c = Counter(flatten)
    return c["#"]


def red_row(array, i):
    length = len(array[0])
    array[i] = ["r"] * length
    return array


def red_col(array, j):
    for row in array:
        row[j] = "r"
    return array


H, W, K = map(int, input().split())
C = []

for _ in range(H):
    row = list(input())
    C.append(row)

total = 0

row_select_patterns = product([True, False], repeat=H)
col_select_patterns = list(product([True, False], repeat=W))

for row_select_pattern in row_select_patterns:
    for col_select_pattern in col_select_patterns:
        c = copy.deepcopy(C)

        for i, i_flag in enumerate(row_select_pattern):
            for j, j_flag in enumerate(col_select_pattern):
                if i_flag:
                    c = red_row(c, i)

                if j_flag:
                    c = red_col(c, j)

        if count_black(c) == K:
            total += 1

print(total)
