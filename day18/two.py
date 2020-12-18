def tokenize(expression):
    for c in expression:
        if c in "0123456789":
            yield int(c)
        if c in "+*()":
            yield c

def result(expression):
    if len(expression) == 1:
        return expression[0]
    if "+" in expression:
        plus = expression.index("+")
        return result(expression[:plus-1] + [expression[plus-1] + expression[plus+1]] + expression[plus+2:])
    return result([expression[0] * expression[2]] + expression[3:])

def rindex(haystack, needle):
    return len(haystack) - next(i for i, v in enumerate(reversed(haystack), 1) if v == needle)

def expression(tokens):
    if "(" not in tokens:
        return result(tokens)
    hclose = tokens.index(")")
    hopen = rindex(tokens[:hclose], "(")
    return expression(tokens[:hopen] + [result(tokens[hopen + 1:hclose])] + tokens[hclose + 1:])

def test():
    assert expression(list(tokenize("1 + 2 * 3 + 4 * 5 + 6"))) == 231
    assert expression(list(tokenize("2 * 3 + (4 * 5)"))) == 46
    assert expression(list(tokenize("5 + (8 * 3 + 9 + 3 * 4 * 3)"))) == 1445
    assert expression(list(tokenize("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))) == 669060
    assert expression(list(tokenize("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))) == 23340

def main():
    with open("input") as fileh:
        total = 0
        for line in fileh:
            total += expression(list(tokenize(line.strip())))
        print(total)

if __name__ == "__main__":
    main()
