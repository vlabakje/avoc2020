OCCUPIED="#"
FREE="L"
EMPTY="."
NEIGHBOURS=[(-1, -1), ( 0, -1), ( 1, -1),
            (-1,  0),           ( 1,  0),
            (-1,  1), ( 0,  1), ( 1,  1)]

class Seat:
    def __init__(self):
        self.occupied = False
        self.neighbours = []

    def __str__(self):
        return OCCUPIED if self.occupied else FREE

    def switch(self):
        around = sum(1 if neighbour.occupied else 0 for neighbour in self.neighbours)
        if self.occupied and around >= 5:
            return True
        if not self.occupied and around == 0:
            return True
        return False

class Grid:
    def __init__(self, lines):
        self._grid = []
        for line in lines:
            row = []
            for c in line.strip():
                if c == EMPTY:
                    row.append(c)
                elif c == FREE:
                    row.append(Seat())
                else:
                    raise Exception(f"invalid {c}")
            self._grid.append(row)
        # populate neighbours
        for x, y, seat in self.seats():
            for dx, dy in NEIGHBOURS:
                self._find_neighbour(x, y, seat, dx, dy)
            

    def _find_neighbour(self, x, y, seat, dx, dy):
        for i in range(1, max(len(self._grid), len(self._grid[0]))):
            possible_x, possible_y = x + (dx*i), y + (dy*i)
            if (0 <= possible_x < len(self._grid[0])) and (0 <= possible_y < len(self._grid)):
                if type(self._grid[possible_y][possible_x]) == Seat:
                    seat.neighbours.append(self._grid[possible_y][possible_x])
                    return
            else:
                return  # ran off the grid
        raise Exception(f"unable to find neighbour from {x},{y} direction {dx},{dy}")

    def __str__(self):
        return "\n".join("".join(str(seat) for seat in row) for row in self._grid)

    def __repr__(self):
        return self.__str__()

    def seats(self):
        for y, line in enumerate(self._grid):
            for x, seat in enumerate(line):
                if type(seat) == Seat:
                    yield x, y, seat

    def why_dont_you_take_a_seat_over_here(self):
        moves = []
        for x, y, seat in self.seats():
            if seat.switch():
                moves.append((x, y, seat))
        for x, y, seat in moves:
            seat.occupied = not seat.occupied
        return len(moves)

def generate_grid():
    with open("input") as fileh:
        return Grid(fileh)

def main():
    grid = generate_grid()
    moves = 1
    while moves:
        moves = grid.why_dont_you_take_a_seat_over_here()
    print(sum(1 if seat.occupied else 0 for _, _, seat in grid.seats()))

if __name__ == "__main__":
    main()
