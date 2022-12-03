# Here I am checkin all possibilities of point awarding so i can call it and get whatever I want
def whathand(enemy):
    if enemy == "A":
        win = 2+6
        draw = 1+3
        lose = 3
    elif enemy  == "B":
        win = 3+6
        draw = 2+3
        lose = 1
    else:
        win = 1 + 6
        draw = 3 + 3
        lose = 2
    return win, draw, lose

# Here I am checkin if I need to lose, win or draw
# and returning the points for the desired outcome
def outcome_calculate(your, enemy):
    if your == "X":
        #you need to lose
        points = int(whathand(enemy)[2])

    elif your == "Y":
        #you need to draw
        points = int(whathand(enemy)[1])
    else:
        # you need to win
        points = int(whathand(enemy)[0])
    return points

# created int for storing points
points_all = 0

# Read input and called function (outcome_calculation)
# and appointed points for each game and printed points_all
with open("input.txt", "r") as read:
    for hand in read:
        enemy = hand.split()[0]
        outcome = hand.split()[1]
        outcome_points = int(outcome_calculate(outcome, enemy))
        points_all += outcome_points
print(points_all)


