# X, A = Rock
# Y, B = Paper
# Z, Y = Scissors

# Here I am checkin how many points will I get for using X, Y, Z hand and returnin the points
def points(your):
    if your == "X":
        return 1
    elif your == "Y":
        return 2
    elif your == "Z":
        return 3

# Here I am checkin if I won, lost or it is a draw
# and I return points 6 - win, 3 - draw, 0 - lose
def outcome(your, enemy):
    if str(your) == "X" and str(enemy) == "A":
        return 3
    elif str(your) == "Y" and str(enemy) == "B":
        return 3
    elif str(your) == "Z" and str(enemy) == "C":
        return 3
    elif your == "X" and enemy=="C":
        return 6
    elif your == "Y" and enemy=="A":
        return 6
    elif your == "Z" and enemy=="B":
        return 6
    else:
        return 0

#I  created int points_all which stores all counted points
points_all = 0
# Here I am reading the input and calling the functions above (points, outcome) and adding it to the points_all
with open("input.txt", "r") as read:
    for hands in read:
        your = hands.split()[1]
        enemy = hands.split()[0]
        point_hand = points(your)
        point_outcome = outcome(your,enemy)
        points_all += point_hand + point_outcome
print(f"all = {points_all}")