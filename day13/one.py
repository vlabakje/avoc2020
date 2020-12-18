def current_time_bus_lines():
    with open("input") as fileh:
        current_time, bus_lines = fileh.readlines()
        return int(current_time), list(int(line) for line in bus_lines.split(",") if line != "x")


def main():
    current_time, bus_lines = current_time_bus_lines()
    for next_minute in range(current_time, current_time + 10):
        for line in bus_lines:
            if next_minute % line == 0:
                print(line * (next_minute - current_time))
                return

if __name__ == "__main__":
    main()
