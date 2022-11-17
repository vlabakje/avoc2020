def p1_p2_stack(filename):
    p1, _, p2 = open(filename).read().partition("\n\n")
    return list(map(int, p1.split("\n")[1:])), list(map(int, p2.split("\n")[1:-1]))

ggame = 1
def play(p1, p2):
    global ggame
    game, r, p1_sets, p2_sets = ggame, 0, set(), set()
    ggame += 1
    while len(p1) != 0 and len(p2) != 0:
        r += 1
        if tuple(p1) in p1_sets or tuple(p2) in p2_sets:
            return True, None
        else:
            p1_sets.add(tuple(p1))
            p2_sets.add(tuple(p2))
        #print(f"{game=}{' '*game}{p1=} {p2=}", end ="")
        t1, t2 = p1.pop(0), p2.pop(0)
        if len(p1) >= t1 and len(p2) >= t2:
            #print(f" sub game! {r=}")
            one_wins, result = play(p1[:t1], p2[:t2])
        else:
            one_wins, result = t1 > t2, None
        if one_wins:
            #print(f" p1 wins {game=} {r=}")
            p1.append(t1)
            p1.append(t2)
        else:
            #print(f" p2 wins {game=} {r=}")
            p2.append(t2)
            p2.append(t1)
    if len(p1):
        return True, p1
    return False, p2


def winrar_score(filename):
    p1, p2 = p1_p2_stack(filename)
    _, result = play(p1, p2)
    score = sum((i+1)*x for i, x in enumerate(result[::-1]))
    print(result, score)
    return score

if __name__ == "__main__":
    assert winrar_score("example") == 291
    ggame = 1
    print(winrar_score("input"))
