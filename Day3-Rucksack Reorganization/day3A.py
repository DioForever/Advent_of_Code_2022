import string
point_awarding = list(string.ascii_lowercase) + list(string.ascii_uppercase)

points = 0

with open("input.txt","r") as read:
    for backpack in read:
        backpack = (backpack.replace("\n",""))
        f_compartment = backpack[:int(len(backpack)/2)]
        s_compartment = backpack[int(len(backpack)/2):]
        for item in s_compartment:
            if f_compartment.__contains__(item):
                points += point_awarding.index(item)+1
                break
print(points)