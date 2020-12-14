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

def apply_mask(mask, value):
    output = ""
    for m, v in zip(mask[::-1], bin(value)[2:].zfill(len(mask))[::-1]):
        if m == "X":
            output += v
        else: 
            output += m
    return int(output[::-1], 2)


def main():
    #print(apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 11))
    #print(apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 101))
    #print(apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 0))
    memory = {}
    for mask, assignments in mask_assignments():
        for location, value in assignments:
            memory[location] = apply_mask(mask, value)
    print(sum(memory.values()))


if __name__ == "__main__":
    main()
