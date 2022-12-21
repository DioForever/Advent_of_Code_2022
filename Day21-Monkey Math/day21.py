input = open("input.txt","r").readlines()
monkeys = {}
for monkey in input:
    monkey = monkey.split(" ")
    if len(monkey) <= 2:
        number = int(str(monkey[1]).replace("\n",""))
        name = monkey[0].replace(":","")
        #print(name, number)
        monkeys.setdefault(name, number)
    else:
        # its math operation
        print(monkey)
        name = monkey[0].replace(":","")
        operation = str(monkey[1:3]).replace("[","").replace("]","").replace("'","").replace(",","")+ " " + str(monkey[3]).replace("\n","")

        print(name,":", operation)
        monkeys.setdefault(name, operation)
print(monkeys)

def get_output(name):
    got = str(monkeys.get(name))
    if got.isnumeric():
        return int(got)
    else:
        first = got.split(" ")[0]
        second = got.split(" ")[2]
        func = got.split(" ")[1]
        f = get_output(first)
        s = get_output(second)
        match(func):
            case "+":
                num = f + s
            case "-":
                num = f - s
            case "/":
                num = f / s
            case "*":
                num = f * s
        print(num)
        return num

# lets go thourgh the input
output = 0
get_output("root")



