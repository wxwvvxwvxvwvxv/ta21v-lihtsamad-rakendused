import random
map = [
    [12, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [24, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
]

start_pos_x = 0
start_pos_y = 0

y_rows = 5
x_columns = 5

def get_next_free_position(current_position_y, current_position_x):
    random_number=random.random()

    can_go_right = current_position_x + 1 < x_columns and map[current_position_y][current_position_x+1] == 1
    can_go_left = current_position_x - 1 >= 0 and map[current_position_y][current_position_x - 1] == 1
    can_go_bottom = current_position_y + 1 < y_rows and map[current_position_y + 1][current_position_x] == 1
    can_go_top = current_position_y - 1 >= 0 and map[current_position_y - 1][current_position_x] == 1
    finish = current_position_y - 1 >= 0 and map[current_position_y - 1][current_position_x] == 24

   

    if can_go_bottom and can_go_left:
        if random_number < 0.25:
            print("can go bottom")
            return [current_position_y + 1, current_position_x]
        else:
            print("can fo left")
            return [current_position_y, current_position_x - 1]
    

    if can_go_left and can_go_right:
        if random_number > 0.5:
            print("can go left")
            return [current_position_y, current_position_x - 1]
        else:
            print("can go right")
            return [current_position_y, current_position_x + 1]

    if can_go_bottom and can_go_right and can_go_top:
        if random_number < 0.25:
            print("can go bottom")
            return [current_position_y + 1, current_position_x]
        elif random_number > 0.25 and random_number < 0.5:
            print("can go right")
            return [current_position_y, current_position_x + 1]
        else:
            print("can go top")
            return [current_position_y - 1, current_position_x]
            
    if finish and can_go_right:
        if random_number < 0.5:
            print("can go right")
            return [current_position_y, current_position_x + 1]
        elif random_number > 0.5:
            print("finish")
            return [current_position_y -1 , current_position_x]
            
    if can_go_left:
        
        print("can go left")
        return [current_position_y, current_position_x - 1]

    if can_go_right:
        
        print("can go right")
        return [current_position_y, current_position_x + 1]

    if can_go_bottom:
        
        print("can go bottom")
        return [current_position_y + 1, current_position_x]

    if can_go_top:
        
        print("can go up")
        return [current_position_y -1 , current_position_x]

next_free_position = get_next_free_position(start_pos_x, start_pos_y)
print("Next free position is: ", next_free_position )

while next_free_position:
    next_free_position = get_next_free_position(next_free_position[0], next_free_position[1])
    print("Next free position is: ", next_free_position )
    if next_free_position == [3,0]:
        break