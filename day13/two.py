def bus_lines():
    with open("input") as fileh:
        _, bus_lines = fileh.readlines()
        output = []
        for i, line in enumerate(bus_lines.split(",")):
            if line != "x":
                output.append((i, int(line)))
        return output

def main():
    n, t = 0, 1
    for i, bus in bus_lines():
        while (n + i) % bus:
            n += t
        t = t * bus
    print(n)

if __name__ == "__main__":
    main()
