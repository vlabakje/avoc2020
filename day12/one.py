def instructions():
    with open("input") as fileh:
        for line in fileh:
            yield line[0], int(line[1:].strip())

def main():
    east, north = 0, 0
    degrees = 90
    for instruction, length in instructions():
        if instruction == "N":
            north += length
        elif instruction == "S":
            north -= length
        elif instruction == "E":
            east += length
        elif instruction == "W":
            east -= length
        elif instruction == "F":
            if degrees == 0:
                north += length
            elif degrees == 90:
                east += length
            elif degrees == 180:
                north -= length
            elif degrees == 270:
                east -= length
            else:
                raise Exception(f"unable to parse {degrees} degrees")
        elif instruction == "R":
            degrees += length
        elif instruction == "L":
            degrees -= length
        else:
            raise Exception(f"uneeastpected instruction {instruction} length={length}")
        degrees = degrees % 360  
    print(east, north, abs(east)+abs(north))

if __name__ == "__main__":
    main()
