#!/usr/bin/env python3
import sys


def solve(M: "List[int]", D: "List[int]"):
    return


# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = [int()] * (2)  # type: "List[int]"
    D = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        M[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(M, D)

if __name__ == '__main__':
    main()
