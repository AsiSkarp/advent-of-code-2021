from numpy import loadtxt

# Part One

scans = loadtxt('scans.txt')
i = 0
count = 0


for line in scans:
    current = int(line)
    if current > i:
        count += 1
    i = current

count -= 1  # remove the first increment

print('Total number of increases: {}'.format(count))

# Part Two




def window(list, window_size):      # Implement sliding window funciton
    window_count = 0
    wd = 0
    for i in range(len(list) - window_size + 1):
        current_sum = sum(list[i:i + window_size])
        if current_sum > wd:
            window_count += 1
        wd = current_sum
    window_count -= 1  # remove the first increment
    return window_count


print('Total number of avg. increments: {}'.format(window(scans, 3)))
