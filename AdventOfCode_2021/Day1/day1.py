import numpy as np


input_fname = 'input.txt'


sweep = []
with open(input_fname, 'r') as f:
    for line in f:
        sweep.append(int(line))

## PART 1
n_increase = 0
for m, pm in zip(sweep[1:], sweep[:-1]):
    if m > pm:
        n_increase += 1

print(n_increase)


## PART 2

N_av = 3
smoothed = []
for i in range(N_av-1, len(sweep)):
    val = 0
    for j in range(N_av):
        val += sweep[i-j]
    
    smoothed.append(val)

n_increase = 0
for m, pm in zip(smoothed[1:], smoothed[:-1]):
    if m > pm:
        n_increase += 1

print(n_increase)
