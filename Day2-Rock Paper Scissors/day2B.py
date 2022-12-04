# here I create 3 lists, in each is how many points would you recieve if u were to Win, Draw, lose
rock = [0+3, 3+1, 6+2]
paper = [0+1, 3+2, 6+3]
scissor = [0+2, 3+3, 6+1]

# Here is the list of all the possibilities
# and every time I select one row according to enemy hand
# and one item in the row according if I want to win(0), draw(1), lose(2)
l = [[rock[0],rock[1],rock[2]],
     [paper[0],paper[1],paper[2]],
     [scissor[0],scissor[1],scissor[2]]]
# Here we save all the acquired points
points_all = 0

# Read input and get 0,1,2 instead of A,B,C and X,Y,Z
# use the values to get the desired outcome and how many points we will be awarded for each line in input
with open("input.txt", "r") as read:
    for hand in read:
        # we get the number 65,66,67 for A,B,C, but we want 0,1,2, so we remove 65 from each one
        enemy = (ord(hand.split()[0])-65)
        # we get the number 88,89,90 for X,Y,Z, but we want 0,1,2, so we remove 65 from each one
        outcome = (ord(hand.split()[1])-88)
        # we use the enemy and outcome to get the desired outcome from the list
        outcome_points = l[enemy][outcome]
        # and we add the points to total points
        points_all += outcome_points
# printed the points
print(points_all)