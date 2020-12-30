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
    point = 0, 0, 0
    for direction in directions:
        point = move(point, direction)
    return point

def move(point, direction):
    return point[0] + direction[0], point[1] + direction[1], point[2] + direction[2]

def neighbors(point):
    for direction in DELTA.values():
        yield move(point, direction)

def flips(blacks):
    whites = set()
    to_be_flipped = set()
    for black in blacks:
        black_neighbors = 0
        for neighbor in neighbors(black):
            if neighbor in blacks:
                black_neighbors += 1
            else:
                whites.add(neighbor)
        if black_neighbors == 0 or black_neighbors > 2:
            to_be_flipped.add(black)
    for white in whites:
        if sum(1 for neighbor in neighbors(white) if neighbor in blacks) == 2:
            to_be_flipped.add(white)
    return to_be_flipped

def main():
    seen = defaultdict(int)
    for directions in lines():
        position = walk(directions)
        seen[position] += 1
    blacks = set()
    for position, times in seen.items():
        if times % 2 == 1:
            blacks.add(position)
    print(len(blacks))
    for day in range(1, 101):
        blacks = blacks.symmetric_difference(flips(blacks))
        print(f"Day: {day}: {len(blacks)}")

if __name__ == "__main__":
    main()
