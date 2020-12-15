from collections import deque, defaultdict
def speak(seq):
    turns = defaultdict(lambda: deque(maxlen=2))
    for turn, s in enumerate(seq):
        turns[s].appendleft(turn)
    # first speak one of each of the seq
    yield from seq
    last = seq[-1]
    for turn in range(len(seq), 2020):
        if last not in turns or len(turns[last]) == 1:
            last = 0
        else:
            last = turns[last][0] - turns[last][1]
        yield last
        turns[last].appendleft(turn)
            

def main():
    for turn, number in enumerate(speak((2,15,0,9,1,20))):
        print(f"Turn {turn+1} {number}")

if __name__ == "__main__":
    main()
