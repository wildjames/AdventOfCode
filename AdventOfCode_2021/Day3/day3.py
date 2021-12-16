import numpy as np

fname = 'input.txt'
Nbits = 12

diagnostics = []
with open(fname, 'r') as f:
    for line in f:
        diagnostics.append(int(line, 2))
diagnostics = np.array(diagnostics)


gamma = 0
epsilon = 0
for i in range(Nbits):
    mask = 1<<i
    masked = np.bitwise_and(diagnostics, mask)
    
    gamma_bit = np.sum(masked != 0) > np.sum(masked == 0)
    epsilon_bit = np.sum(masked != 0) < np.sum(masked == 0)
    
    gamma_val = (1<<i) * gamma_bit
    gamma += gamma_val

    epsilon_val = (1<<i) * epsilon_bit
    epsilon += epsilon_val

print(epsilon)
print(gamma)
print(gamma * epsilon)
print()


## PART 2

genny = 0
genny_diagnostics = np.copy(diagnostics)
for i in range(Nbits):
    print("Diagnostics left: {}".format(len(genny_diagnostics)))
    mask = (2**(Nbits-1)) >> i
    masked = np.bitwise_and(genny_diagnostics, mask) != 0

    print("N1: {}\nN0: {}".format(np.sum(masked != 0), np.sum(masked == 0)))

    # I want to get the MOST common digit
    most_common = int(np.sum(masked != 0) > np.sum(masked == 0))
    # For the genny, if there are equal 0 and 1, I prefer the 1
    if int(np.sum(masked != 0) == np.sum(masked == 0)):
        most_common = 1

    if most_common:
        # I want numbers with a one at `mask`
        desired = np.where(masked != 0)
    else:
        # I want numbers with a zero at `mask`
        desired = np.where(masked == 0)

    genny_diagnostics = genny_diagnostics[desired]

    if len(genny_diagnostics) == 1:
        genny = genny_diagnostics[0]
        break

print("\nDone Oxygen generator!")
print(bin(genny))
print("\n------------------------\n\n")


scrubber = 0
scrubber_diagnostics = np.copy(diagnostics)
for i in range(Nbits):
    print("Diagnostics left: {}".format(len(scrubber_diagnostics)))
    mask = (2**(Nbits-1)) >> i
    masked = np.bitwise_and(scrubber_diagnostics, mask) != 0

    print("N1: {}\nN0: {}".format(np.sum(masked != 0), np.sum(masked == 0)))

    # I want to get the MOST common digit
    least_common = int(np.sum(masked != 0) < np.sum(masked == 0))
    print("I want to keep those with {} at this index".format(least_common))
    # For the scrubber, if there are equal 0 and 1, I prefer the 1
    if int(np.sum(masked != 0) == np.sum(masked == 0)):
        least_common = 0

    if least_common:
        # I want numbers with a one at `mask`
        desired = np.where(masked != 0)
    else:
        # I want numbers with a zero at `mask`
        desired = np.where(masked == 0)

    scrubber_diagnostics = scrubber_diagnostics[desired]

    if len(scrubber_diagnostics) == 1:
        scrubber = scrubber_diagnostics[0]
        break

print("\nDone Oxygen scrubber!")
print(bin(scrubber))

print()
print(genny * scrubber)