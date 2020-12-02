import os
import sys
from dataclasses import dataclass

@dataclass
class Password:
    min: int
    max: int
    digit: str
    password: str

def policy_password():
    with open("input") as fileh:
        for line in fileh:
            policy, password = line.split(": ", 1)
            counts, digit = policy.split(" ", 1)
            a, b = map(int, counts.split("-", 1))
            yield Password(a, b, digit, password)

def main():
    count = 0
    for password in policy_password():
        digit_count = len([True for c in password.password if c == password.digit])
        if password.min <= digit_count <= password.max:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
