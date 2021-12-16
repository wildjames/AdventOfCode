import numpy as np

input = 'input.txt'


key = {
    'forward': np.array([1, 0, 0]),
    'up': np.array([0, 0, -1]),
    'down': np.array([0, 0, 1]),
}

# [Horizontal position, depth, aim]
position = np.array([0, 0, 0])

instructions = []
with open(input, 'r') as f:
    for line in f:
        direction, distance = line.split(' ')

        distance = int(distance)
        instructions.append([direction, distance])

for instruction in instructions:
    direction, distance = instruction
    vector = key[direction] * distance

    # Handle aim modification to the vector
    if direction == 'forward':
        vector[1] += distance * position[2]

    position += vector

print(position)
print(position[0] * position[1])