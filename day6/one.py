def groups():
    group = ""
    with open("input") as fileh:
        for line in fileh:
            if line.strip() == "":
                yield group
                group = ""
            else:
                group += line
        if group != "":
            yield group

def answers(group):
    output = set()
    for c in group:
        if c == "\n":
            continue
        output.add(c)
    return output

def answercount(group):
    return len(answers(group))

def main():
    print(sum([answercount(group) for group in groups()]))

if __name__ == "__main__":
    main()
