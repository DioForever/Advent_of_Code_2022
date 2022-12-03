import string

# Here I created the list of point awarding according to index+1
point_awarding = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# I created 4 variables for storing all points (points)
# and three backpacks (backpack_f,s,t) cuz the groups of elfs are of 3 members
points = 0

# I read the input and created num which indicated which backpack in a group is that
# and according to the num I saved new backpack or if it was the third backpack checked for the badge item
input = open("input.txt","r").readlines()
for num in range(int(len(input)/3)):
    num = num*3
    backpack_f = input[num].replace("\n","")
    backpack_s = input[num+1].replace("\n","")
    backpack_t = input[num+2].replace("\n","")
    for item in backpack_f:
        if backpack_s.__contains__(item) and backpack_t.__contains__(item):
            points += point_awarding.index(item) + 1
            print(backpack_f, backpack_s, backpack_t, item,point_awarding.index(item)+1)
            break

# once I found all badges across all the groups and awarded points I printed out the total points
print(points)