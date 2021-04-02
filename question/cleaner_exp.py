
import os, sys, shutil, glob, time, re
from sys import argv
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.title("Сортировка файлов по расширению")
root.geometry('600x500+200+100')

# Поля
ent_src = tk.Entry(root, width=60 )
ent_dst = tk.Entry(root, width=60 )
ent_expancion = tk.Entry(root, width=20)

ent_dst_title = tk.Label(root, text='Введите абсолютный путь к папке назначения:')
ent_src_title = tk.Label(root, text='Введите абсолютный путь к исходному каталогу:')
ent_expansion_title = tk.Label(root, text='Введите расширения файла, например - .txt : ')

# Инициализация
ent_src_title.pack(fill= tk.BOTH)
ent_src.pack(fill=tk.BOTH, padx=10)
ent_dst_title.pack()
ent_dst.pack(fill= tk.BOTH, padx=10)
ent_expansion_title.pack(pady =1, padx=1)
ent_expancion.pack( pady =5, padx=5)




# получаем адрес исходной папки и сохраняем в !src_adr!
def my_src():
    if len(ent_src.get()) == 0:
        mb.showerror('warning',
                     'Поле 1 не должно быть пустым')
                     
    else:
        src_adr = ent_src.get()
        return src_adr


# получаем адрес назначения и сохраняем в !dts_adr!
def my_dts():
    if len(ent_dst.get()) == 0:
        mb.showerror('warning',
                     'Поле 2 не должно быть пустым')

    else:
        dst_adr = ent_dst.get()
        return dst_adr


# получаем расширение назначения и сохраняем в !expancion_adr!
def expancion():
    if len(ent_expancion.get()) == 0:
        mb.showerror('warning',
                     'Поле 3 не должно быть пустым')
    else:
        expancion_adr = ent_expancion.get()
        return expancion_adr





# Сортировщик  файлов
def cleaner(src_adr, dst_adr, expancion_adr):
    os.chdir(src_adr)
    path_file = os.listdir(src_adr)
    for file in path_file:
        if file.endswith(expancion_adr) and os.path.abspath(file) != dst_adr: # перебираем фалы по расширению 
            shutil.move(os.path.abspath(file), dst_adr)
            print('succeful')
            print('file moved --- %s' % file)
            
# Вызываем функции и передаем  результат

def main():
    try:
        cleaner(my_src(), my_dts(), expancion())
        mb.showinfo("Perfect", "All files moved!" )
        return 1
    except Exception as ex:
        mb.showerror("error", ex)
        return 0
    

# Дополнительный функционал
def exit_prog():
    sys.exit()                  

#Определить расширение файла 
def show_expancion():
    window = tk.Toplevel()
    window.geometry('400x400')
    window.title('Определить расширение файла')
    var = tk.StringVar
    
    def _file_expancion():
        fiel_exp = askopenfilename()
        _expancion = fiel_exp.rpartition('.')[-1] 
        mb.showinfo(title='Расширение файла', 
                    message= (' - .%s  ' %(_expancion)))  
        
        
    
    ent = tk.Entry(window, textvariable=var)
    back = tk.Button(window, text="Browse",command = _file_expancion)
     
    ent.pack(side=tk.TOP, pady =5, padx=5 )
    back.pack(side=tk.TOP, pady=10)

    

mainmenu = tk.Menu(root) 
root.config(menu=mainmenu) 
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Узнать расширение", command = show_expancion )
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход", command = exit_prog)

helpmenu = tk.Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="О программе")
mainmenu.add_cascade(label="Файл",
                     menu=filemenu)
mainmenu.add_cascade(label="Справка",
                     menu=helpmenu )





def help_user():
    window = tk.Toplevel()
    window.geometry('500x400')
    window.title('Help')
    
    about = '''Абсолютный путь очень точно показывает где именно находится \n
    файл, а относительный должен иметь обязательную привязку к какой-либо \n
    отправной точкe, относительно которой и укзывается путь. \n
    Например у нас есть картинка file.png на диске D:\,  Абсолютный \n
    путь к ней будет D:\picture\\file.png, а относительно корневого \n
    каталога можно указывать \picture\\file.png '''
    
    text_help = tk.Label(window ,text=about)
    text_help.pack(side=tk.LEFT, expand=True, pady=10)
    window.mainloop()

helpmenu.add_command(label="Помощь", command = help_user)
but = tk.Button(root, text="Старт",bg="lightblue" , command=main )
but.config(width=11, height=2)
but.place(x=500, y=50)
but.pack()
root.mainloop()
