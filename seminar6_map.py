# Создайте программу для игры в ""Крестики-нолики"".
import random, time
empty_field=[['_','_','_'],['_','_','_'],['_','_','_']]
print(empty_field[0][1])
print(*empty_field, sep="\n")
turn=round(time.time())%2==0
win=False
def fine_winer(a):#ходит ноликами
    play="O"
    if a: play="X"
    for i in range(3):
        if empty_field[i][0]==play and empty_field[i][1]==play and empty_field[i][2]==play:return True
        if empty_field[0][i]==play and empty_field[1][i]==play and empty_field[2][i]==play:return True
        if empty_field[0][0]==play and empty_field[1][1]==play and empty_field[2][2]==play:return True
        if empty_field[0][2]==play and empty_field[1][1]==play and empty_field[2][0]==play:return True
        # else: print ('Ничья')
        return False
        print("Победа!!!")
while not win:
    user_input=list(map(int,input("Введите координаты строка/столбец, через пробел ").split()))
    if turn and empty_field[user_input[0]-1][user_input[1]-1]=='_':
        empty_field[user_input[0]-1][user_input[1]-1]='X'
    elif not turn and empty_field[user_input[0]-1][user_input[1]-1]=='_':
        empty_field[user_input[0]-1][user_input[1]-1]='O'
    else: turn= not turn
    win= fine_winer(turn)
    turn=not turn
    print(*empty_field, sep="\n")
print(win)
