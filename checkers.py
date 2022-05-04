field1 = [
    [" - ", " B ", " - ", " B ", " - ", " B ", " - ", " B ", " 8 "], #0
    [" B ", " - ", " B ", " - ", " B ", " - ", " B ", " - ", " 7 "], #1
    [" - ", " B ", " - ", " B ", " - ", " B ", " - ", " B ", " 6 "], #2
    [" + ", " - ", " + ", " - ", " + ", " - ", " + ", " - ", " 5 "], #3
    [" - ", " + ", " - ", " + ", " - ", " + ", " - ", " + ", " 4 "], #4
    [" W ", " - ", " W ", " - ", " W ", " - ", " W ", " - ", " 3 "], #5
    [" - ", " W ", " - ", " W ", " - ", " W ", " - ", " W ", " 2 "], #6
    [" W ", " - ", " W ", " - ", " W ", " - ", " W ", " - ", " 1 "], #7
    [" a ", " b ", " c ", " d ", " e ", " f ", " g ", " h "] #8
    ]


def showField():
    print(field1[0][0] + field1[0][1] + field1[0][2] + field1[0][3] + field1[0][4] + field1[0][5] + field1[0][6] + field1[0][7] + field1[0][8])
    print(field1[1][0] + field1[1][1] + field1[1][2] + field1[1][3] + field1[1][4] + field1[1][5] + field1[1][6] + field1[1][7] + field1[1][8])
    print(field1[2][0] + field1[2][1] + field1[2][2] + field1[2][3] + field1[2][4] + field1[2][5] + field1[2][6] + field1[2][7] + field1[2][8])
    print(field1[3][0] + field1[3][1] + field1[3][2] + field1[3][3] + field1[3][4] + field1[3][5] + field1[3][6] + field1[3][7] + field1[3][8])
    print(field1[4][0] + field1[4][1] + field1[4][2] + field1[4][3] + field1[4][4] + field1[4][5] + field1[4][6] + field1[4][7] + field1[4][8])
    print(field1[5][0] + field1[5][1] + field1[5][2] + field1[5][3] + field1[5][4] + field1[5][5] + field1[5][6] + field1[5][7] + field1[5][8])
    print(field1[6][0] + field1[6][1] + field1[6][2] + field1[6][3] + field1[6][4] + field1[6][5] + field1[6][6] + field1[6][7] + field1[6][8])
    print(field1[7][0] + field1[7][1] + field1[7][2] + field1[7][3] + field1[7][4] + field1[7][5] + field1[7][6] + field1[7][7] + field1[7][8])
    print(field1[8][0] + field1[8][1] + field1[8][2] + field1[8][3] + field1[8][4] + field1[8][5] + field1[8][6] + field1[8][7])

def checkFirstIndex(checker_num_position):
    while True:
        if checker_num_position == "1":
            firstIndex = 7
            return firstIndex
        elif checker_num_position == "2":
            firstIndex = 6
            return firstIndex
        elif checker_num_position == "3":
            firstIndex = 5
            return firstIndex
        elif checker_num_position == "4":
            firstIndex = 4
            return firstIndex
        elif checker_num_position == "5":
            firstIndex = 3
            return firstIndex
        elif checker_num_position == "6":
            firstIndex = 2
            return firstIndex
        elif checker_num_position == "7":
            firstIndex = 1
            return firstIndex
        elif checker_num_position == "8":
            firstIndex = 0
            return firstIndex
        else:
            print("Wrong checker_num_position")
            break

def checkSecondIndex(checker_char_position):
    while True:
        if checker_char_position == "a":
            secondIndex = 0
            return secondIndex
        elif checker_char_position == "b":
            secondIndex = 1
            return secondIndex
        elif checker_char_position == "c":
            secondIndex = 2
            return secondIndex
        elif checker_char_position == "d":
            secondIndex = 3
            return secondIndex
        elif checker_char_position == "e":
            secondIndex = 4
            return secondIndex
        elif checker_char_position == "f":
            secondIndex = 5
            return secondIndex
        elif checker_char_position == "g":
            secondIndex = 6
            return secondIndex
        elif checker_char_position == "h":
            secondIndex = 7
            return secondIndex
        else:
            print("Wrong checker_char_position")
            break

def checkNewFirstIndex(next_checker_num):
    while True:
        if next_checker_num == "1":
            new_firstIndex = 7
            return new_firstIndex
        elif next_checker_num == "2":
            new_firstIndex = 6
            return new_firstIndex
        elif next_checker_num == "3":
            new_firstIndex = 5
            return new_firstIndex
        elif next_checker_num == "4":
            new_firstIndex = 4
            return new_firstIndex
        elif next_checker_num == "5":
            new_firstIndex = 3
            return new_firstIndex
        elif next_checker_num == "6":
            new_firstIndex = 2
            return new_firstIndex
        elif next_checker_num == "7":
            new_firstIndex = 1
            return new_firstIndex
        elif next_checker_num == "8":
            new_firstIndex = 0
            return new_firstIndex
        else:
            print("Wrong next_checker_num")
            break

def checkNewSecondIndex(next_checker_char):
    while True:
        if next_checker_char == "a":
            new_secondIndex = 0
            return new_secondIndex
        elif next_checker_char == "b":
            new_secondIndex = 1
            return new_secondIndex
        elif next_checker_char == "c":
            new_secondIndex = 2
            return new_secondIndex
        elif next_checker_char == "d":
            new_secondIndex = 3
            return new_secondIndex
        elif next_checker_char == "e":
            new_secondIndex = 4
            return new_secondIndex
        elif next_checker_char == "f":
            new_secondIndex = 5
            return new_secondIndex
        elif next_checker_char == "g":
            new_secondIndex = 6
            return new_secondIndex
        elif next_checker_char == "h":
            new_secondIndex = 7
            return new_secondIndex
        else:
            print("Wrong next_checker_char")
            break

def checkCanGoNext_for_white():
    if field1[checkFirstIndex(checker_num_position)][checkSecondIndex(checker_char_position)] == " W ": #check if checker is W
        old_check_index_1 = [checkFirstIndex(checker_num_position)] 
        old_check_index_2 = [checkSecondIndex(checker_char_position)]
        print(old_check_index_1, old_check_index_2)

        next_checker_num = input("(White player) Choose next checker num position: ")
        next_checker_char = input("(White player) Choose next checker char position: ")

        if field1[checkNewFirstIndex(next_checker_num)][checkNewSecondIndex(next_checker_char)] == " + ":
            new_check_index_1 = [checkNewFirstIndex(next_checker_num)]
            new_check_index_2 = [checkNewSecondIndex(next_checker_char)]
            print(new_check_index_1, new_check_index_2)

            if old_check_index_1[0] - 1 == new_check_index_1[0] and old_check_index_2[0] + 1 == new_check_index_2[0]:
                field1[new_check_index_1[0]][new_check_index_2[0]] = " W "
                field1[old_check_index_1[0]][old_check_index_2[0]] = " + "
                showField()
                

            elif old_check_index_1[0] - 1 == new_check_index_1[0] and old_check_index_2[0] - 1 == new_check_index_2[0]:
                field1[new_check_index_1[0]][new_check_index_2[0]] = " W "
                field1[old_check_index_1[0]][old_check_index_2[0]] = " + "
                showField()
                
                    
        elif field1[checkNewFirstIndex(next_checker_num)][checkNewSecondIndex(next_checker_char)] == " B ":
            new_check_index_1 = [checkNewFirstIndex(next_checker_num)]
            new_check_index_2 = [checkNewSecondIndex(next_checker_char)]
            print(new_check_index_1, new_check_index_2)

            if old_check_index_1[0] - 1 == new_check_index_1[0] and old_check_index_2[0] + 1 == new_check_index_2[0]:
                field1[new_check_index_1[0]][new_check_index_2[0]] = " W "
                field1[old_check_index_1[0]][old_check_index_2[0]] = " + "
                showField()
                
                

            elif old_check_index_1[0] - 1 == new_check_index_1[0] and old_check_index_2[0] - 1 == new_check_index_2[0]:
                field1[new_check_index_1[0]][new_check_index_2[0]] = " W "
                field1[old_check_index_1[0]][old_check_index_2[0]] = " + "
                showField()
        
                        

            

def checkCanGoNext_for_black():
    if field1[checkFirstIndex(checker_num_position)][checkSecondIndex(checker_char_position)] == " B ":
        old_check_index_1 = [checkFirstIndex(checker_num_position)]
        old_check_index_2 = [checkSecondIndex(checker_char_position)]
        print(old_check_index_1, old_check_index_2)

        next_checker_num = input("(Black player) Choose next checker num position: ")
        next_checker_char = input("(Black player) Choose next checker char position: ")

        if field1[checkNewFirstIndex(next_checker_num)][checkNewSecondIndex(next_checker_char)] == " + ":
            new_check_index_1 = [checkNewFirstIndex(next_checker_num)]
            new_check_index_2 = [checkNewSecondIndex(next_checker_char)]
            print(new_check_index_1, new_check_index_2)

            if old_check_index_1[0] + 1 == new_check_index_1[0] and old_check_index_2[0] + 1 == new_check_index_2[0]:
                field1[new_check_index_1[0]][new_check_index_2[0]] = " B "
                field1[old_check_index_1[0]][old_check_index_2[0]] = " + "
                showField()

            elif old_check_index_1[0] + 1 == new_check_index_1[0] and old_check_index_2[0] - 1 == new_check_index_2[0]:
                field1[new_check_index_1[0]][new_check_index_2[0]] = " B "
                field1[old_check_index_1[0]][old_check_index_2[0]] = " + "
                showField()

        elif field1[checkNewFirstIndex(next_checker_num)][checkNewSecondIndex(next_checker_char)] == " W ":
            new_check_index_1 = [checkNewFirstIndex(next_checker_num)]
            new_check_index_2 = [checkNewSecondIndex(next_checker_char)]
            print(new_check_index_1, new_check_index_2)

            if old_check_index_1[0] + 1 == new_check_index_1[0] and old_check_index_2[0] + 1 == new_check_index_2[0]:
                
                field1[new_check_index_1[0]][new_check_index_2[0]] = " B "
                field1[old_check_index_1[0]][old_check_index_2[0]] = " + "
                showField()

            elif old_check_index_1[0] + 1 == new_check_index_1[0] and old_check_index_2[0] - 1 == new_check_index_2[0]:
                field1[new_check_index_1[0]][new_check_index_2[0]] = " B "
                field1[old_check_index_1[0]][old_check_index_2[0]] = " + "
                showField()


i = 0
showField()
while True:
    if i % 2 == 0:

        if " W " not in field1[0] and " W " not in field1[1] and " W " not in field1[2] and " W " not in field1[3] and " W " not in field1[4] and " W " not in field1[5] and " W " not in field1[6] and " W " not in field1[7]:
            print("Black wins")
            break
        elif " B " not in field1[0] and " B " not in field1[1] and " B " not in field1[2] and " B " not in field1[3] and " B " not in field1[4] and " B " not in field1[5] and " B " not in field1[6] and " B " not in field1[7]:
            print("White wins")
            break

        checker_num_position = input("(White player) Choose checker num position: ")
        checker_char_position = input("(White player) Choose checker char position: ")
        checkCanGoNext_for_white()
        i+=1
            
        
    else:

        if " W " not in field1[0] and " W " not in field1[1] and " W " not in field1[2] and " W " not in field1[3] and " W " not in field1[4] and " W " not in field1[5] and " W " not in field1[6] and " W " not in field1[7]:
            print("Black wins")
            break
        elif " B " not in field1[0] and " B " not in field1[1] and " B " not in field1[2] and " B " not in field1[3] and " B " not in field1[4] and " B " not in field1[5] and " B " not in field1[6] and " B " not in field1[7]:
            print("White wins")
            break
            
        checker_num_position = input("(Black player) Choose checker num position: ")
        checker_char_position = input("(Black player) Choose checker char position: ")
        checkCanGoNext_for_black()
        i+=1
