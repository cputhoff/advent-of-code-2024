import re

def extract_mul_from_input(input):
    mul_list =[]
    with open(input, 'r') as f:
        content = f.read()
        mul_list = re.findall(r"mul\(\d+,\d+\)", content)
    return mul_list

def execute_mul(mul_string):
    numbers = re.findall(r"\d+", mul_string)
    return int(numbers[0]) * int(numbers[1])

def sum_execute_mul(mul_list):
    mul_sum = 0
    for element in mul_list:
        mul_sum += execute_mul(element)
    return mul_sum

input = "input.txt"
mul_list = extract_mul_from_input(input)
print(sum_execute_mul(mul_list))