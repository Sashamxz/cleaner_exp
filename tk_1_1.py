import tkinter as tk
from abc import ABC
from tkinter import messagebox as mb
import os, sys, shutil, glob, abc
from sys import argv


root = tk.Tk()
root.title("Сортировка файлов по расширению")
root.geometry('600x500+200+100')


class Touch:
    """Клас принимает данные от пользователя
    Абмтрактный клас
    """

    def __init__(self, afr):
        self.atr = afr
        pass

    @abc.abstractmethod
    def get_path(self):
        pass


class Touch_src(Touch):
    # получаем адрес исходной папки и сохраняем в ! src_adr!
    def get_path(ent_src):
        # self.src_adr = ent_src()
        if len(ent_src.get()) == 0:
            mb.showerror('ERROR',
                         'Поле 1 не должно быть пустым')
        else:
            src_adr = ent_src.get()
            return src_adr


# получаем адрес назначения и сохраняем в !dts_adr!
class Touch_dst(Touch):
    def get_path(ent_dst):
        # self.dts_adr = ent_dst.get()
        if len(ent_dst.get()) == 0:
            mb.showerror('ERROR',
                         'Поле 2 не должно быть пустым')
        else:
            dts_adr = ent_dst.get()
            return dts_adr


# получаем расширение назначения и сохраняем в !expancion_adr!
class Touch_expansion(Touch):

    def get_path(ent_expaimcions):
        # self.expansion_adr = ent_expancions.get()
        if len(ent_expancions.get()) == 0:
            mb.showerror('ERROR',
                         'Поле 3 не должно быть пустым')
        else:
            expancion_adr = ent_expancions.get()
            return expancion_adr


#Функционал
class Cleaner(Touch):
    def cleaner(self,get_path,dst_adr,expancion_adr):
        self.
        get_path = dst_adr
        self.ent_src = src_adr
        self.expancions = expancion_adr
        os.chdir(src_adr)
        path_file = os.listdir(src_adr)
        for file in path_file:
            if file.endswith(expancion_adr) and os.path.abspath(file) != ent_dst:
                #print(os.path.abspath(file))
                shutil.move(os.path.abspath(file), dst_adr)
                print('file moved --- %s' % file)


# Вызываем функции и охраняем получаный результат
def main():
    try:
        Touch_src.get_path(ent_src)
        Touch_dst.get_path(ent_dst)
        Touch_expansion.get_path(ent_expancions)
        Cleaner.cleaner()
    except Exception as ex:
        mb.showerror("error", ex)


# Поля
ent_src = tk.Entry(root, width=60)
ent_dst = tk.Entry(root, width=60)
ent_expancions = tk.Entry(root, width=20)
but = tk.Button(root, text="Старт", command=main)
but.config(width=11, height=2)
ent_dst_title = tk.Label(root, text='Введите адрес папки назначения')
ent_src_title = tk.Label(root, text='Введите путь к исходному каталогу')
ent_expansions = tk.Label(root, text='Введите расширения файла, например - .txt ')

# Инициализация
ent_src_title.pack()
ent_src.pack()
ent_dst_title.pack()
ent_dst.pack()
ent_expansions.pack()
ent_expancions.pack()
but.place(x=500, y=50)

root.mainloop()
