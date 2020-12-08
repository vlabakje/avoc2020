class LoopException(Exception):
    pass


def instruction_generator():
    with open("input") as fileh:
        for line in fileh:
            instruction, parameter = line.strip().split()
            yield instruction, int(parameter)

def loop(instructions):
    acc = 0
    pc = 0
    seen = set()
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
        if pc >= len(instructions):
            return acc
    raise LoopException("loop detected")

def main():
    instructions = list(instruction_generator())
    for i in range(len(instructions)):
        if instructions[i][0] not in ("jmp", "nop"):
            continue
        new_instructions = instructions[:]
        new_instructions[i] = ("jmp" if instructions[i][0] == "nop" else "nop", instructions[i][1])
        try:
            print(loop(new_instructions))
        except LoopException:
            pass

if __name__ == "__main__":
    main()
