from functools import reduce

class Rule():
    def __init__(self, rule):
        self.name, _, conditions = rule.partition(": ")
        one, _, two = conditions.partition(" or ")
        self.one = tuple(map(int, one.split("-", 1)))
        self.two = tuple(map(int, two.split("-", 1)))

    def match(self, value):
        return (self.one[0] <= value <= self.one[1]) or (self.two[0] <= value <= self.two[1])

def rules_mine_others():
    rules, mine, others = segments()
    return [Rule(rule) for rule in rules], mine[0], others

def segments():
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

def valid(rules, ticket):
    for value in ticket.split(","):
        if not any(rule.match(int(value)) for rule in rules):
            return False
    return True

def all_values_for_field(fieldnum, tickets):
    for ticket in tickets:
        yield int(list(ticket.split(","))[fieldnum])

def match_field_against_rules(rules, fieldnum, tickets):
    for rule in rules:
        if all(rule.match(value) for value in all_values_for_field(fieldnum, tickets)):
            yield rule

def field_rule_generator(fieldcount, rules, valids):
    for fieldnum in range(fieldcount):
        yield fieldnum, set(match_field_against_rules(rules, fieldnum, valids))

def departure_values(field_rules, mine):
    seen = set()
    for fieldnum, rules in sorted(field_rules.items(), key=lambda x: len(x[1])):
        rules -= seen
        assert len(rules) == 1, f"{fieldnum} {rules}"
        rule = rules.pop()
        seen.add(rule)
        if rule.name.startswith("departure"):
            yield int(mine.split(",")[fieldnum])

def main():
    rules, mine, others = rules_mine_others()
    valids = [ticket for ticket in others if valid(rules, ticket)]
    field_rules = dict(field_rule_generator(len(mine.split(",")), rules, valids))
    print(reduce(lambda a,b: a*b, departure_values(field_rules, mine)))

if __name__ == "__main__":
    main()
