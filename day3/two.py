def read_map():
    output = []
    with open("input") as fileh:
        for line in fileh:
            output.append(list(line.strip()))
    return output

def path(x, y):
    map_ = read_map()
    for z in range(0, 100000):
        y_ = z*y
        if y_ >= len(map_):
            break
        yield map_[y_][(x * z) % len(map_[0])]

def trees(x, y):
    count = 0
    for c in path(x, y):
        if c == "#":
            count += 1
    return count

def main():
    a = trees(1, 1)
    b = trees(3, 1)
    c = trees(5, 1)
    d = trees(7, 1)
    e = trees(1, 2)
    print(a * b * c * d * e)

if __name__ == "__main__":
    main()
