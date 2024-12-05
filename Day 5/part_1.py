import math

input = [line.upper() for line in open("./Day 5/input.txt", "r").read().split("\n")]

# split rules and page numbers by the one blank line
rules = []
pageList = []

total = 0

for line in input:
    if line == "":
        break
    rules.append(line)

for line in input[len(rules) + 1:]:
    pageList.append(line)

for pages in pageList:
    pages = list(map(int, pages.split(",")))
            

    for rule in rules:
        # Split the rule into two parts and convert to int
        rule = rule.split("|")
        first = int(rule[0])
        second = int(rule[1])

        
        # Find all rules that match the pages
        if first in pages and second in pages:
            # Check if first is before second
            if pages.index(first) < pages.index(second):
                print(f"{first} is before {second}")
                total += math.floor(len(pages) / 2)

        else:
            continue

print(total)