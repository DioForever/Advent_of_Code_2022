input = open("input.txt","r").readlines()
cycle = 0
x = 1
signal_strength_sum = 0
cycles = [20,60,100,140,180,220]
for line in input:
    line = line.replace("\n","").split(" ")
    if line[0] == "noop":
        cycle += 1
        if cycles.__contains__(cycle):
            signal_strength_sum += x * cycle
    else:
        for i in range(2):
            cycle += 1
            if cycles.__contains__(cycle):
                signal_strength_sum += x * cycle
            if i == 1:
                if len(line) > 1:
                    x += int(line[1])
print(signal_strength_sum)