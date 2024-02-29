"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""
#tic,tac,toe

pattern = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

player_one = "X"
player_two = "Y"

print("[x,y] = [0,0] at bottom left corner")
def check_win():
    if pattern[0][0] == pattern[0][1] == pattern[0][2] != 0:
        return True
    elif pattern[1][0] == pattern[1][1] == pattern[1][2] != 0:
        return True
    elif pattern[2][0] == pattern[2][1] == pattern[2][2] != 0:
        return True
    elif pattern[0][0] == pattern[1][0] == pattern[2][0] != 0:
        return True
    elif pattern[0][1] == pattern[1][1] == pattern[2][1] != 0:
        return True
    elif pattern[0][2] == pattern[1][2] == pattern[2][2] != 0:
        return True
    elif pattern[0][0] == pattern[1][1] == pattern[2][2] != 0:
        return True
    elif pattern[0][2] == pattern[1][1] == pattern[2][0] != 0:
        return True
    else:
        return False
    

def pattern_display():
    print(f'{str(pattern[2]):^10}')
    print(f'{str(pattern[1]):^10}')
    print(f'{str(pattern[0]):^10}')

def check_input (player):
    while True:
        inp = input(f"Please enter the location for your turn({player})[x,y]: ").split()
        if len(inp) != 2:
            print("Invalid input")
            continue
        elif not inp[0].isdigit() or not inp[1].isdigit():
            print("Invalid input")
            continue
        else:
            break

    return inp

while True:
    pattern_display()
    locate = check_input("X")
    locate[0] = int(locate[0])
    locate[1] = int(locate[1])
    pattern[locate[0]][locate[1]] = "X"
    if check_win():
        print("Player 1 win")
        break
    pattern_display()
    locate = check_input("Y")
    locate[0] = int(locate[0])
    locate[1] = int(locate[1])
    pattern[locate[0]][locate[1]] = "Y"
    if check_win():
        print("Player 2 win")
        break
    
