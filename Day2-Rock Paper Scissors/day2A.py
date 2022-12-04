# X, A = Rock
# Y, B = Paper
# Z, Y = Scissors


# Here I am checkin how many points will I get for using X, Y, Z hand and returnin the points
def points(your):
    match your:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3

# Here I am checkin if I won, lost or it is a draw
# and I return points 6 - win, 3 - draw, 0 - lose
def outcome(your, enemy):
    match [your,enemy]:
        case ["X","A"]:
            return 3
        case ["Y","B"]:
            return 3
        case ["Z","C"]:
            return 3
        case ["X","C"]:
            return 6
        case ["Y","A"]:
            return 6
        case ["Z","B"]:
            return 6
        case _:
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
print(points_all)