game = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", "."
]
<<<<<<< HEAD

print(game[0] + game[1] + game[2])
print(game[3] + game[4] + game[5])
print(game[6] + game[7] + game[8])

next_position = input("Please type what position: ")

if next_position == "1":
    game[0] = "X"

if next_position == "2":
    game[1] = "X"

print(game[0] + game[1] + game[2])
print(game[3] + game[4] + game[5])
print(game[6] + game[7] + game[8])
=======
def gamePlan():
    print(game[0] + game[1] + game[2])
    print(game[3] + game[4] + game[5])
    print(game[6] + game[7] + game[8])

for i in range(1, 10):
    if i % 2 != 0:
        next_position = int(input("(Player one) Type what position: "))
        if game[next_position - 1] == "x":
            print("You typed wrong position")
            break

        elif game[next_position - 1] == "o":
            print("You typed wrong position")
            break

        else:
            game[next_position - 1] = "x"
            gamePlan()
        
    else:
        next_position = int(input("(Player two) Type what position: "))
        if game[next_position - 1] == "x":
            print("You typed wrong position")
            break
        
        elif game[next_position - 1] == "o":
            print("You typed wrong position")
            break

        else:
            game[next_position - 1] = "o"
            gamePlan()

    if game[0] == "x"and game[3] == "x" and game[6] == "x":
        print("Player one - winner")
        break
    elif game[1] == "x" and game[4] == "x" and game[7] == "x":
        print("Player one - winner")
        break
    elif game[2] == "x" and game[5] == "x" and game[8] == "x":
        print("Player one - winner")
        break
    elif game[0] == "x" and game[1] == "x" and game[2] == "x":
        print("Player one - winner")
        break
    elif game[3] == "x" and game[4] == "x" and game[5] == "x":
        print("Player one - winner")
        break
    elif game[6] == "x" and game[7] == "x" and game[8] == "x":
        print("Player one - winner")
        break
    elif game[0] == "x" and game[4] == "x" and game[8] == "x":
        print("Player one - winner")
        break
    elif game[3] == "x" and game[4] == "x" and game[6] == "x":
        print("Player one - winner")
        break

    if game[0] == "o" and game[3] == "o" and game[6] == "o":
        print("Player two - winner")
        break
    elif game[1] == "o" and game[4] == "o" and game[7] == "o":
        print("Player two - winner")
        break
    elif game[2] == "o" and game[5] == "o" and game[8] == "o":
        print("Player two - winner")
        break
    elif game[0] == "o" and game[1] == "o" and game[2] == "o":
        print("Player two - winner")
        break
    elif game[3] == "o" and game[4] == "o" and game[5] == "o":
        print("Player two - winner")
        break
    elif game[6] == "o" and game[7] == "o" and game[8] == "o":
        print("Player two - winner")
        break
    elif game[0] == "o" and game[4] == "o" and game[8] == "o":
        print("Player two - winner")
        break
    elif game[3] == "o" and game[4] == "o" and game[6] == "o":
        print("Player two - winner")
        break
>>>>>>> e2ca075a3974c10975a99da1777b4e4c5ed93db7
