import re

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
        else:
            if not globals()[r](fields[r]):
                return False
    return True

def byr(value):
    return 1920 <= int(value) <= 2002

def iyr(value):
    return 2010 <= int(value) <= 2020

def eyr(value):
    return 2020 <= int(value) <= 2030

def hgt(value):
    if value.endswith("cm"):
        return 150 <= int(value[:-2]) <= 193
    if value.endswith("in"):
        return 59 <= int(value[:-2]) <= 76

def hcl(value):
    return re.match("^#[0-9a-f]{6}$", value) != None

def ecl(value):
    return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def pid(value):
    return re.match("^[0-9]{9}$", value) != None

def main():
    count = 0
    for passport in passports():
        if is_valid(passport):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
