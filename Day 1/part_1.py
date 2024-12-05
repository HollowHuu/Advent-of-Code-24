data = open("./Day 1/input.txt", "r").read().split("\n")

list1 = []
list2 = []

for i in data:
    if i == "":
        continue
    num1 = int(i.split("   ")[0])
    num2 = int(i.split("   ")[1])

    list1.append(num1)
    list2.append(num2)

list1.sort()
list2.sort()

total = 0

for i in range(len(list1)):
    if list1[i] > list2[i]:
        total += list1[i] - list2[i]
    else:
        total += list2[i] - list1[i]

print(total)
