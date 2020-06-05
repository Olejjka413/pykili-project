from tkinter import *
from tkinter import font
import tkinter.messagebox
from functools import partial
import random
import sys
import os
 
root = Tk()
root.wm_title('Морской бой')
root.configure(background='midnight blue')
font1 = font.Font(family='Comic Sans MS', size=12, weight='bold')
font_big = font.Font(family='Comic Sans MS', size=16, weight='bold')
font_normal = font.Font(family='Comic Sans MS', size=10, weight='normal')
ships = {'4': 4, '3': 3, '2': 2, '1': 1}
AI = False

 
#генерация игрового поля
def player_field_generator():
    field = []
    t = []
    # вверхняя граница
    t += (10 + 2) * ['# ']
    field.append(t)
    rad = ['# ']
    for r in range(0, 10):
        rad.append('~ ')
    # новая строка
    rad.append('# ')
    for k in range(0, 10):
        field.append(list(rad))
    # нижняя граница
    field.append(t)
    return field
 
#размещение кораблей
def ship_placer(ship, board):
    while True:
        coords = []
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        o = random.randint(0, 1)
        if o == 0:
            ori = 'в' #в-вертикально
        else:
            ori = 'г' #г-горизонтально 
        # проверка чтобы корабль не вышел за предели поля
        if (ori == 'в' and y + ships[ship] > 10) or (ori == 'г' and x + ships[ship] > 10):
            pass
        else:
            if ori == 'в':
                # проверка доступности места
                for i in range(-1, (ships[ship] + 1)):
                    for j in range(-1, 2):
                        coords.append(board[y + i][x + j])
                if ': ' not in coords:
                    for i in range(ships[ship]):
                        board[y + i][x] = ': '
                    break
            elif ori == 'г':
                for i in range(-1, (ships[ship] + 1)):
                    for j in range(-1, 2):
                        coords.append(board[y + j][x + i])
                if ': ' not in coords:
                    for i in range(ships[ship]):
                        board[y][x + i] = ': '
                    break



#счетчик кораблей 
def all_ships(board):
    for ship in ships:
        for _ in range(0, (5 - ships[ship])):
            ship_placer(ship, board)


#возобновляет программу, чтобы сыграть снова#
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


#активируется при победе или поражении, чтобы сообщить об этом и предложить сыграть снова# 
def messager(name):
    answer = tkinter.messagebox.askquestion('Игра закончена', name + ', желаете сыграть снова ?')
    if answer == 'yes':
        restart_program()
    elif answer == 'no':
        quit()
 
#в зависимости от количества игроков выбирае нужную конфигурацию#
def num_players(number):
    global AI
    for bt_list in every_button[1]:
        for bt in bt_list:
            bt['state'] = 'normal'
    if number == 1:
        player2_or_AI.set('Компьютер')
        AI = True
    else:
        for bt_list in every_button[0]:
            for bt in bt_list:
                bt['state'] = 'normal'
        player2_or_AI.set('Игрок 2')
 
 
info = StringVar()
player2_or_AI = StringVar()
every_button = []
 
 
#создает название игре и кнопам с количеством игроков
def buttons_labels():
    o = StringVar()
    Label(root, text='МОРСКОЙ БОЙ', fg='white', bg='midnight blue', font=font_big).grid(row=0, column=10, columnspan=9)
    Label(root, textvariable=info, fg='black', bg='midnight blue', font=font1).grid(row=12, column=6, columnspan=18)
    for _ in range(10):
        Label(root, text="   ", bg='midnight blue').grid(row=_, column=0)
    Button(root, width=7, height=1, text=' 1 Игрок', font=font1, fg="white", activebackground='midnight blue',
           bg='midnight blue', command=lambda: num_players(1)).grid(row=2, column=1)
    Button(root, width=7, height=1, text='2 Игрока', font=font1, fg="white", activebackground='midnight blue',
           bg='midnight blue', command=lambda: num_players(2)).grid(row=3, column=1)
    for _ in range(10):
        Label(root, text="   ", bg='midnight blue').grid(row=_, column=2)
    for _ in range(10):
        Label(root, width=20, text="   ", bg='midnight blue').grid(row=_, column=25)
    
 
#обработка хода компьютера 
def comp_shoots(y, x, player_1_field):
    if player_1_field[y][x] == ': ':
        comp_scorer()
        player_1_field[y][x] = 'X ' #попадание + стрелять снова
        every_button[0][y-1][x-1].configure(text='X', fg='black', bg='red')
        x = random.randint(1, 10) 
        y = random.randint(1, 10)            
        comp_shoots(y, x, player_1_field)
        #если уже стрелял по этой клетке то снова
    elif player_1_field[y][x] == 'X ' or player_1_field[y][x] == 'O ':
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        comp_shoots(y, x, player_1_field)
    else: #если мимо
        player_1_field[y][x] = 'O '
        every_button[0][y-1][x-1].configure(text='O', fg='white')
                        
#обраотка хода игроков
def player_shoot(a, b, field, all_buttons, info, player, field2):
    global AI
    if field[a + 1][b + 1] == 'O ' or field[a + 1][b + 1] == 'X ':
        #если игрок уже стрелял в клетку
        tkinter.messagebox.showerror('ОЙ!','Уже стрелял сюда!')
    elif field[a + 1][b + 1] == ': ':
        #если попал
        field[a + 1][b + 1] = 'X '
        all_buttons[a][b].configure(text='X', fg='black', bg='red', activebackground='red')
        score(player)
    else:
        field[a + 1][b + 1] = 'O '
        all_buttons[a][b].configure(text='O', fg='White', activeforeground='white')
        if AI: #если играем против компьютера то переключаемся на его ход
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            comp_shoots(y, x, field2)
#счетчик попаданий для игрока/игроков     
def score(player):
    global player_1_score
    global player_2_score
    if player == 'Игрок 2':
        player_1_score+=1
    else:
        player_2_score+=1
    if player_1_score == 20:
        messager('Игрок 1 победил')
    if player_2_score == 20:
        messager('Игрок 2 победил')
#счетчик попаданий для компьютера
def comp_scorer():
    global comp_score
    comp_score+=1
    if comp_score == 20:
        messager('Вы проиграли')
    

#в зависимости от выбора режима игры размещает кнопки
def side(player, allbuttons):
    col = 4 if player == 'Игрок 1' else 15
    for row in range(10):
        for column in range(10):
            allbuttons[row][column].grid(row=1 + row, column=col + column)
    if player == 'Игрок 1':
        label2 = Label(root, text='Игрок 1', font=font1, fg='white', bg='midnight blue')
        label2.grid(row=11, column=4, columnspan=10)
    else:
        label3 = Label(root, textvariable=player2_or_AI, font=font1, fg='white', bg='midnight blue')
        label3.grid(row=11, column=15, columnspan=10)
 
#создает функциональные кнопки
def field_buttons(field, info, player, field2):
    allbuttons = []
    a = 0
    for i in range(10):
        b = 0
        buttons = []
        for j in range(10):
            #полученые кнопки будут вызывать функцию player_shoot + если редим одного игрока деактивировать другое поле
            button = Button(root, width=3 , height=1, font=font1, bg="sky blue", activebackground="sky blue",
                            command=partial(player_shoot, a, b, field, allbuttons, info, player, field2), state="disable")
            buttons.append(button)
            b += 1
        allbuttons.append(list(buttons))
        a += 1
    every_button.append(allbuttons)
    side(player, allbuttons)
 
 
def middle_board_space():
    for _ in range(10):
        Label(root, text="   ", bg='midnight blue').grid(row=1 + _, column=14)
 
 
def main():
    global player_1_score
    global player_2_score
    global comp_score
    player_1_score = 0
    player_2_score = 0
    comp_score = 0
    player_1_field = player_field_generator()
    player_2_field = player_field_generator()
    all_ships(player_1_field)
    all_ships(player_2_field)
    info = StringVar()
    buttons_labels()
    field_buttons(player_1_field, info, 'Игрок 1', player_2_field)
    middle_board_space()
    field_buttons(player_2_field, info, 'Игрок 2', player_1_field)
 
 
main()
root.mainloop()
