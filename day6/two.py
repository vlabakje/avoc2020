def groups():
    group = []
    with open("input") as fileh:
        for line in fileh:
            if line.strip() == "":
                yield group
                group = []
            else:
                group.append(line.strip())
        if group:
            yield group

def answers(lines):
    output = set([c for c in lines[0]])
    for line in lines[1:]:
        output = output.intersection(set([c for c in line]))
    return output

def answercount(group):
    return len(answers(group))

def main():
    print(sum([answercount(group) for group in groups()]))

if __name__ == "__main__":
    main()
