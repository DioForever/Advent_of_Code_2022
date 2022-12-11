input = open("input.txt","r").read().split("\n\n")
monkeys = []
inspects = [0]*len(input)
print(inspects)
for line in input:
    line = line.split("\n")
    monkey = []
    #inventory
    items = (line[1].split(": ")[1].split(", "))
    items = [int(x) for x in items]
    monkey.append(items)
    #operation
    monkey.append(eval(f"lambda old: {line[2].split('= ')[1]}"))
    #test case - division
    monkey.append(int(line[3].split("by ")[1]))
    #true target
    monkey.append(int(line[4].split("monkey ")[1]))
    #false target
    monkey.append(int(line[5].split("monkey ")[1]))
    monkeys.append(monkey)

rounds = 20
# for x rounds
for r in range(rounds):
    # for every monkey
    monkey_number = 0
    for monkey in monkeys:
        for item_level in monkey[0]:
            # for every item in monkey
            worry_level = int(monkey[1](item_level)/3)
            if worry_level % monkey[2] == 0:
                monkeys[monkey[3]][0].append(worry_level)
            else:
                monkeys[monkey[4]][0].append(worry_level)
            # add amount of inspects according to amount of items in inventory at the start
            inspects[monkey_number] += len((monkey[0]))
            # reset the inv, cuz we move all the items elsewhere
            monkey[0] = []
        monkey_number+=1
inspects.sort(reverse=True)
print(inspects)
print(f"Bussines level {inspects[0]*inspects[1]}")