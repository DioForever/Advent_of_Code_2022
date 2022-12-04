# Here I read the input
input = open("input.txt","r").readlines()
# I created variable for counting all the overlaping pairs
output = 0
# Here I looped through to check if there are pairs that overlap or contain each other
# and if it did, added 1 to the output
for group in input:
    first = group.split(",")[0]
    second = group.split(",")[1].replace("\n","")
    first_f = int(first.split("-")[0])
    first_s = int(first.split("-")[1])
    second_f = int(second.split("-")[0])
    second_s = int(second.split("-")[1])
    if (first_f <= second_f and first_s >= second_f) or (first_f >= second_f and first_s <=second_s) or (first_f <= second_f and first_s >=second_s) or (first_f>= second_f and first_f <= second_s) :
        output += 1