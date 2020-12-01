import itertools
import os
import sys

def read_input():
    with open("input") as fileh:
        for line in fileh:
            yield int(line.strip())

def main():
    for a, b, c in itertools.combinations(read_input(), 3):
        if a + b + c== 2020:
            print(a * b * c)

if __name__ == "__main__":
    main()
