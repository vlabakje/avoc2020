REQUIRED = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

def passports():
    passport = ""
    with open("input") as fileh:
        for line in fileh:
            if line.strip() == "":
                yield passport
                passport = ""
            else:
                passport += line[:-1] + " "
    if passport != "":
        yield passport

def is_valid(passport):
    fields = {}
    for field in passport.split():
        k, v = field.split(":", 1)
        fields[k] = v
    for r in REQUIRED:
        if r not in fields:
            return False
    return True

def main():
    count = 0
    for passport in passports():
        if is_valid(passport):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
