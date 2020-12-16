class Rule():
    def __init__(self, rule):
        self.name, _, conditions = rule.partition(": ")
        one, _, two = conditions.partition(" or ")
        self.one = tuple(map(int, one.split("-", 1)))
        self.two = tuple(map(int, two.split("-", 1)))

    def match(self, value):
        return (self.one[0] <= value <= self.one[1]) or (self.two[0] <= value <= self.two[1])

def rules_mine_others():
    with open("input") as fileh:
        segment = []
        for line in fileh:
            if line.strip() == "":
                yield segment
                segment = []
            elif line.strip() in ("your ticket:", "nearby tickets:"):
                continue
            else:
                segment.append(line.strip())
        yield segment

def invalid_values(rules, ticket):
    for value in ticket.split(","):
        if not any(rule.match(int(value)) for rule in rules):
            yield int(value)

def main():
    rules, mine, others = rules_mine_others()
    rule_list = [Rule(rule) for rule in rules]
    print(sum(sum(invalid_values(rule_list, ticket)) for ticket in others))

if __name__ == "__main__":
    main()
