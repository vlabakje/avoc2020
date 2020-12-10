def generate_adapters():
    with open("input") as fileh:
        for line in fileh:
            yield int(line)

CACHE={}

def possible_paths(adapters, start):
    if start in CACHE:
        return CACHE[start]
    if start == len(adapters) - 2:
        return 1
    if len(adapters) - 3 > start and adapters[start+3] - 3 == adapters[start]:
        CACHE[start] = possible_paths(adapters, start+1) + possible_paths(adapters, start+2) + possible_paths(adapters, start+3)
    elif adapters[start+2] - 2 == adapters[start]:
        CACHE[start] = possible_paths(adapters, start+1) + possible_paths(adapters, start+2)
    else:
        CACHE[start] = possible_paths(adapters, start + 1)
    return CACHE[start]

def main():
    adapters = sorted(generate_adapters())
    # add the builtin device and charging port
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)
    print(possible_paths(adapters, 0))

if __name__ == "__main__":
    main()
