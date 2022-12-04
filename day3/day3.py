priorities = []
content = open("day3_input.txt", 'r')

for first in content:
    second = content.readline()
    third = content.readline()

    for i in range(len(first)):
        if first[i] in second and first[i] in third:
            if 'a' <= first[i] <= 'z':
                priorities.append(ord(first[i]) - 96)
            elif 'A' <= first[i] <= 'Z':
                priorities.append(ord(first[i]) - 38)
            break
print("The sum of the priorities of those item types is ", sum(priorities))
