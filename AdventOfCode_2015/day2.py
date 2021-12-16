def calc_surface(l, w, h):
    A = 2*l*w + 2*w*h + 2*h*l
    
    largest = max([l,w,h])
    
    small_sides = [i for i in [l,w,h] if i != largest]
    # Handle the case where two or three sides are the same length, by appending small_sides with the longest value until it's long enough
    while len(small_sides) < 2:
        small_sides.append(largest)
    slack = small_sides[0] * small_sides[1]

    return A + slack

def calc_ribbon(l, w, h):
    largest = max([l,w,h])
    small_sides = [i for i in [l,w,h] if i != largest]
    while len(small_sides) < 2:
        small_sides.append(largest)
    ribbon = 2*sum(small_sides)
    bow = l*w*h

    return ribbon + bow


total_paper = 0
total_ribbon = 0
with open('day2_input.txt', 'r') as f:
    for line in f:
        l, w, h = [int(i) for i in line.split('x')]
        total_paper += calc_surface(l, w, h)
        total_ribbon += calc_ribbon(l, w, h)


print("The elves need a total of {} square feet of paper".format(total_paper))
print("The elves need a total of {} feet of ribbon".format(total_ribbon))