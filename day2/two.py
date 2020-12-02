import os
import sys
from dataclasses import dataclass

@dataclass
class Password:
    a: int
    b: int
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
        if (password.password[password.a-1] == password.digit) ^ (password.password[password.b-1] == password.digit):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
