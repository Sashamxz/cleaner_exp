import os
import sys
import logging
import shutil
from logging import FileHandler
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb




#Логирование перемещения файлов
logger = logging.getLogger(__name__)
FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, filename = 'log.txt' ) 




#Получаем данные от пользователя (исходный путь , назначения, расширения)
def get_addr(ent_adr):
    if len(ent_adr.get()) == 0:
        mb.showerror('warning',
                     f'Поле {ent_adr} не должно быть пустым')
        

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


# Функция сортировки  файлов
@take_data
def cleaner(src_adr,dst_adr,expancion_adr):
    os.chdir(src_adr)
    path_file = os.listdir(src_adr) #список файлов
    for _file in path_file:
        if _file.endswith(expancion_adr) and os.path.abspath(_file) != dst_adr: # выбираем  фалы по расширению,!=dst
            shutil.move(os.path.abspath(_file), dst_adr)
            logging.info('file - %s    moved || from --- %s || to--- %s' %(_file,src_adr,dst_adr))
            
        elif expancion_adr == '*' and os.path.abspath(_file) != dst_adr:
            shutil.move(os.path.abspath(_file), dst_adr)
            logging.info('file - %s    moved || from --- %s || to--- %s' %(_file,src_adr,dst_adr))
                 


# Вызываем функции и передаем  результат работы в лог файл
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
class InformMenu():
    def show_expancion(tk):
        if __name__ == "__main__":
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



def open():
    sys.version

class HelpMenu(InformMenu):
    def help_user(tk):
        window = tk.Toplevel()
        window.geometry('600x400')
        window.columnconfigure(0, minsize=130)
        window.title('Help')
        about = ('''Абсолютный путь очень точно показывает где именно находится \n
        файл, а относительный должен иметь обязательную привязку к какой-либо \n
        отправной точкe, относительно которой и укзывается путь. \n
        Например у нас есть картинка file.png на диске D:\\,  Абсолютный \n
        путь к ней будет D:\\picture\\file.png, а относительно корневого \n
        каталога можно указывать \\picture\\file.png ''')
    
        text_help = tk.Label(window ,text=about)
        text_help.pack(side=tk.LEFT, expand=True,padx=10, pady=10)
        if __name__ == "__main__":  
            window.mainloop()


    def about_prog(__version, tk):
        window = tk.Toplevel()
        window.geometry('600x400')
        window.title('About')
        about = 'Cleaner expansion-програма для сортировки файлов по рассширению \n  Version - %s'  %(__version)
        text_help = tk.Label(window ,text=about)
        text_help.pack(side=tk.LEFT, expand=True,padx=10, pady=10)
        if __name__ == "__main__":
            window.mainloop()