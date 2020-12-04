import os
import sys

def read_map():
    output = []
    with open("input") as fileh:
        for line in fileh:
            output.append(list(line.strip()))
    return output

def path():
    map_ = read_map()
    path = []
    for y in range(0, 100000):
        if y == len(map_):
            return path
        path.append(map_[y][(3 * y) % len(map_[0])])

def main():
    count = 0
    for c in path():
        if c == "#":
            count += 1
    print(count)

if __name__ == "__main__":
    main()
