white = ["b", "d", "f", "h"]
black = ["a", "c", "e", "g"]

position = (input("Enter your position on the board: "))

if position[0] in white:
    if int(position[-1]) % 2 == 0:
        print ("Your square is black")
    else:
        print ("Your square is white")

if position[0] in black:
    if int(position[-1]) % 2 == 0:
        print ("Your square is white")
    else:
        print ("Your square is black")