import re
input = open("./Day 3/input.txt", "r").read()

def find_muls(input):
    m = re.findall(r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)", input)
    return m

muls = find_muls(input)
results = []

status = True
for item in muls:
    if item[0] == "do()":
        status = True
    elif item[0] == "don't()":
        status = False
    elif status and item[1] and item[2]:
        results.append(int(item[1]) * int(item[2]))

    
print(sum(results))