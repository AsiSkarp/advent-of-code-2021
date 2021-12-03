with open('input.txt') as f:
    lines = f.readlines()

# Part One


def measure_position(lines):
    horizontal = 0
    depth = 0
    for line in lines:
        if "forward" in line:
            print(line)
            horizontal += int(line[line.index(" ") + 1:])
        elif "up" in line:
            print(line)
            depth -= int(line[line.index(" ") + 1:])
        elif "down" in line:
            print(line)
            depth += int(line[line.index(" ") + 1:])
        print("Current horizontal: {} \t Current depth: {}".format(horizontal, depth))
    return horizontal * depth


#print('Product of distance travelled: {}'.format(measure_position(lines)))

# Part Two

def postion_by_aim(lines):
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        if "forward" in line:
            print(line)
            horizontal += int(line[line.index(" ") + 1:])
            depth += aim * int(line[line.index(" ") + 1:])
        elif "up" in line:
            print(line)
            aim -= int(line[line.index(" ") + 1:])
        elif "down" in line:
            print(line)
            aim += int(line[line.index(" ") + 1:])
        print("Current horizontal: {} \t Current depth: {} \t Current aim: {}".format(horizontal, depth, aim))
    return horizontal * depth


print('Product of distance travelled with aim: {}'.format(postion_by_aim(lines)))

