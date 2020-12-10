def generate_adapters():
    with open("input") as fileh:
        for line in fileh:
            yield int(line)

def main():
    adapters = sorted(generate_adapters())
    # add the builtin device and charging port
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)
    ones, threes = 0, 0
    for i in range(len(adapters)-1):
        diff = adapters[i+1] - adapters[i]
        assert 0 < diff <= 3, f"adapter issue {diff}"
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
    print(ones, threes, ones * threes)

if __name__ == "__main__":
    main()
