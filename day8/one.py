def instruction_generator():
    with open("input") as fileh:
        for line in fileh:
            instruction, parameter = line.strip().split()
            yield instruction, int(parameter)

def main():
    acc = 0
    pc = 0
    seen = set()
    instructions = list(instruction_generator())
    while pc not in seen:
        seen.add(pc)
        instruction, parameter = instructions[pc]
        if instruction == "acc":
            acc += parameter
            pc += 1
        elif instruction == "jmp":
            pc += parameter
        elif instruction == "nop":
            pc += 1
        else:
            raise NotImplementedError(f"unsupported instruction {instruction} pc={pc}")
    print(acc)

if __name__ == "__main__":
    main()
