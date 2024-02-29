
def split(input):
    test = input
    act = 1
    part1 = ""
    part2 = ""
    for char in test:
        if char == " " and act == 1:
            act = 2
        elif act == 2:
            part2 += char
        elif act == 1:
            part1 += char
    print(part1)
    print(part2)

split("take two")



