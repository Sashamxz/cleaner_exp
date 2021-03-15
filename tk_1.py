import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import os, sys, shutil, glob
from sys import argv

root = tk.Tk()
root.title("Сортировка файлов по расширению")
root.geometry('600x500+200+100')





#получаем адрес исходной папки и сохраняем в ! src_adr!
def my_src():
    if len(ent_src.get()) == 0: 
        mb.showerror('ERROR',
            'Поле 1 не должно быть пустым')
    else:
        src_adr = ent_src.get() 
        return(src_adr)
    
#получаем адрес назначения и сохраняем в !dts_adr!
def my_dts():
    if len(ent_dst.get()) == 0: 
        mb.showerror('ERROR',
            'Поле 2 не должно быть пустым')
    else:
        dts_adr = ent_dst.get() 
        return(dts_adr)

#получаем расширение назначения и сохраняем в !expancion_adr!
def expancion():
    if len(expancions_touch.get()) == 0: 
        mb.showerror('ERROR',
            'Поле 3 не должно быть пустым')
    else:
        expancion_adr = expancions_touch.get() 
        return(expancion_adr)



#Вызываем функции и охраняем получаный результат 

def open_folder():
    try:
        my_src()
        my_dts()
        expancion()
        
    except Exception as ex:
        mb.showerror("error",ex)
    

def main():
    cleaner(open_folder)

#Функционал
def cleaner(open_folder):
    os.chdir(src_adr)
    path_file = os.listdir(src_adr)
    for file in path_file:
        if file.endswith(expancion_adr) and os.path.abspath(file) != dts_adr:
            #print(os.path.abspath(file))
            shutil.move(os.path.abspath(file), dts_adr)
            print('file moved --- %s' % file)
    

#Поля
ent_src = tk.Entry(root, width=60)
ent_dst = tk.Entry(root, width=60)
expancions_touch = tk.Entry(root, width = 20)
but = tk.Button(root,  text="Старт", command = main)
but.config( width= 11, height = 2)
ent_dst_title = tk.Label (root, text = 'Введите адрес папки назначения') 
ent_src_title = tk.Label (root, text = 'Введите путь к исходному каталогу') 
ent_expansions = tk.Label(root, text = 'Введите расширения файла, например - .txt ')


#Инициализация
ent_src_title.pack()
ent_src.pack()
ent_dst_title.pack()
ent_dst.pack()
ent_expansions.pack()
expancions_touch.pack()
but.place(x=500, y=50)



root.mainloop()


