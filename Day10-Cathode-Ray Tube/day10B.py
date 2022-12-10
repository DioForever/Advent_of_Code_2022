input = open("input.txt","r").readlines()
cycle = 0
x = 0
signal_strength_sum = 0
rows = [[],[],[],[],[],[]]

def after_cycle():
    global x, cycle
    '''print(f"cycle {cycle, cycle/40,int(cycle/40) }")
    rows_index = int(cycle/40)
    print(f"rows index {rows_index}")
    if rows_index < 6:
        index_order = len(rows[rows_index])
        print(f"index order {index_order}")
        print(f"{index_order} - {x, x+1, x+2}")
        if index_order == x or index_order == x+1 or index_order == x+2:
            rows[rows_index].append("#")
        else:
            rows[rows_index].append(" ")'''
    if len(rows[0]) != 40:
        index_order = len(rows[0])
        print(f"index order {index_order}")
        print(f"{index_order} - {x, x + 1, x + 2}")
        if index_order == x or index_order == x + 1 or index_order == x + 2:
            rows[0].append("#")
        else:
            rows[0].append(" ")
    elif len(rows[1]) != 40:
        index_order = len(rows[1])
        print(f"index order {index_order}")
        print(f"{index_order} - {x, x + 1, x + 2}")
        if index_order == x or index_order == x + 1 or index_order == x + 2:
            rows[1].append("#")
        else:
            rows[1].append(" ")
    elif len(rows[2]) != 40:
        index_order = len(rows[2])
        print(f"index order {index_order}")
        print(f"{index_order} - {x, x + 1, x + 2}")
        if index_order == x or index_order == x + 1 or index_order == x + 2:
            rows[2].append("#")
        else:
            rows[2].append(" ")
    elif len(rows[3]) != 40:
        index_order = len(rows[3])
        print(f"index order {index_order}")
        print(f"{index_order} - {x, x + 1, x + 2}")
        if index_order == x or index_order == x + 1 or index_order == x + 2:
            rows[3].append("#")
        else:
            rows[3].append(" ")
    elif len(rows[4]) != 40:
        index_order = len(rows[4])
        print(f"index order {index_order}")
        print(f"{index_order} - {x, x + 1, x + 2}")
        if index_order == x or index_order == x + 1 or index_order == x + 2:
            rows[4].append("#")
        else:
            rows[4].append(" ")
    elif len(rows[5]) != 40:
        index_order = len(rows[5])
        print(f"index order {index_order}")
        print(f"{index_order} - {x, x + 1, x + 2}")
        if index_order == x or index_order == x + 1 or index_order == x + 2:
            rows[5].append("#")
        else:
            rows[5].append(" ")



def print_rows():
    for row in rows:
        print(row)


for line in input:
    line = line.replace("\n","").split(" ")
    if line[0] == "noop":
        cycle += 1
        after_cycle()
    else:
        for i in range(2):
            cycle += 1
            after_cycle()
            if i == 1:
                if len(line) > 1:
                    print(f"x {x} {line[1]}")
                    x += int(line[1])
                    print(f"x {x}")
    print_rows()
print(x)