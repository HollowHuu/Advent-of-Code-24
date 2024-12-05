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

similarity = 0

for i in list1:
    if i in list2:
        count = list2.count(i)
        similarity += count * i


print(similarity)
    

