#!/bin/usr/env python3
#verion 0.3.2
#Програма для перемещения файлов по расширению из исходной папки(src) в папку назначения(dst) 


import tkinter as tk
from model import InformMenu,HelpMenu, winlin, exit_prog,main
 

__version = "0.3."



# Главное окно
root = tk.Tk()
root.title('Сортировка файлов по расширению')
root.geometry('700x600+200+100')


# Поля
ent_src = tk.Entry(root, width=70 ) #Поле ввода исходного каталога
ent_dst = tk.Entry(root, width=70 ) #Поле ввода  каталога назначения
ent_expancion = tk.Entry(root, width=70) #Поле ввода расширения
ent_dst_title = tk.Label(root, text='Введите абсолютный путь к каталогу назначения:')
ent_src_title = tk.Label(root, text='Введите абсолютный путь к исходному каталогу:')
ent_expansion_title = tk.Label(root, text='Введите расширения файла, например - (.txt) или " * " что бы выбрать все файлы: ')



# Инициализация
ent_src_title.grid(column=0, row=2, padx=10, sticky=tk.W)
ent_src.grid(column=0, row=3, padx=10, sticky=tk.W)
ent_dst_title.grid(column=0, row=4, padx=10, sticky=tk.W)
ent_dst.grid(column=0, row=5, padx=10, sticky=tk.W)
ent_expansion_title.grid(column=0, row=6, padx=10, sticky=tk.W)
ent_expancion.grid(column=0, row=7, padx=10, sticky=tk.W)



#Pack
mainmenu = tk.Menu(root) 
root.config(menu=mainmenu) 
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть", command= open)
filemenu.add_command(label="Узнать расширение", command = InformMenu.show_expancion(tk))
filemenu.add_command(label="win/lin/mack", command = winlin)
filemenu.add_command(label="Выход", command = exit_prog)
helpmenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu )



helpmenu.add_command(label="О программе", command=HelpMenu.about_prog(__version, tk))
helpmenu.add_command(label="Помощь", command = HelpMenu.help_user(tk))
but = tk.Button(root, text="Старт",bg="lightgreen" , command=main )
but.config(width=9, height=2, padx=10, pady=10)
but.place(x=580, y=20)



root.mainloop()
