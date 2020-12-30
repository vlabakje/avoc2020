from collections import defaultdict

DELTA = { 
        "e":  (1, -1, 0),
        "se": (0, -1, 1),
        "sw": (-1, 0, 1),
        "w":  (-1, 1, 0),
        "nw": (0, 1, -1),
        "ne": (1, 0, -1)
        }

def lines():
    with open("input") as fileh:
        for line in fileh:
            yield parse_line(line.strip())

def parse_line(line):
    output = []
    while len(line):
        if line[0] in DELTA:
            output.append(DELTA[line[0]])
            line = line[1:]
        else:
            output.append(DELTA[line[:2]])
            line = line[2:]
    return output

def walk(directions):
    x, y, z = 0, 0, 0
    for direction in directions:
        x, y, z = x + direction[0], y + direction[1], z + direction[2]
    return (x, y, z)

def main():
    seen = defaultdict(int)
    for directions in lines():
        position = walk(directions)
        seen[position] += 1
    black = 0
    for position, times in seen.items():
        if times % 2 == 1:
            black += 1
    print(black)

if __name__ == "__main__":
    main()
