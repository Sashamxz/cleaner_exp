import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import os, sys, shutil, glob
from sys import argv

root = tk.Tk()
root.title("Сортировка файлов по расширению")
root.geometry('600x500+200+100')

# Поля
ent_src = tk.Entry(root, width=60)
ent_dst = tk.Entry(root, width=60)
ent_expancion = tk.Entry(root, width=20)

ent_dst_title = tk.Label(root, text='Введите адрес папки назначения')
ent_src_title = tk.Label(root, text='Введите путь к исходному каталогу')
ent_expansion_title = tk.Label(root, text='Введите расширения файла, например - .txt ')

# Инициализация
ent_src_title.pack()
ent_src.pack()
ent_dst_title.pack()
ent_dst.pack()
ent_expansion_title.pack()
ent_expancion.pack()




# получаем адрес исходной папки и сохраняем в ! src_adr!
def my_src():
    if len(ent_src.get()) == 0:
        mb.showerror('ERROR',
                     'Поле 1 не должно быть пустым')
    else:
        src_adr = ent_src.get()
        return src_adr


# получаем адрес назначения и сохраняем в !dts_adr!
def my_dts():
    if len(ent_dst.get()) == 0:
        mb.showerror('ERROR',
                     'Поле 2 не должно быть пустым')

    else:
        dst_adr = ent_dst.get()
        return dst_adr


# получаем расширение назначения и сохраняем в !expancion_adr!
def expancion():
    if len(ent_expancion.get()) == 0:
        mb.showerror('ERROR',
                     'Поле 3 не должно быть пустым')
    else:
        expancion_adr = ent_expancion.get()
        return expancion_adr


# Вызываем функции и передаем получаный результат

def main():
    try:
        # my_src()
        # my_dts()
        # expancion()
        cleaner(my_src(), my_dts(), expancion())
    except Exception as ex:
        mb.showerror("error", ex)


# Функционал
def cleaner(src_adr, dst_adr, expancion_adr):
    os.chdir(src_adr)
    path_file = os.listdir(src_adr)
    for file in path_file:
        if file.endswith(expancion_adr) and os.path.abspath(file) != dst_adr:
            # print(os.path.abspath(file))
            shutil.move(os.path.abspath(file), dst_adr)
            print(" ")
            print('file moved --- %s' % file)


but = tk.Button(root, text="Старт", command=main)
but.config(width=11, height=2)
but.place(x=500, y=50)
but.pack()
root.mainloop()
