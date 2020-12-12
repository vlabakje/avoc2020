class Point:
    def __init__(self, east, north):
        self.east = east
        self.north = north

def instructions():
    with open("input") as fileh:
        for line in fileh:
            yield line[0], int(line[1:].strip())

def move_ship(ship, waypoint, distance):
    ship.east += waypoint.east * distance
    ship.north += waypoint.north * distance

def move_waypoint(waypoint, direction, distance):
    if   direction == "N": waypoint.north += distance
    elif direction == "S": waypoint.north -= distance
    elif direction == "E": waypoint.east  += distance
    elif direction == "W": waypoint.east  -= distance

def rotate_waypoint(waypoint, direction, degrees):
    if (direction, degrees) in (("R", 90), ("L", 270)):
        waypoint.east, waypoint.north = waypoint.north, -1 * waypoint.east
    elif (direction, degrees) in (("L", 90), ("R", 270)):
        waypoint.east, waypoint.north = -1 * waypoint.north, waypoint.east
    elif degrees == 180:
        waypoint.east, waypoint.north = -1 * waypoint.east, -1 * waypoint.north

def main():
    ship = Point(0, 0)
    waypoint = Point(10, 1)
    for instruction, length in instructions():
        if instruction in "NSEW":
            move_waypoint(waypoint, instruction, length)
        elif instruction in "LR":
            rotate_waypoint(waypoint, instruction, length)
        elif instruction == "F":
            move_ship(ship, waypoint, length)
        else:
            raise Exception(f"uneeastpected instruction {instruction} length={length}")
    print(ship.east, ship.north, abs(ship.east)+abs(ship.north))

if __name__ == "__main__":
    main()
