#!/bin/usr/env python3
#verion 0.2.9
#Програма для перемещения файлов по расширению из исходной папки(src) в папку назначения(dst) 

import os
import sys
import time
import logging
import shutil
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename
from logging import FileHandler


__version = "0.3.2"


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


#Логирование
logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format = FORMAT, level=logging.INFO, filename = 'log.txt' ) 



#Получаем данные от пользователя 
def get_addr(ent_adr):
    if len(ent_adr.get()) == 0:
        mb.showerror('warning',
                     f'Поле {ent_adr} не должно быть пустым')
        while True:
            break

    else:
        ent_adr = ent_adr.get()
        return ent_adr



#Декоратор для передачи данных в функцию сортировки 
def take_data(func):   
    def wrapper():    
        src_adr = get_addr(ent_src)
        dts_adr = get_addr(ent_dst)
        expancion_adr = get_addr(ent_expancion)
        func(src_adr,dts_adr,expancion_adr)
        
    return wrapper

# # получаем адрес исходной папки и сохраняем в !src_adr!
# def my_src():
#     if len(ent_src.get()) == 0:
#         mb.showerror('warning',
#                      'Поле 1 не должно быть пустым')
        
#     else:
#         src_adr = ent_src.get()
#         return src_adr


# # получаем адрес назначения и сохраняем в !dts_adr!
# def my_dts():
#     if len(ent_dst.get()) == 0:
#         mb.showerror('warning',
#                      'Поле 2 не должно быть пустым')
#     else:
#         dst_adr = ent_dst.get()
#         return dst_adr


# # получаем расширение назначения и сохраняем в !expancion_adr!
# def expancion():
#     if len(ent_expancion.get()) == 0:
#         mb.showerror('warning',
#                      'Поле 3 не должно быть пустым') 
#     else:
#         expancion_adr = ent_expancion.get()
#         return expancion_adr


# Функция сортировки  файлов
@take_data
def cleaner(src_adr,dst_adr,expancion_adr):
    os.chdir(src_adr)
    path_file = os.listdir(src_adr) #список файлов
    for _file in path_file:
        if _file.endswith(expancion_adr) and os.path.abspath(_file) != dst_adr: # выбираем  фалы по расширению,!=dst
            shutil.move(os.path.abspath(_file), dst_adr)
            logging.info('file -%s    moved || from --- %s || to--- %s' %(_file,src_adr,dst_adr))
            
        elif expancion_adr == '*' and os.path.abspath(_file) != dst_adr:
            shutil.move(os.path.abspath(_file), dst_adr)
            logging.info('file -%s    moved || from --- %s || to--- %s' %(_file,src_adr,dst_adr))
                 

# Вызываем функции и передаем  результат
def main():
    try:
        
        cleaner()
        mb.showinfo('Perfect', 'All files moved! \n \
                  \n See "log.txt" for details ')
        return 1
    except Exception as ex:
        mb.showerror('error', ex)
        return 0
    




###########Дополнительный функционал###########:

#Определить расширение файла 

def show_expancion():
    window = tk.Toplevel()
    window.geometry('400x400')
    window.title('Определить расширение файла')
    var = tk.StringVar
    window_text=tk.Label(window,text='Выберите файл чтобы узнать его расширение' )
    
    def _file_expancion():
        fiel_exp = askopenfilename()
        if len(fiel_exp) > 0:
            _expancion = fiel_exp.rpartition('.')[-1]
            mb.showinfo(title='Расширение файла', 
                    message= (' - .%s  ' %(_expancion)))  
        else:
            pass
        
    
    ent = tk.Entry(window, textvariable=var)
    back = tk.Button(window, text="Browse",command = _file_expancion)
    window_text.pack(side=tk.TOP, pady=5, padx=5 )
    ent.pack(side=tk.TOP, pady=5, padx=5 )
    back.pack(side=tk.TOP, pady=10)


#Меню/выход
def exit_prog():
    sys.exit()         


#Определеяем ОС
def winlin():
    platformf = sys.platform
    if platformf == "linux" or platformf == "linux2" :
        mb.showinfo("OS", "Linux :)")   # linux
    
    elif platformf == "darwin":
        mb.showinfo("OS", "macOS")    # OS X
    
    elif platformf == "win32":
        mb.showinfo("OS", "Windows...") # Windows...



#Pack
mainmenu = tk.Menu(root) 
root.config(menu=mainmenu) 
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть", command= open)
filemenu.add_command(label="Узнать расширение", command = show_expancion )
filemenu.add_command(label="win/lin/mack", command = winlin)
filemenu.add_command(label="Выход", command = exit_prog)
helpmenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu )

def open():
    sys.version



def help_user():
    window = tk.Toplevel()
    window.geometry('600x400')
    window.title('Help')
    about = '''Абсолютный путь очень точно показывает где именно находится \n
    файл, а относительный должен иметь обязательную привязку к какой-либо \n
    отправной точкe, относительно которой и укзывается путь. \n
    Например у нас есть картинка file.png на диске D:\\,  Абсолютный \n
    путь к ней будет D:\\picture\\file.png, а относительно корневого \n
    каталога можно указывать \\picture\\file.png '''
    text_help = tk.Label(window ,text=about)
    text_help.pack(side=tk.LEFT, expand=True,padx=10, pady=10)
    window.mainloop()


def about_prog():
    window = tk.Toplevel()
    window.geometry('600x400')
    window.title('About')
    about = 'Cleaner expansion-програма для сортировки файлов по рассширению \n  Version - %s'  %(__version)
    text_help = tk.Label(window ,text=about)
    text_help.pack(side=tk.LEFT, expand=True,padx=10, pady=10)
    window.mainloop()

helpmenu.add_command(label="О программе", command=about_prog)
helpmenu.add_command(label="Помощь", command = help_user)
but = tk.Button(root, text="Старт",bg="lightgreen" , command=main )
but.config(width=9, height=2, padx=10, pady=10)
but.place(x=580, y=20)



root.mainloop()
