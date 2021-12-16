def contains_three_vowels(string):
    vowels = 'aeiou'
    N = 0
    for char in string:
        if char in vowels:
            N += 1
        if N >= 3:
            return True
    return False

def contains_double_char(string):
    for char1, char2 in zip(string[:-1], string[1:]):
        if char1 == char2:
            return True
    return False

def contains_forbidden_strings(string, forbidden):
    if type(forbidden) is not list:
        raise TypeError("Forbidden strings must be in a list!")
    
    for substring in forbidden:
        if substring in string:
            if substring in string:
                return False
    
    return True


def part1_is_nice(string):
    if contains_double_char(string):
        if contains_three_vowels(string):
            forbidden_strings = ['ab', 'cd', 'pq', 'xy']
            if contains_forbidden_strings(string, forbidden_strings):
                return True
    return False


# test_string = 'haegwjzuvuyypxyu'
# print("Is {} nice? {}".format(test_string, is_nice(test_string)))
strings = []
with open("day5_input.txt", 'r') as f:
    for string in f:
        string = string.rstrip()
        strings.append(string)

N_nice = 0
for string in strings:
    if part1_is_nice(string):
        N_nice +=1

print("I found {} nice strings under the old rules".format(N_nice))

def contains_double_pair(string):
    for i, pair in enumerate(zip(string[:-1], string[1:])):
        pair = ''.join(pair)
        subtracted_string = string[:i] + string[i+2:]
        if pair in subtracted_string:
            return True
    return False

def contains_separated_pair(string):
    for char1, char2 in zip(string[:-2], string[2:]):
        if char1 == char2:
            return True
    return False

def part2_is_nice(string):
    print("\n\nTesting {}".format(string))
    if contains_separated_pair(string):
        print("Contains separated pair!")
        if contains_double_pair(string):
            print("Contains double substring!")
            return True

    return False

test_strings = [
    'aaa',
    'qjhvhtzxzqqjkmpb',
    'xxyxx',
    'uurcxstgmygtbstg',
    'ieodomkazucvgmuy',
]
test_answers = [False, True, True, False, False]

for test_string, answer in zip(test_strings, test_answers):
    print("Testing {}".format(test_string))
    print("Contains double pair? {}".format(contains_double_pair(test_string)))
    print("Contains separated pair? {}".format(contains_separated_pair(test_string)))
    print(part2_is_nice(test_string))
    print("Should be {}\n".format(answer))

input("> ")

N_nice = 0
for string in strings:
    if part2_is_nice(string):
        N_nice += 1

print("For part2, we have {} nice strings".format(N_nice))