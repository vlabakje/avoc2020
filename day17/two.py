from collections import defaultdict
class Space():
    _active = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
    _bounds_x = 0, 0
    _bounds_y = 0, 0
    _bounds_z = 0, 0
    _bounds_w = 0, 0
    
    def all_points(self):
        for x in range(self._bounds_x[0]-1, self._bounds_x[1] + 3):
            for y in range(self._bounds_y[0]-1, self._bounds_y[1] + 3):
                for z in range(self._bounds_z[0]-1, self._bounds_z[1] + 3):
                    for w in range(self._bounds_w[0]-1, self._bounds_w[1] + 3):
                        yield x, y, z, w, self.is_active(x, y, z, w)

    def active_points(self):
        for x, columns in self._active.items():
            for y, stacks in self._active[x].items():
                for z, ws in self._active[x][y].items():
                    for w in ws:
                        yield x, y, z, w

    def count_active_points(self):
        return sum(1 for cell in self.active_points())

    def set_active(self, x, y, z, w):
        self._active[x][y][z].add(w)
        self._bounds_x = min(self._bounds_x[0], x), max(self._bounds_x[1], x)
        self._bounds_y = min(self._bounds_y[0], y), max(self._bounds_y[1], y)
        self._bounds_z = min(self._bounds_z[0], z), max(self._bounds_z[1], z)
        self._bounds_w = min(self._bounds_w[0], w), max(self._bounds_w[1], w)

    def set_inactive(self, x, y, z, w):
        if x in self._active and y in self._active[x] and z in self._active[x][y] and w in self._active[x][y][z]:
            self._active[x][y][z].remove(w)

    def is_active(self, x, y, z, w):
        return x in self._active and y in self._active[x] and z in self._active[x][y] and w in self._active[x][y][z]

    def print(self):
        for w in range(self._bounds_w[0], self._bounds_w[1] + 1):
            for z in range(self._bounds_z[0], self._bounds_z[1] + 1):
                print(f"z={z}, x={self._bounds_x} y={self._bounds_y}")
                for y in range(self._bounds_y[0], self._bounds_y[1] + 1):
                    print("".join("#" if self.is_active(x, y, z, w) else "." for x in range(self._bounds_x[0], self._bounds_x[1] + 1)))
                print("")


def neighbors(x, y, z, w):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if (dx, dy, dz, dw) != (0, 0, 0, 0):
                        yield x + dx, y + dy, z+dz, w + dw


def cycle(space):
    set_active = []
    set_inactive = []
    for x, y, z, w, active in space.all_points():
        active_neighbors = 0
        for nx, ny, nz, nw in neighbors(x, y, z, w):
            if space.is_active(nx, ny, nz, nw):
                active_neighbors += 1
        if active and active_neighbors not in (2, 3):
            set_inactive.append((x, y, z, w))
        if not active and active_neighbors == 3:
            set_active.append((x, y, z, w))
    for x, y, z, w in set_active:
        space.set_active(x, y, z, w)
    for x, y, z, w in set_inactive:
        space.set_inactive(x, y, z, w)

def example():
    space = Space()
    space.set_active(1, 0, 0, 0)
    space.set_active(2, 1, 0, 0)
    space.set_active(0, 2, 0, 0)
    space.set_active(1, 2, 0, 0)
    space.set_active(2, 2, 0, 0)
    for _ in range(6):
        cycle(space)
    print(space.count_active_points())

def main():
    space = Space()
    with open("input") as fileh:
        for y, line in enumerate(fileh):
            for x, field in enumerate(line.strip()):
                if field == "#":
                    space.set_active(x, y, 0, 0)
    for _ in range(6):
        cycle(space)
    print(space.count_active_points())

if __name__ == "__main__":
    main()
