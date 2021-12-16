import numpy as np
from numpy.testing._private.utils import clear_and_catch_warnings

fname = 'input.txt'

card_size = 5

numbers = []
cards = []

with open(fname, 'r') as f:
    numbers = [int(x) for x in f.readline().split(',')]
    line = f.readline()
    while line:
        card = []
        for i in range(card_size):
            card.append([int(x) for x in f.readline().split()])
        cards.append(card)
        line = f.readline()
cards = np.array(cards)


# Start with an empty mask. Called numbers will have their positions flagged here.
# Win conditions will be checked against this array
mask = np.zeros_like(cards)

for i, number in enumerate(numbers):
    mask |= cards == number

    vertical_bingo = np.any(np.all(mask, axis=1))
    horizontal_bingo = np.any(np.all(mask, axis=2))

    if vertical_bingo:
        win_loc = np.where(np.all(mask, axis=1))
        break
    if horizontal_bingo:
        win_loc = np.where(np.all(mask, axis=2))
        break

winner = ((mask==False)*cards)[win_loc[0]]

print("Bingo! after {} numbers".format(i))
print("Last number was {}".format(number))
print("Board {} won".format(win_loc))
print("It looks like this:")
print(winner)

score = np.sum(winner*number)

print("It scores {}".format(score))




mask = np.zeros_like(cards)
i = -1
while True:
    i += 1
    number = numbers[i]

    bingo = False

    mask |= cards == number

    vertical_bingo = np.any(np.all(mask, axis=1))
    horizontal_bingo = np.any(np.all(mask, axis=2))

    if vertical_bingo:
        win_loc = np.where(np.all(mask, axis=1))[0]
        bingo = True
    if horizontal_bingo:
        win_loc = np.where(np.all(mask, axis=2))[0]
        bingo = True

    if bingo and cards.shape[0] > 1:
        mask = np.delete(mask, win_loc, axis=0)
        cards = np.delete(cards, win_loc, axis=0)
    elif bingo and cards.shape[0] == 1:
        print("Done!")
        break


winner = ((mask==False)*cards)[win_loc[0]]
score = np.sum(winner*number)

print("\n\nThe last number is {}".format(number))
print("Last winner is:\n{}".format(cards))
print(winner)
print("\nIt has a score of {}".format(score))