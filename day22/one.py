def p1_p2_stack(filename):
    p1, _, p2 = open(filename).read().partition("\n\n")
    return list(map(int, p1.split("\n")[1:])), list(map(int, p2.split("\n")[1:-1]))


def play(p1, p2):
    while len(p1) != 0 and len(p2) != 0:
        t1, t2 = p1.pop(0), p2.pop(0)
        if t1 > t2:
            p1.append(t1)
            p1.append(t2)
        else:
            p2.append(t2)
            p2.append(t1)
        #print(f"{p1=} {p2=}")
    if len(p1):
        return p1
    return p2


def winrar_score(filename):
    p1, p2 = p1_p2_stack(filename)
    result = play(p1, p2)
    score = sum((i+1)*x for i, x in enumerate(result[::-1]))
    #print(result, score)
    return score

if __name__ == "__main__":
    assert winrar_score("example") == 306
    print(winrar_score("input"))
