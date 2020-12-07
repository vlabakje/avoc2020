from dataclasses import dataclass

@dataclass
class Rule:
    color: str
    contains: dict

def rule_generator():
    with open("input") as fileh:
        for line in fileh:
            color, _, rules = line.partition(" bags contain ")
            assert rules.endswith(".\n")
            contains = {}
            for rule in rules[:-2].split(", "):
                if rule == "no other bags":
                    continue
                count, _, rule_color = rule.partition(" ")
                rule_color = rule_color.rsplit(" ", 1)[0]
                contains[rule_color] = int(count)
            yield Rule(color, contains)

def can_contain(rules, color):
    for rule in rules:
        if rule.color == color:
            continue
        if color in rule.contains.keys():
            yield rule.color
            yield from can_contain(rules, rule.color)

def main():
    rules = list(rule_generator())
    print(len(set(can_contain(rules, "shiny gold"))))

if __name__ == "__main__":
    main()
