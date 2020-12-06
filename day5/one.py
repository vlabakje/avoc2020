def encoded():
    with open("input") as fileh:
        for line in fileh:
            yield line.strip()

def decode(seat):
    row = sum(n if c == "B" else 0 for c, n in zip(seat[:7], (64, 32, 16, 8, 4, 2, 1)))
    column = sum(n if c == "R" else 0 for c, n in zip(seat[7:], (4, 2, 1)))
    return row, column

def seat_id(row, column):
    return (row * 8) + column

def seat_ids():
    for seat in encoded():
        row, column = decode(seat)
        yield seat_id(row, column)

def all_seats():
    for row in range(128):
        for column in range(8):
            yield seat_id(row, column)

def main():
    print(max(seat_ids()))

if __name__ == "__main__":
    main()
