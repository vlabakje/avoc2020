import itertools
import os
import sys

def read_input():
    with open("input") as fileh:
        for line in fileh:
            yield int(line.strip())

def main():
    entries = list(read_input())
    for a, b in itertools.combinations(entries, 2):
        if a + b == 2020:
            print(a * b)

if __name__ == "__main__":
    main()
