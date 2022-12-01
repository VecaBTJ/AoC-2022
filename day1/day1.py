elves = []
current_elf = 0

for line in open("day1_input.txt", 'r'):
    if line == '\n':
        elves.append(current_elf)
        current_elf = 0

    else:
        current_elf += int(line)

if current_elf != 0:
    elves.append(current_elf)

elves.sort(reverse=True)

print("The elf carrying the most calories carries", elves[1], "calories")
print("Top three elves are the elves with ", elves[1], ", ", elves[2], " and ", elves[3], " calories\n",
      "They are carrying in total of ", sum(elves[:3]), " calories", sep="")
