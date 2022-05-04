import tkinter as tk
from model import Model
from view import View, ExpancionFile
from controller import Controller



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Сортировка файлов по расширению')
        self.geometry('700x600')
        
        # создание окна и расположения
        view = View(self)
        view.grid(row=0, column=0, padx=5, pady=5)     
        expansc_file = ExpancionFile
        
        # создание модели
        model = Model(view.ent_src, view.ent_dst, view.ent_expancion, view.field_num)
        
        # создание контроллера 
        controller = Controller(model, view, expansc_file)

        # установка контролерра в отображении 
        view.set_controller(controller)

    


if __name__ == '__main__':
    app = App()
    app.mainloop()