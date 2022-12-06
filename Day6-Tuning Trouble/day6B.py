input = open("input.txt", "r").read()
last = []

output = ""
count = 0
for char in input:
    last.append(char)
    count += 1
    if len(last) >= 14:
        if len(set(last)) == 14:
            output = str(last)
            break
        last.pop(0)
print(count)
print(output)