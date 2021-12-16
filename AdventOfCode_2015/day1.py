with open('day1_input.txt', 'r') as f:
    data = f.read()

floor = 0
for i, d in enumerate(data):
    if d == '(':
        floor += 1
    if d == ')':
        floor -= 1
    
    if floor == -1:
        print("Reached the basement in position {}".format(i+1))
        exit()

print("At the end of the instructions, the floor is {}".format(floor))