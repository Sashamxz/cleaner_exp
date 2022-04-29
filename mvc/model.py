import os
import sys
import shutil
import logging
from logging import FileHandler
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename


logger = logging.getLogger(__name__)
FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, filename = 'log.txt' ) 
__version = "0.3.2"


class Model:
    def __init__(self, ent_src, ent_dst, ent_expancion):
        self.ent_src = ent_src
        self.ent_dst = ent_dst
        self.ent_expancion = ent_expancion

   



    def get_addr(self,ent_adr):
        self.ent_adr = ent_adr
        if len(self.ent_adr.get()) == 0:
            mb.showerror('warning',
                        f'Поле {ent_adr} не должно быть пустым')
            raise Exception(' Confirm your entries ')

        else:
            self.ent_adr = ent_adr.get()
            return self.ent_adr


            
    #Декоратор для передачи данных в функцию сортировки 
    
    def take_data(func):   
        def wrapper(self, *args, **kwargs):    
            src_adr = self.get_addr(self.ent_src)
            dts_adr = self.get_addr(self.ent_dst)
            expancion_adr = self.get_addr(self.ent_expancion)
            func(self, src_adr,dts_adr,expancion_adr)
            
        return wrapper

    
    # Функция сортировки  файлов
    @take_data
    def cleaner(self,src_adr,dst_adr,expancion_adr):
        os.chdir(src_adr)
        path_file = os.listdir(src_adr) #список файлов
        for _file in path_file:
            if _file.endswith(expancion_adr) and os.path.abspath(_file) != dst_adr: # выбираем  фалы по расширению,!=dst
                shutil.move(os.path.abspath(_file), dst_adr)
                logging.info('file - %s    moved || from --> %s || to--> %s' %(_file,src_adr,dst_adr))
                
            elif expancion_adr == '*' and os.path.abspath(_file) != dst_adr:
                shutil.move(os.path.abspath(_file), dst_adr)
                logging.info('file - %s    moved || from --> %s || to--> %s' %(_file,src_adr,dst_adr))
                    

    # Вызываем функции и передаем  результат
    def main(self):
        try:
            self.cleaner()
            mb.showinfo('Perfect', 'All files moved! \n \
                    \n See "log.txt" for details ')
            return 1
        except Exception as ex:
            mb.showerror('error', ex)
            return 0    

    ###########Дополнительный функционал###########:

    #Определить расширение файла 

    def show_expancion(self):
        def _file_expancion():
            fiel_exp = askopenfilename()
            if len(fiel_exp) > 0:
                _expancion = fiel_exp.rpartition('.')[-1]
                mb.showinfo(title='Расширение файла', 
                        message= (' - .%s  ' %(_expancion)))  
            else:
                pass
        



    #Меню/выход
    def exit_prog(self):
        sys.exit()         


    #Определеяем ОС
    def winlin(self):
        platformf = sys.platform
        if platformf == "linux" or platformf == "linux2" :
            mb.showinfo("OS", "Linux :)")   # linux
        
        elif platformf == "darwin":
            mb.showinfo("OS", "macOS")    # OS X
        
        elif platformf == "win32":
            mb.showinfo("OS", "Windows...") # Windows...        