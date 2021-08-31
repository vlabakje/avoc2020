import re
import sys

def rules_messages():
    with open("input") as fileh:
        rule_lines, messages = fileh.read().split("\n\n")
        rules = {}
        for rule_line in rule_lines.split("\n"):
            n, _, line = rule_line.partition(": ")
            rules[int(n)] = line
        rules[8] = ' | '.join([n * ' 42 ' for n in range(1, 10)])
        rules[11] = ' | '.join([n * ' 42 ' + n * ' 31 ' for n in range(1, 10)])
        return rules, (message for message in messages.split("\n") if message)

def build_regex(rules):
    rule = rules[0]
    while re.search(r'\d', rule):
        rule = ' '.join(['( '+ rules[int(c)] + ' )' if re.match(r'\d+', c) else c for c in rule.split()])
    return '^' + rule.replace('( "', '').replace('" )', '').replace(' ', '') + '$'

def main():
    rules, messages = rules_messages()
    regex = build_regex(rules)
    print(sum(1 for message in messages if re.match(regex, message) is not None))

if __name__ == "__main__":
    main()
    sys.exit()
