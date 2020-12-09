import itertools

def read_ints():
    with open("input") as fileh:
        for line in fileh:
            yield int(line.strip())

def main():
    messages = list(read_ints())
    for i in range(25, len(messages)):
        if messages[i] not in (a + b for a, b in itertools.combinations(messages[i-25:i], 2)):
            print(messages[i])
            return

if __name__ == "__main__":
    main()
