characters = []
signal = open("day6_input.txt", 'r').readline()

for i in range(len(signal)):
    characters = signal[i:i+14]
    if len(set(characters)) == len(characters):
        print(i+14, "characters need to be processed before the first start-of-message marker is detected!")
        break
