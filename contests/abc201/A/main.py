#!/usr/bin/env python3
import sys
from typing import List

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: "List[int]"):
    A.sort()

    if A[0] - A[1] == A[1] - A[2]:
        print(YES)
    else:
        print(NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    solve(A)


if __name__ == "__main__":
    main()
