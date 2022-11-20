class Cups():
    def __init__(self, labels):
        self.labels = list(int(c) for c in labels)

    def move(self):
        one, two, three = self.pickup()
        destination = self.destination(self.labels[0])
        #print(f"pick up: {one}, {two}, {three}\ndestination: {self.labels[destination]}\n")
        self.labels.insert(destination + 1, three)
        self.labels.insert(destination + 1, two)
        self.labels.insert(destination + 1, one)
        self.labels.append(self.labels.pop(0))

    def pickup(self):
        for i in range(3):
            yield self.labels.pop(1)

    def destination(self, label):
        while True:
            label = label - 1 if label - 1 >= min(self.labels) else max(self.labels)
            if label in self.labels:
                return self.labels.index(label)

    def __repr__(self):
        return " ".join(str(c) for c in self.labels)

def main():
    cups = Cups("496138527")
    for i in range(100):
        #print(cups)
        cups.move()
    print(cups)

if __name__ == "__main__":
    main()
