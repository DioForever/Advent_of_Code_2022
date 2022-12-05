input = open("input.txt", "r")

map = []
size = 0

# Read file
for line in input:
    line = line.replace("    ","[ ]").replace("\n","").replace(" ","").split("]")
    if line != "":
        for n in range(len(line)-1):
            box = line[n]+"]"
            if len(map)!=9:
                # its new so add it as a list
                map.append([box])
            else:
                map[n].append(box)
    else:
        break
# Reverse it so its according to map
for l in map:
    l.reverse()
    for lists in map:
        for item in lists:
            if item == "[]":
                lists.remove(item)
    print(l)

print(map)
# do the instructions
with open("input.txt", "r") as read:
    for line in read:
        if line.__contains__("move"):
            line = line.replace("\n","")
            much = int(line.split(" ")[1])
            where = int(line.split(" ")[3])
            to = int(line.split(" ")[5])
            # now do the instructions
            #2 8 4
            what_move = []

            how = 0
            # get the boxes
            while len(what_move) != much:
                box = map[where-1][len(map[where-1])  -1 ]
                print(box)
                if box != "[]":
                    what_move.append(box)
                    # remove the boxes from last place
                    map[where-1].pop(len(map[where-1])  -1  )
                how += 1
            print(f"what_moves = {what_move}")
            # add the boxes to desired place
            for box in what_move:
                map[to-1].append(box)

for l in map:
    print(l)





