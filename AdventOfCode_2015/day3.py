current = [0,0]
visited = [current.copy()]

input = open('day3_input.txt', 'r').read()
# input = '^>v<'
print(len(input))

for instruction in input:
    if instruction == '^':
        current[0] += 1
    elif instruction == 'v':
        current[0] -= 1
    elif instruction == '>':
        current[1] += 1
    elif instruction == '<':
        current[1] -= 1
    
    visited.append(current.copy())


unique_houses = []
for house in visited:
    if house not in unique_houses:
        unique_houses.append(house)

print("Visited {} houses".format(len(unique_houses)))


print("----- PART 2 -----")

current = [[0,0], [0,0]]
visited = [current[0].copy()]

which_santa = 0
for instruction in input:
    if instruction == '^':
        current[which_santa][0] += 1
    elif instruction == 'v':
        current[which_santa][0] -= 1
    elif instruction == '>':
        current[which_santa][1] += 1
    elif instruction == '<':
        current[which_santa][1] -= 1
    
    visited.append(current[which_santa].copy())

    which_santa += 1
    which_santa = which_santa % 2

unique_houses = []
for house in visited:
    if house not in unique_houses:
        unique_houses.append(house)

print("Visited {} houses".format(len(unique_houses)))


