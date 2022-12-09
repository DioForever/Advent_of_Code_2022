input = open("input.txt","r").readlines()
head_loc = [0,0]
tail_loc = [0,0]
visited = [[0,0]]
hll = [0,0]



def tail_check(hll, head_loc, tail_loc_):
    global tail_loc
    if (abs(head_loc[0]-tail_loc_[0])) > 1 or abs(head_loc[1]-tail_loc_[1]) > 1:
        # tail is too far away from head
        tail_loc = hll
        if not visited.__contains__(tail_loc):
            visited.append(tail_loc)

for order in input:
    side = order.split(" ")[0]
    size = int(order.split(" ")[1])
    match side:
        case "R":
            for i in range(size):
                hll = list(head_loc)
                head_loc[0] = head_loc[0] +1
                tail_check(hll, head_loc, tail_loc)
        case "L":
            for i in range(size):
                hll = list(head_loc)
                head_loc[0] = head_loc[0] -1
                tail_check(hll, head_loc, tail_loc)
        case "U":
            for i in range(size):
                hll = list(head_loc)
                head_loc[1] = head_loc[1] +1
                tail_check(hll, head_loc, tail_loc)
        case "D":
            for i in range(size):
                hll = list(head_loc)
                head_loc[1] = head_loc[1] - 1
                tail_check(hll, head_loc, tail_loc)

print(len(visited))