#input all numbers
input = []
with open("input.txt", "r") as read:
#turns string into array of string into array
    for line in read:
        input.append(line.replace("\n",""))
#makes array for all elves an var containing last sumed up numbers
food = []
last = 0
#for every number in input:
for item in input:
    #if space is not blank add number to LAST
    if item != '':
        last += int(item)
    #if space is blank add LAST to FOOD and set it up to zero
    else:
        food.append(last)
        last = 0;
#sort list FOOD in ascending order
food.sort()
#print everythnig in FOOD, Max second and third max numbers and theyer sum
print(food)
print(f"First - {food[-1]}")
print(f"First - {food[-2]}")
print(f"First - {food[-3]}")
print(f"Total Top 3 - {food[-1]+food[-2]+food[-3]}")