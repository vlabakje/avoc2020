class Cup():
    def __init__(self, label):
        self.label = label
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.label)

class DLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.labelindex = {}
        self.current = None

    def add_end(self, label):
        new_cup = Cup(label)
        new_cup.prev = self.tail
        self.labelindex[label] = new_cup
        if self.head == None:
            self.head = new_cup
            self.tail = new_cup
            self.current = new_cup
        else:
            self.tail.next = new_cup
            self.tail = new_cup

    def values(self):
        cur = self.head
        while cur != None:
            out = str(cur.label)
            if cur == self.current:
                out = f"({out})"
            if cur == self.head:
                out = f"_{out}"
            if cur == self.tail:
                out = f"{out}_"
            yield out
            cur = cur.next

    def advance(self):
        if self.current == self.tail:
            self.current = self.head
        elif self.current.next:
            self.current = self.current.next

    def __str__(self):
        return " ".join(self.values())

    def pop(self, right_from):
        out = self.labelindex[right_from].next
        if out is None:
            out = self.head
            self.head = out.next
        if out == self.tail:
            self.tail = out.prev
        p, n = out.prev, out.next
        if p:
            p.next = n
        if n:
            n.prev = p
        return out

    def insert(self, right_from, cup):
        x = self.labelindex[right_from]
        n = x.next
        x.next = cup
        cup.prev = x
        cup.next = n
        if n:
            n.prev = cup
        if x == self.tail:
            self.tail = cup
        
    def move(self):
        v = self.current.label
        one, two, three = self.pop(v), self.pop(v), self.pop(v)
        dest = self.destination(set([one.label, two.label, three.label]))
        #print("pick up: ", one, two, three)
        #print("destination: ", dest)
        self.insert(dest, three)
        self.insert(dest, two)
        self.insert(dest, one)
        self.advance()
        
    def destination(self, excl):
        label = self.current.label
        while True:
            label = label - 1 if label - 1 > 0 else 1_000_000
            if label not in excl:
                return label

def ten():
    d = DLL()
    for i in "389125467":
        d.add_end(int(i))
    for i in range(10):
        print(f"move {i+1}")
        print(d)
        d.move()
        print("==")

def part_two_test():
    d = DLL()
    for i in "496138527":
        d.add_end(int(i))
    for i in range(10, 1_000_001):
        d.add_end(i)
    for i in range(10_000_000):
        if i % 100_000 == 0:
            print(f"{i/100_000}%")
        d.move()
    print(d.labelindex[1].next.label, d.labelindex[1].next.next.label)

part_two_test()
