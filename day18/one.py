def tokenize(expression):
    number = ""
    for c in expression:
        if c in "0123456789":
            number += c
            continue
        if number:
            yield int(number)
            number = ""
        if c == "+":
            yield lambda a, b: a + b
        elif c == "*":
            yield lambda a, b: a * b
        elif c in "()":
            yield c
    if number:
        yield int(number)

def result(expression):
    if len(expression) == 1:
        return expression[0]
    elif len(expression) == 3:
        return expression[1](expression[0], expression[2]) 
    return result([result(expression[0:3])] + expression[3:])

def rindex(haystack, needle):
    return len(haystack) - next(i for i, v in enumerate(reversed(haystack), 1) if v == needle)

def expression(tokens):
    if "(" not in tokens:
        return result(tokens)
    hclose = tokens.index(")")
    hopen = rindex(tokens[:hclose], "(")
    return expression(tokens[:hopen] + [result(tokens[hopen + 1:hclose])] + tokens[hclose + 1:])

def test():
    assert expression(list(tokenize("1 + 2 * 3 + 4 * 5 + 6"))) == 71, "failed"
    assert expression(list(tokenize("2 * 3 + (4 * 5)"))) == 26
    assert expression(list(tokenize("5 + (8 * 3 + 9 + 3 * 4 * 3)"))) == 437
    assert expression(list(tokenize("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))) == 12240
    assert expression(list(tokenize("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))) == 13632

def main():
    with open("input") as fileh:
        total = 0
        for line in fileh:
            total += expression(list(tokenize(line.strip())))
        print(total)

if __name__ == "__main__":
    main()
