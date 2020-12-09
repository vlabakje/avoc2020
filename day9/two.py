import itertools

def read_ints():
    with open("input") as fileh:
        for line in fileh:
            yield int(line.strip())

def one(messages):
    for i in range(25, len(messages)):
        if messages[i] not in (a + b for a, b in itertools.combinations(messages[i-25:i], 2)):
            return messages[i]

def contiguous(messages):
    for i in range(2, len(messages)-1):
        for j in range(i, len(messages)-i):
            yield messages[j:i+j]

def main():
    messages = list(read_ints())
    message = one(messages)
    for segment in contiguous(messages):
        if sum(segment) == message:
            print(min(segment) + max(segment))
            return

if __name__ == "__main__":
    main()
