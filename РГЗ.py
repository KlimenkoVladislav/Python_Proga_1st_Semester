import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import random

def start():
    
    def pole_igroka_sozdanie(pole_igroka_Frame, block):
        pole_igroka_massiv = []
        first_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        first_column = 'АБВГДЕЖЗИК'
        
        for i in range(11):
            line = []
            for j in range(11):
                if i==0 and j!=0:
                    numbers = tk.Label(pole_igroka_Frame, text = str(first_row[j-1]), font=('Times New Roman', 14))
                    numbers.grid(row=i, column=j, ipadx=14, ipady=14)
                else:
                    if j==0 and i!=0:
                        bukva = tk.Label(pole_igroka_Frame, text = first_column[i-1], font=('Times New Roman', 14))
                        bukva.grid(row=i, column=j, ipadx=14, ipady=14)
                    elif i!=0 and j!=0:
                        if block == 1:
                            kletka = tk.Button(pole_igroka_Frame, bg = '#007FFF', state=tk.DISABLED)
                        if block ==0:
                            kletka = tk.Button(pole_igroka_Frame, bg = '#007FFF')
                        kletka.grid(row=i, column=j, ipadx=20, ipady=15)
                        line.append(kletka)
            if len(line)!=0:
                pole_igroka_massiv.append(line)

        return pole_igroka_massiv

    def pole_robota_sozdanie(pole_robota_Frame, block):
        pole_robota_massiv = []
        first_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        first_column = 'АБВГДЕЖЗИК'
        
        for i in range(11):
            line = []
            for j in range(11):
                if i==0 and j!=0:
                    numbers = tk.Label(pole_robota_Frame, text = str(first_row[j-1]), font=('Times New Roman', 14))
                    numbers.grid(row=i, column=j, ipadx=14, ipady=14)
                else:
                    if j==0 and i!=0:
                        bukva = tk.Label(pole_robota_Frame, text = first_column[i-1], font=('Times New Roman', 14))
                        bukva.grid(row=i, column=j, ipadx=14, ipady=14)
                    elif i!=0 and j!=0:
                        if block == 1:
                            kletka = tk.Button(pole_robota_Frame, bg = '#007FFF', state=tk.DISABLED)
                        if block == 0:
                            kletka = tk.Button(pole_robota_Frame, bg = '#007FFF')
                        kletka.grid(row=i, column=j, ipadx=20, ipady=15)
                        line.append(kletka)
            if len(line)!=0:
                pole_robota_massiv.append(line)

        return pole_robota_massiv

    def ships_igrok(pole_igroka_massiv):
        
        def vibor_ship(ship_size, pole_igroka_massiv, pole_igroka_massiv_012):
            nonlocal ship_size_global
            ship_size_global = ship_size
            
            ship_1_knopka.config(state = tk.DISABLED)
            ship_2_knopka.config(state = tk.DISABLED)
            ship_3_knopka.config(state = tk.DISABLED)
            ship_4_knopka.config(state = tk.DISABLED)
            delete_ship_button.config(state = tk.DISABLED)
            
            for i in range(10):
                for j in range(10):
                    pole_igroka_massiv[i][j].config(state=tk.NORMAL, command = lambda a = i, b = j: vibor_mesta(ship_size, pole_igroka_massiv, a, b, pole_igroka_massiv_012))

        def vibor_mesta(ship_size, pole_igroka_massiv, i, j, pole_igroka_massiv_012):
            nonlocal x, y
            x = i
            y = j
            
            if pole_igroka_massiv_012[i][j]==1:
                pole_igroka_massiv[i][j].config(bg = 'green')
                pole_igroka_massiv_012[i][j] = 2
                
                for a in range(10):
                    for b in range(10):
                        pole_igroka_massiv[a][b].config(state=tk.DISABLED)
                
                if i-ship_size+1>=0 and pole_igroka_massiv_012[i-ship_size+1][j]==1:
                    for a in range(1, ship_size):
                        pole_igroka_massiv[i-a][j].config(bg = 'grey')
                if j+ship_size-1<=9 and pole_igroka_massiv_012[i][j+ship_size-1]==1:
                    for a in range(1, ship_size):
                        pole_igroka_massiv[i][j+a].config(bg = 'grey')
                if i+ship_size-1<=9 and pole_igroka_massiv_012[i+ship_size-1][j]==1:
                    for a in range(1, ship_size):
                        pole_igroka_massiv[i+a][j].config(bg = 'grey')
                if j-ship_size+1>=0 and pole_igroka_massiv_012[i][j-ship_size+1]==1:
                    for a in range(1, ship_size):
                        pole_igroka_massiv[i][j-a].config(bg = 'grey')
                    
        def napravlenie(event, pole_igroka_massiv, pole_igroka_massiv_012, ship_size):
            nonlocal kol_ship_1, kol_ship_2, kol_ship_3, kol_ship_4, x, y
            
            if x<0 and y<0:
                return 0
            
            if event.keysym == 'Up' and x-ship_size+1>=0:
                for i in range(1, ship_size):
                    if pole_igroka_massiv_012[x-i][y]!=1:
                        return 0
                
                for i in range(ship_size-1, 0, -1):
                    pole_igroka_massiv[x-i][y].config(bg = 'green')
                    pole_igroka_massiv_012[x-i][y] = 2
                    if x+ship_size-1<=9 and pole_igroka_massiv_012[x+1][y]==2:
                        pole_igroka_massiv[x+i][y].config(bg = 'grey')
                        pole_igroka_massiv_012[x+i][y] = 1
                    if y+ship_size-1<=9 and pole_igroka_massiv_012[x][y+1]==2:
                        pole_igroka_massiv[x][y+i].config(bg = 'grey')
                        pole_igroka_massiv_012[x][y+i] = 1
                    if y-ship_size+1>=0 and pole_igroka_massiv_012[x][y-1]==2:
                        pole_igroka_massiv[x][y-i].config(bg = 'grey')
                        pole_igroka_massiv_012[x][y-i] = 1
                
            elif event.keysym == 'Down' and x+ship_size-1<=9:
                for i in range(1, ship_size):
                    if pole_igroka_massiv_012[x+i][y]!=1:
                        return 0
                
                for i in range(ship_size-1, 0, -1):
                    pole_igroka_massiv[x+i][y].config(bg = 'green')
                    pole_igroka_massiv_012[x+i][y] = 2
                    if x-ship_size+1>=0 and pole_igroka_massiv_012[x-1][y]==2:
                        pole_igroka_massiv[x-i][y].config(bg = 'grey')
                        pole_igroka_massiv_012[x-i][y] = 1
                    if y+ship_size-1<=9 and pole_igroka_massiv_012[x][y+1]==2:
                        pole_igroka_massiv[x][y+i].config(bg = 'grey')
                        pole_igroka_massiv_012[x][y+i] = 1
                    if y-ship_size+1>=0 and pole_igroka_massiv_012[x][y-1]==2:
                        pole_igroka_massiv[x][y-i].config(bg = 'grey')
                        pole_igroka_massiv_012[x][y-i] = 1
            
            elif event.keysym == 'Right' and y+ship_size-1<=9:
                for i in range(1, ship_size):
                    if pole_igroka_massiv_012[x][y+i]!=1:
                        return 0
                
                for i in range(ship_size-1, 0, -1):
                    pole_igroka_massiv[x][y+i].config(bg = 'green')
                    pole_igroka_massiv_012[x][y+i] = 2
                    if x-ship_size+1>=0 and pole_igroka_massiv_012[x-1][y]==2:
                        pole_igroka_massiv[x-i][y].config(bg = 'grey')
                        pole_igroka_massiv_012[x-i][y] = 1
                    if x+ship_size-1<=9 and pole_igroka_massiv_012[x+1][y]==2:
                        pole_igroka_massiv[x+i][y].config(bg = 'grey')
                        pole_igroka_massiv_012[x+i][y] = 1
                    if y-ship_size+1>=0 and pole_igroka_massiv_012[x][y-1]==2:
                        pole_igroka_massiv[x][y-i].config(bg = 'grey')
                        pole_igroka_massiv_012[x][y-i] = 1
            
            elif event.keysym == 'Left' and y-ship_size+1>=0:
                for i in range(1, ship_size):
                    if pole_igroka_massiv_012[x][y-i]!=1:
                        return 0
                
                for i in range(ship_size-1, 0, -1):
                    pole_igroka_massiv[x][y-i].config(bg = 'green')
                    pole_igroka_massiv_012[x][y-i] = 2
                    if x-ship_size+1>=0 and pole_igroka_massiv_012[x-1][y]==2:
                        pole_igroka_massiv[x-i][y].config(bg = 'grey')
                        pole_igroka_massiv_012[x-i][y] = 1
                    if x+ship_size-1<=9 and pole_igroka_massiv_012[x+1][y]==2:
                        pole_igroka_massiv[x+i][y].config(bg = 'grey')
                        pole_igroka_massiv_012[x+i][y] = 1
                    if y+ship_size-1<=9 and pole_igroka_massiv_012[x][y+1]==2:
                        pole_igroka_massiv[x][y+i].config(bg = 'grey')
                        pole_igroka_massiv_012[x][y+i] = 1
                
            elif event.keysym == 'Return':
                while True:
                    if ship_size>=2:
                        if x+1<=9 and pole_igroka_massiv_012[x+1][y]==2:
                            break
                        elif x-1>=0 and pole_igroka_massiv_012[x-1][y]==2:
                            break
                        elif y+1<=9 and pole_igroka_massiv_012[x][y+1]==2:
                            break
                        elif y-1>=0 and pole_igroka_massiv_012[x][y-1]==2:
                            break
                        else:
                            msg.showerror('error', 'Вы не выбрали расположение корабля')
                            return 0
                    else:
                        break
                    
                for i in range(1, ship_size):
                    if x-ship_size+1>=0 and pole_igroka_massiv_012[x-i][y]!=2:
                        pole_igroka_massiv[x-i][y].config(bg = '#007FFF')
                    if x+ship_size-1<=9 and pole_igroka_massiv_012[x+i][y]!=2:
                        pole_igroka_massiv[x+i][y].config(bg = '#007FFF')
                    if y+ship_size-1<=9 and pole_igroka_massiv_012[x][y+i]!=2:
                        pole_igroka_massiv[x][y+i].config(bg = '#007FFF')
                    if y-ship_size+1>=0 and pole_igroka_massiv_012[x][y-i]!=2:
                        pole_igroka_massiv[x][y-i].config(bg = '#007FFF')
                
                ogr()
                
                if ship_size==1:
                    kol_ship_1-=1
                    ship_1_label.config(text = str(kol_ship_1))
                    if kol_ship_1!=0:
                        ship_1_knopka.config(state = tk.NORMAL)
                    else:
                        ship_1_knopka.config(bg = 'grey')
                    
                    if kol_ship_2!=0:
                        ship_2_knopka.config(state = tk.NORMAL)
                    if kol_ship_3!=0:
                        ship_3_knopka.config(state = tk.NORMAL)
                    if kol_ship_4!=0:
                        ship_4_knopka.config(state = tk.NORMAL)
                
                elif ship_size==2:
                    kol_ship_2-=1
                    ship_2_label.config(text = str(kol_ship_2))
                    if kol_ship_2!=0:
                        ship_2_knopka.config(state = tk.NORMAL)
                    else:
                        ship_2_knopka.config(bg = 'grey')
                    
                    if kol_ship_1!=0:
                        ship_1_knopka.config(state = tk.NORMAL)
                    if kol_ship_3!=0:
                        ship_3_knopka.config(state = tk.NORMAL)
                    if kol_ship_4!=0:
                        ship_4_knopka.config(state = tk.NORMAL)
                
                elif ship_size==3:
                    kol_ship_3-=1
                    ship_3_label.config(text = str(kol_ship_3))
                    if kol_ship_3!=0:
                        ship_3_knopka.config(state = tk.NORMAL)
                    else:
                        ship_3_knopka.config(bg = 'grey')
                    
                    if kol_ship_1!=0:
                        ship_1_knopka.config(state = tk.NORMAL)
                    if kol_ship_2!=0:
                        ship_2_knopka.config(state = tk.NORMAL)
                    if kol_ship_4!=0:
                        ship_4_knopka.config(state = tk.NORMAL)
                
                elif ship_size==4:
                    kol_ship_4-=1
                    ship_4_label.config(text = str(kol_ship_4))
                    if kol_ship_4!=0:
                        ship_4_knopka.config(state = tk.NORMAL)
                    else:
                        ship_4_knopka.config(bg = 'grey')
                    
                    if kol_ship_1!=0:
                        ship_1_knopka.config(state = tk.NORMAL)
                    if kol_ship_2!=0:
                        ship_2_knopka.config(state = tk.NORMAL)
                    if kol_ship_3!=0:
                        ship_3_knopka.config(state = tk.NORMAL)

                delete_ship_button.config(state = tk.NORMAL)
                x, y = -1, -1
            
            elif event.keysym == 'Escape':
                
                pole_igroka_massiv[x][y].config(bg = '#007FFF')
                pole_igroka_massiv_012[x][y] = 1
                
                if ship_size==2:
                    if x-1>=0 and pole_igroka_massiv_012[x-1][y]>=1:
                            pole_igroka_massiv[x-1][y].config(bg = '#007FFF')
                            pole_igroka_massiv_012[x-1][y] = 1
                    if y+1<=9 and pole_igroka_massiv_012[x][y+1]>=1:
                            pole_igroka_massiv[x][y+1].config(bg = '#007FFF')
                            pole_igroka_massiv_012[x][y+1] = 1
                    if x+1<=9 and pole_igroka_massiv_012[x+1][y]>=1:
                            pole_igroka_massiv[x+1][y].config(bg = '#007FFF')
                            pole_igroka_massiv_012[x+1][y] = 1
                    if y-1>=0 and pole_igroka_massiv_012[x][y-1]>=1:
                            pole_igroka_massiv[x][y-1].config(bg = '#007FFF')
                            pole_igroka_massiv_012[x][y-1] = 1
                
                if ship_size>=3:
                    if x-ship_size+1>=0 and pole_igroka_massiv_012[x-ship_size+1][y]>=1 and pole_igroka_massiv_012[x-ship_size+2][y]>=1:
                        for a in range(1, ship_size):
                            pole_igroka_massiv[x-a][y].config(bg = '#007FFF')
                            pole_igroka_massiv_012[x-a][y] = 1
                    if y+ship_size-1<=9 and pole_igroka_massiv_012[x][y+ship_size-1]>=1 and pole_igroka_massiv_012[x][y+ship_size-2]>=1:
                        for a in range(1, ship_size):
                            pole_igroka_massiv[x][y+a].config(bg = '#007FFF')
                            pole_igroka_massiv_012[x][y+a] = 1
                    if x+ship_size-1<=9 and pole_igroka_massiv_012[x+ship_size-1][y]>=1 and pole_igroka_massiv_012[x+ship_size-2][y]>=1:
                        for a in range(1, ship_size):
                            pole_igroka_massiv[x+a][y].config(bg = '#007FFF')
                            pole_igroka_massiv_012[x+a][y] = 1
                    if y-ship_size+1>=0 and pole_igroka_massiv_012[x][y-ship_size+1]>=1 and pole_igroka_massiv_012[x][y-ship_size+2]>=1:
                        for a in range(1, ship_size):
                            pole_igroka_massiv[x][y-a].config(bg = '#007FFF')
                            pole_igroka_massiv_012[x][y-a] = 1
                
                ship_1_knopka.config(state = tk.NORMAL)
                ship_2_knopka.config(state = tk.NORMAL)
                ship_3_knopka.config(state = tk.NORMAL)
                ship_4_knopka.config(state = tk.NORMAL)
                delete_ship_button.config(state = tk.NORMAL)
        
        def ogr():
            for i in range(10):
                for j in range(10):
                    if pole_igroka_massiv_012[i][j]!=2:
                        if i-1>=0 and pole_igroka_massiv_012[i-1][j]==2:
                            pole_igroka_massiv[i][j].config(bg = 'grey')
                            pole_igroka_massiv_012[i][j] = 0
                        if i-1>=0 and j+1<=9 and pole_igroka_massiv_012[i-1][j+1]==2:
                            pole_igroka_massiv[i][j].config(bg = 'grey')
                            pole_igroka_massiv_012[i][j] = 0
                        if j+1<=9 and pole_igroka_massiv_012[i][j+1]==2:
                            pole_igroka_massiv[i][j].config(bg = 'grey')
                            pole_igroka_massiv_012[i][j] = 0
                        if i+1<=9 and j+1<=9 and pole_igroka_massiv_012[i+1][j+1]==2:
                            pole_igroka_massiv[i][j].config(bg = 'grey')
                            pole_igroka_massiv_012[i][j] = 0
                        if i+1<=9 and pole_igroka_massiv_012[i+1][j]==2:
                            pole_igroka_massiv[i][j].config(bg = 'grey')
                            pole_igroka_massiv_012[i][j] = 0
                        if i+1<=9 and j-1>=0 and pole_igroka_massiv_012[i+1][j-1]==2:
                            pole_igroka_massiv[i][j].config(bg = 'grey')
                            pole_igroka_massiv_012[i][j] = 0
                        if j-1>=0 and pole_igroka_massiv_012[i][j-1]==2:
                            pole_igroka_massiv[i][j].config(bg = 'grey')
                            pole_igroka_massiv_012[i][j] = 0
                        if i-1>=0 and j-1>=0 and pole_igroka_massiv_012[i-1][j-1]==2:
                            pole_igroka_massiv[i][j].config(bg = 'grey')
                            pole_igroka_massiv_012[i][j] = 0
        
        def delete_ship():
            for i in range(10):
                for j in range(10):
                    pole_igroka_massiv[i][j].config(state = tk.NORMAL, command = lambda x=i, y=j: delete_ship_vibor(x, y))
            
            ship_1_knopka.config(state = tk.DISABLED)
            ship_2_knopka.config(state = tk.DISABLED)
            ship_3_knopka.config(state = tk.DISABLED)
            ship_4_knopka.config(state = tk.DISABLED)
            
        def delete_ship_vibor(x, y):
            if pole_igroka_massiv_012[x][y]!=2:
                msg.showerror('error', 'Это не корабль')
                ship_1_knopka.config(state = tk.NORMAL)
                ship_2_knopka.config(state = tk.NORMAL)
                ship_3_knopka.config(state = tk.NORMAL)
                ship_4_knopka.config(state = tk.NORMAL)
                for i in range(10):
                    for j in range(10):
                        pole_igroka_massiv[i][j].config(state = tk.DISABLED)
                return 0
            
            nonlocal kol_ship_1, kol_ship_2, kol_ship_3, kol_ship_4

            for i in range(10):
                for j in range(10):
                    pole_igroka_massiv[i][j].config(state = tk.DISABLED)
            
            pole_igroka_massiv_012[x][y] = 1
            pole_igroka_massiv[x][y].config(bg = '#007FFF')
            up, down, left, right = 1, 1, 1, 1
            ship_size = 1
            
            for i in range(1, 4):
                if up == 1 and x-i>=0 and pole_igroka_massiv_012[x-i][y] == 2:
                    pole_igroka_massiv_012[x-i][y] = 1
                    pole_igroka_massiv[x-i][y].config(bg = '#007FFF')
                    ship_size+=1
                else:
                    up = 0
                
                if down == 1 and x+i<=9 and pole_igroka_massiv_012[x+i][y] == 2:
                    pole_igroka_massiv_012[x+i][y] = 1
                    pole_igroka_massiv[x+i][y].config(bg = '#007FFF')
                    ship_size+=1
                else:
                    down = 0
                
                if left == 1 and y-i>=0 and pole_igroka_massiv_012[x][y-i] == 2:
                    pole_igroka_massiv_012[x][y-i] = 1
                    pole_igroka_massiv[x][y-i].config(bg = '#007FFF')
                    ship_size+=1
                else:
                    left = 0
                
                if right == 1 and y+i<=9 and pole_igroka_massiv_012[x][y+i] == 2:
                    pole_igroka_massiv_012[x][y+i] = 1
                    pole_igroka_massiv[x][y+i].config(bg = '#007FFF')
                    ship_size+=1
                else:
                    right = 0
            
            for i in range(10):
                for j in range(10):
                    if pole_igroka_massiv_012[i][j] == 0:
                        pole_igroka_massiv_012[i][j] = 1
                        pole_igroka_massiv[i][j].config(bg = '#007FFF')
            
            ogr()
            
            ship_1_knopka.config(state = tk.NORMAL)
            ship_2_knopka.config(state = tk.NORMAL)
            ship_3_knopka.config(state = tk.NORMAL)
            ship_4_knopka.config(state = tk.NORMAL)
            
            if ship_size == 1:
                if kol_ship_1 == 0:
                    ship_1_knopka.config(bg = 'green')
                kol_ship_1+=1
                ship_1_label.config(text = str(kol_ship_1))
            elif ship_size == 2:
                if kol_ship_2 == 0:
                    ship_2_knopka.config(bg = 'green')
                kol_ship_2+=1
                ship_2_label.config(text = str(kol_ship_2))
            elif ship_size == 3:
                if kol_ship_3 == 0:
                    ship_3_knopka.config(bg = 'green')
                kol_ship_3+=1
                ship_3_label.config(text = str(kol_ship_3))
            elif ship_size == 4:
                if kol_ship_4 == 0:
                    ship_4_knopka.config(bg = 'green')
                kol_ship_4+=1
                ship_4_label.config(text = str(kol_ship_4))

        def show_info():
            window_for_info = tk.Toplevel(window)
            window_for_info.title('Подсказка')
            window_for_info.geometry('460x110')
            
            label1 = tk.Label(window_for_info, text = 'Стрелочки - выбор направления корабля', font = ('Times New Roman', 14))
            label1.grid(row = 0)
            label2 = tk.Label(window_for_info, text = 'Enter - зафиксировать корабль', font = ('Times New Roman', 14))
            label2.grid(row = 1)
            label3 = tk.Label(window_for_info, text = 'Escape - вернуть незафиксированный корабль', font = ('Times New Roman', 14))
            label3.grid(row = 2)
            label4 = tk.Label(window_for_info, text = 'Кнопка "Удалить" - удаляет зафиксированный корабль', font = ('Times New Roman', 14))
            label4.grid(row = 3)
        
        nonlocal kol_ship_1, kol_ship_2, kol_ship_3, kol_ship_4, pole_igroka_massiv_012
        
        x = -1
        y = -1
        
        pole_for_ships = tk.Frame(window)
        pole_for_ships.grid(row = 0, column = 1, padx = 275, pady = 50)
        
        ship_size_global = 0
        
        ship_1_label = tk.Label(pole_for_ships, text = str(kol_ship_1), font = ('Times New Roman', 16))
        ship_1_label.grid(row = 0, column = 0, pady = 20)
        ship_2_label = tk.Label(pole_for_ships, text = str(kol_ship_2), font = ('Times New Roman', 16))
        ship_2_label.grid(row = 1, column = 0, pady = 20)
        ship_3_label = tk.Label(pole_for_ships, text = str(kol_ship_3), font = ('Times New Roman', 16))
        ship_3_label.grid(row = 2, column = 0, pady = 20)
        ship_4_label = tk.Label(pole_for_ships, text = str(kol_ship_4), font = ('Times New Roman', 16))
        ship_4_label.grid(row = 3, column = 0, pady = 20)
        
        ship_1_knopka = tk.Button(pole_for_ships, bg = 'green', command = lambda : vibor_ship(1, pole_igroka_massiv, pole_igroka_massiv_012))
        ship_1_knopka.grid(row = 0, column = 1, padx = 30, ipadx=30, ipady=15, sticky='w')
        ship_2_knopka = tk.Button(pole_for_ships, bg = 'green', command = lambda : vibor_ship(2, pole_igroka_massiv, pole_igroka_massiv_012))
        ship_2_knopka.grid(row = 1, column = 1, padx = 30, ipadx=60, ipady=15, sticky='w')
        ship_3_knopka = tk.Button(pole_for_ships, bg = 'green', command = lambda : vibor_ship(3, pole_igroka_massiv, pole_igroka_massiv_012))
        ship_3_knopka.grid(row = 2, column = 1, padx = 30, ipadx=90, ipady=15, sticky='w')
        ship_4_knopka = tk.Button(pole_for_ships, bg = 'green', command = lambda : vibor_ship(4, pole_igroka_massiv, pole_igroka_massiv_012))
        ship_4_knopka.grid(row = 3, column = 1, padx = 30, ipadx=120, ipady=15, sticky='w')
        
        info = tk.Button(pole_for_ships, bg = "#3B80C5", text = 'помощь', font = ('Times New Roman', 20), command = show_info)
        info.grid(row = 5, column = 0, columnspan = 2)
        delete_ship_button = tk.Button(pole_for_ships, bg = 'red', text = 'Удалить корабль', font = ('Times New Roman', 20), command = delete_ship)
        delete_ship_button.grid(row = 4, column = 0, columnspan=2, pady = 100)
                
        window.bind('<KeyPress>', lambda event : napravlenie(event, pole_igroka_massiv, pole_igroka_massiv_012, ship_size_global))
            
    def ships_robot():
        
        def vibor_mesta_for_robot(ship_size):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                var = ['up', 'down', 'right', 'left']
                
                if pole_robota_massiv_012[x][y]==1:
                    pole_robota_massiv_012[x][y] = 2
                else:
                    continue
                
                if x-ship_size+1<0:
                    var.remove('up')
                else:
                    for i in range(1, ship_size):
                        if pole_robota_massiv_012[x-i][y]!=1:
                            var.remove('up')
                            break
                if y+ship_size-1>9:
                    var.remove('right')
                else:
                    for i in range(1, ship_size):
                        if pole_robota_massiv_012[x][y+i]!=1:
                            var.remove('right')
                            break
                if x+ship_size-1>9:
                    var.remove('down')
                else:
                    for i in range(1, ship_size):
                        if pole_robota_massiv_012[x+i][y]!=1:
                            var.remove('down')
                            break
                if y-ship_size+1<0:
                    var.remove('left')
                else:
                    for i in range(1, ship_size):
                        if pole_robota_massiv_012[x][y-i]!=1:
                            var.remove('left')
                            break
                
                if len(var)!=0:
                    side = random.choice(var)
                else:
                    pole_robota_massiv_012[x][y] = 1
                    continue
                
                if side == 'up':
                    for i in range(1, ship_size):
                        pole_robota_massiv_012[x-i][y] = 2
                    break
                elif side == 'down':
                    for i in range(1, ship_size):
                        pole_robota_massiv_012[x+i][y] = 2
                    break
                elif side == 'right':
                    for i in range(1, ship_size):
                        pole_robota_massiv_012[x][y+i] = 2
                    break
                elif side == 'left':
                    for i in range(1, ship_size):
                        pole_robota_massiv_012[x][y-i] = 2
                    break                    
            
            for i in range(10):
                for j in range(10):
                    if pole_robota_massiv_012[i][j]!=2:
                        if i-1>=0 and pole_robota_massiv_012[i-1][j]==2:
                            pole_robota_massiv_012[i][j] = 0
                        if i-1>=0 and j+1<=9 and pole_robota_massiv_012[i-1][j+1]==2:
                            pole_robota_massiv_012[i][j] = 0
                        if j+1<=9 and pole_robota_massiv_012[i][j+1]==2:
                            pole_robota_massiv_012[i][j] = 0
                        if i+1<=9 and j+1<=9 and pole_robota_massiv_012[i+1][j+1]==2:
                            pole_robota_massiv_012[i][j] = 0
                        if i+1<=9 and pole_robota_massiv_012[i+1][j]==2:
                            pole_robota_massiv_012[i][j] = 0
                        if i+1<=9 and j-1>=0 and pole_robota_massiv_012[i+1][j-1]==2:
                            pole_robota_massiv_012[i][j] = 0
                        if j-1>=0 and pole_robota_massiv_012[i][j-1]==2:
                            pole_robota_massiv_012[i][j] = 0
                        if i-1>=0 and j-1>=0 and pole_robota_massiv_012[i-1][j-1]==2:
                            pole_robota_massiv_012[i][j] = 0
        
        pole_robota_massiv_012 = [[1]*10 for i in range(10)]
        
        vibor_mesta_for_robot(4)
        for i in range(2):
            vibor_mesta_for_robot(3)
        for i in range(3):
            vibor_mesta_for_robot(2)
        for i in range(4):
            vibor_mesta_for_robot(1)
        
        return pole_robota_massiv_012
    
    def fight(pole_igroka_Frame, pole_robota_massiv_012_for_fight, pole_igroka_massiv_012, variants):
        
        def opredelenie_popadaniia(x, y, atakovannoe_pole, massiv_knopok_atakovannogo_polia, is_this_robot):
            nonlocal popal, ships_is_alive_YOU, ships_is_alive_ROBOT
            
            if atakovannoe_pole[x][y]==0:
                return 0
            
            if atakovannoe_pole[x][y]==1:
                atakovannoe_pole[x][y] = 0
                massiv_knopok_atakovannogo_polia[x][y].config(bg = 'grey', state = tk.DISABLED)
                
                popal = 0
                return 0
                
            elif atakovannoe_pole[x][y]==2:
                atakovannoe_pole[x][y] = 1.5
                massiv_knopok_atakovannogo_polia[x][y].config(bg = 'red', state = tk.DISABLED)
                
                ship_size = [[x, y]]
                kol_proboin = 1
                for i in range(1, 4):
                    if x+i<=9 and atakovannoe_pole[x+i][y] > 1:
                        ship_size.append([x+i, y])
                    else:
                        break
                    if x+i<=9 and atakovannoe_pole[x+i][y] == 1.5:
                        kol_proboin+=1
                for i in range(1, 4):
                    if x-i>=0 and atakovannoe_pole[x-i][y] > 1:
                        ship_size.append([x-i, y])
                    else:
                        break
                    if x-i>=0 and atakovannoe_pole[x-i][y] == 1.5:
                        kol_proboin+=1
                for i in range(1, 4):
                    if y+i<=9 and atakovannoe_pole[x][y+i] > 1:
                        ship_size.append([x, y+i])
                    else:
                        break
                    if y+i<=9 and atakovannoe_pole[x][y+i] == 1.5:
                        kol_proboin+=1
                for i in range(1, 4):
                    if y-i>=0 and atakovannoe_pole[x][y-i] > 1:
                        ship_size.append([x, y-i])
                    else:
                        break
                    if y-i>=0 and atakovannoe_pole[x][y-i] == 1.5:
                        kol_proboin+=1
                
                if len(ship_size) == kol_proboin:
                    ship_is_dead(atakovannoe_pole, ship_size, massiv_knopok_atakovannogo_polia, is_this_robot)
                    if is_this_robot==0:
                        ships_is_alive_ROBOT-=1
                    elif is_this_robot==1:
                        ships_is_alive_YOU-=1
                    if ships_is_alive_ROBOT==0:
                        msg.showinfo('Йо-хо-хо', 'Не верю своему глазу! Вы победили!')
                        window.destroy()
                    elif ships_is_alive_YOU==0:
                        msg.showinfo('Раздался громкий крик', 'За борт его!')
                        msg.showinfo('Поражение', 'Вы умерли')
                        for i in range(10):
                            for j in range(10):
                                if pole_robota_massiv_012_for_fight[i][j] == 2:
                                    pole_robota_massiv[i][j].config(bg = 'purple')
                
                popal = 1
                return 1
        
        def ship_is_dead(pole, ship_size, pole_massiv_knopok, is_this_robot):
            for i in range(10):
                for j in range(10):
                    if pole[i][j] == 1:
                        if i-1>=0 and pole[i-1][j]==1.5 and [i-1, j] in ship_size:
                            pole[i][j] = 0
                            variants.remove([i, j]) if [i, j] in variants and is_this_robot == 1 else None
                            pole_massiv_knopok[i][j].config(bg = 'grey', state = tk.DISABLED)
                            continue
                        if i-1>=0 and j+1<=9 and pole[i-1][j+1]==1.5 and [i-1, j+1] in ship_size:
                            pole[i][j] = 0
                            variants.remove([i, j]) if [i, j] in variants and is_this_robot == 1 else None
                            pole_massiv_knopok[i][j].config(bg = 'grey', state = tk.DISABLED)
                            continue
                        if j+1<=9 and pole[i][j+1]==1.5 and [i, j+1] in ship_size:
                            pole[i][j] = 0
                            variants.remove([i, j]) if [i, j] in variants and is_this_robot == 1 else None
                            pole_massiv_knopok[i][j].config(bg = 'grey', state = tk.DISABLED)
                            continue
                        if i+1<=9 and j+1<=9 and pole[i+1][j+1]==1.5 and [i+1, j+1] in ship_size:
                            pole[i][j] = 0
                            variants.remove([i, j]) if [i, j] in variants and is_this_robot == 1 else None
                            pole_massiv_knopok[i][j].config(bg = 'grey', state = tk.DISABLED)
                            continue
                        if i+1<=9 and pole[i+1][j]==1.5 and [i+1, j] in ship_size:
                            pole[i][j] = 0
                            variants.remove([i, j]) if [i, j] in variants and is_this_robot == 1 else None
                            pole_massiv_knopok[i][j].config(bg = 'grey', state = tk.DISABLED)
                            continue
                        if i+1<=9 and j-1>=0 and pole[i+1][j-1]==1.5 and [i+1, j-1] in ship_size:
                            pole[i][j] = 0
                            variants.remove([i, j]) if [i, j] in variants and is_this_robot == 1 else None
                            pole_massiv_knopok[i][j].config(bg = 'grey', state = tk.DISABLED)
                            continue
                        if j-1>=0 and pole[i][j-1]==1.5 and [i, j-1] in ship_size:
                            pole[i][j] = 0
                            variants.remove([i, j]) if [i, j] in variants and is_this_robot == 1 else None
                            pole_massiv_knopok[i][j].config(bg = 'grey', state = tk.DISABLED)
                            continue
                        if i-1>=0 and j-1>=0 and pole[i-1][j-1]==1.5 and [i-1, j-1] in ship_size:
                            pole[i][j] = 0
                            variants.remove([i, j]) if [i, j] in variants and is_this_robot == 1 else None
                            pole_massiv_knopok[i][j].config(bg = 'grey', state = tk.DISABLED)
                            continue

            for i in range(len(ship_size)):
                pole[ship_size[i][0]][ship_size[i][1]] = 0
        
        def vistrel(x, y):
            nonlocal pole_robota_massiv_012_for_fight, pole_igroka_massiv_012, popal, ships_is_alive_ROBOT, ships_is_alive_YOU
            
            opredelenie_popadaniia(x, y, pole_robota_massiv_012_for_fight, pole_robota_massiv, 0)
            for i in range(10):
                for j in range(10):
                    pole_robota_massiv[i][j].config(state = tk.DISABLED)
            window.after(1000, lambda : vistrel_robota(1))
                
            def vistrel_robota(is_this_first):
                if ships_is_alive_ROBOT == 0 or ships_is_alive_YOU == 0:
                    return 0
                if is_this_first==1:
                    if popal==0:
                        a = random.choice(variants)
                        x = a[0]
                        y = a[1]
                        variants.remove(a)
                        opredelenie_popadaniia(x, y, pole_igroka_massiv_012, pole_igroka_massiv, 1)
                        window.after(1000, lambda : vistrel_robota(0))
                    else:
                        for i in range(10):
                            for j in range(10):
                                if pole_robota_massiv_012_for_fight[i][j]!=0:
                                    pole_robota_massiv[i][j].config(state=tk.NORMAL)
                        return 0
                elif is_this_first==0:
                    if popal==1:
                        a = random.choice(variants)
                        x = a[0]
                        y = a[1]
                        variants.remove(a)
                        opredelenie_popadaniia(x, y, pole_igroka_massiv_012, pole_igroka_massiv, 1)
                        window.after(1000, lambda : vistrel_robota(0))
                    else:
                        for i in range(10):
                            for j in range(10):
                                if pole_robota_massiv_012_for_fight[i][j]!=0:
                                    pole_robota_massiv[i][j].config(state=tk.NORMAL)
                        return 0
                    
        nonlocal kol_ship_1, kol_ship_2, kol_ship_3, kol_ship_4
        
        if kol_ship_1!=0 or kol_ship_2!=0 or kol_ship_3!=0 or kol_ship_4!=0:
            msg.showerror('error', 'Вы расположили не все корабли')
            return 0
        
        knopka_fight.destroy()
        pole_igroka_Frame.destroy()
        
        pole_igroka_Frame = tk.Frame(window)
        pole_igroka_Frame.grid(row = 0, column=0, padx = 100, pady = 50)
        pole_robota_Frame = tk.Frame(window)
        pole_robota_Frame.grid(row = 0, column = 1, padx = 100, pady = 50)
        
        pole_igroka_massiv = pole_igroka_sozdanie(pole_igroka_Frame, 1)
        pole_robota_massiv = pole_robota_sozdanie(pole_robota_Frame, 0)
        
        msg.showinfo('Этап атаки', 'Атакуйте противника')
        popal = -1
        
        for i in range(10):
            for j in range(10):
                if pole_igroka_massiv_012[i][j] == 0:
                    pole_igroka_massiv_012[i][j] = 1
                if pole_igroka_massiv_012[i][j] == 2:
                    pole_igroka_massiv[i][j].config(bg = 'green')
        
        for i in range(10):
            for j in range(10):
                if pole_robota_massiv_012_for_fight[i][j] == 0:
                    pole_robota_massiv_012_for_fight[i][j] = 1
                pole_robota_massiv[i][j].config(command = lambda x=i, y=j : vistrel(x, y))
    
    window.geometry('1600x800')
    window.title('Морской бой')
    knopka_start.destroy()
    label_for_photo.destroy()
    
    kol_ship_1 = 4
    kol_ship_2 = 3
    kol_ship_3 = 2
    kol_ship_4 = 1
    
    ships_is_alive_YOU = 10
    ships_is_alive_ROBOT = 10
    
    pole_igroka_Frame = tk.Frame(window)
    pole_igroka_Frame.grid(row = 0, column=0, padx = 100, pady = 50)

    pole_igroka_massiv = pole_igroka_sozdanie(pole_igroka_Frame, 1)
    pole_igroka_massiv_012 = [[1]*10 for i in range(10)]
    ships_igrok(pole_igroka_massiv)
    pole_robota_massiv_012_for_fight = ships_robot()
    
    variants = []
    for i in range(10):
        for j in range(10):
            variants.append([i, j])
            
    msg.showinfo('Этап расстановки', 'Расставьте ваши корабли')

    knopka_fight = tk.Button(window, text = 'Начать бой', font = ('Times New Roman', 20), bg = 'green', command = lambda : fight(pole_igroka_Frame, pole_robota_massiv_012_for_fight, pole_igroka_massiv_012, variants))
    knopka_fight.grid(row = 1, column = 0, columnspan = 2, pady = 20)

window = tk.Tk()
window.title('Добро пожаловать')
window.geometry('800x450')

img = Image.open('img_for_rgz/hello.webp')
img = img.resize((800, 350))
photo = ImageTk.PhotoImage(img)
label_for_photo = tk.Label(window, image = photo)
label_for_photo.grid(row = 0, column=0, columnspan=2)

knopka_start = tk.Button(window, text = 'Старт', font = ('Times New Roman', 20), bg = 'green', command=start)
knopka_start.grid(row = 1, column=0, columnspan=2, pady = 20)

window.mainloop()