#!/usr/bin/env python3
import sys
from typing import List

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: "List[str]"):
    if ".#" in S and "#." in S:
        print(NO)
    else:
        print(YES)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = [next(tokens) for _ in range(2)]  # type: "List[str]"
    solve(S)


if __name__ == "__main__":
    main()
