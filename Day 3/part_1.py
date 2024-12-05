import re
input = open("./Day 3/input.txt", "r").read()

def find_muls(input):
    m = re.findall(r"mul\((\d+),(\d+)\)", input)
    return [(int(a), int(b)) for a, b in m]

muls = find_muls(input)

sums = list(map(lambda x: x[0] * x[1], muls))
result = sum(sums)
print(result)