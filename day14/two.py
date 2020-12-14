def mask_assignments():
    with open("input") as fileh:
        mask = ""
        assignments = []
        for line in fileh:
            if line.startswith("mask = "):
                if assignments:
                    yield mask, assignments
                    assignments = []
                _, _, mask = line.strip().partition(" = ")
            elif line.startswith("mem["):
                mem, _, value = line.strip().partition(" = ")
                assignments.append((int(mem[4:-1]), int(value)))
        if assignments:
            yield mask, assignments


def masks(prefix, mask, address):
    if not mask:
        yield prefix
    elif mask[0] == "X":
        yield from masks(prefix + "0", mask[1:], address[1:])
        yield from masks(prefix + "1", mask[1:], address[1:])
    elif mask[0] == "1":
        yield from masks(prefix + "1", mask[1:], address[1:])
    else:
        yield from masks(prefix + address[0], mask[1:], address[1:])

def main():
    memory = {}
    for mask, assignments in mask_assignments():
        for location, value in assignments:
            for m in masks("", mask[::-1], bin(location)[2:].zfill(len(mask))[::-1]):
                memory[int(m[::-1], 2)] = value
    print(sum(memory.values()))


if __name__ == "__main__":
    main()
