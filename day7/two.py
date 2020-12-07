from one import rule_generator

def number_of_bags_contained(rules, color):
    output = 0
    for contain, count in rules[color].contains.items():
        output += count * (1 + number_of_bags_contained(rules, contain))
    return output

def main():
    rules = {rule.color:rule for rule in (rule_generator())}
    print(number_of_bags_contained(rules, "shiny gold"))

if __name__ == "__main__":
    main()
