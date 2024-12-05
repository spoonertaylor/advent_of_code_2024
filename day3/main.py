import re
from functools import reduce

def read_input():
    with open("input_file.txt") as f:
        return f.read()

def mul_sum(instructions):
    matches = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", instructions)
    prod_sum = 0
    for m in matches:
        nums = re.findall(r"\d+", m)
        prod_sum += reduce(lambda a,b: a*b, map(int, nums))
    return prod_sum

def mul_sum_dos_donts(instructions):
    matches = re.findall(r"(don\'t\(\)|do\(\)|mul\(\d{1,3}\,\d{1,3}\))", instructions)
    prod_sum = 0
    mult = True
    for m in matches:
        if m == "don't()":
            mult = False
            continue
        elif m == "do()":
            mult = True
            continue
        else:
            if mult:
                nums = re.findall(r"\d+", m)
                prod_sum += reduce(lambda a,b: a*b, map(int, nums))
            else:
                continue
    return prod_sum

if __name__ == "__main__":
    instructions = read_input()
    print(f"First multiplication: {mul_sum(instructions)}")
    print(f"With do's and donts: {mul_sum_dos_donts(instructions)}")
