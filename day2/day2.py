rounds = []

for line in open("day2_input.txt", 'r'):
    if line[0] == 'A':
        if line[2] == 'X':
            rounds.append(3)
        elif line[2] == 'Y':
            rounds.append(4)
        elif line[2] == 'Z':
            rounds.append(8)

    elif line[0] == 'B':
        if line[2] == 'X':
            rounds.append(1)
        elif line[2] == 'Y':
            rounds.append(5)
        elif line[2] == 'Z':
            rounds.append(9)

    if line[0] == 'C':
        if line[2] == 'X':
            rounds.append(2)
        elif line[2] == 'Y':
            rounds.append(6)
        elif line[2] == 'Z':
            rounds.append(7)

print("If everything goes exactly according to my stragegy, my total score would be", sum(rounds), "points")
