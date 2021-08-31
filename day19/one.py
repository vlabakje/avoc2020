def rules_messages():
    with open("input") as fileh:
        rule_lines, messages = fileh.read().split("\n\n")
        rules = {}
        for rule_line in rule_lines.split("\n"):
            n, _, line = rule_line.partition(": ")
            rules[int(n)] = line
        return rules, (message for message in messages.split("\n") if message)

def applies(message, rules, rule, matched):
    if not message:
        return False, 0
    if "\"" in rules[rule]:
        return message[0] == rules[rule][1], matched + 1
    else: # refers to other rules
        anymatches = False
        for alternative in rules[rule].split(" | "):
            allgood = True
            total = matched
            for i, rulenum in enumerate(alternative.split(" ")):
                result, count = applies(message[total:], rules, int(rulenum), matched)
                if not result:
                    allgood = False
                    break
                total += count
            if allgood:
                anymatches = True
                break
        return anymatches, total

def okay(message, rules):
    return applies(message, rules, 0, 0) == (True, len(message))

def main():
    rules, messages = rules_messages()
    print(sum(1 for message in messages if okay(message, rules)))

if __name__ == "__main__":
    main()
