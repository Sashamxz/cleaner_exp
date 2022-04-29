import tkinter as tk
from model import Model
from view import View
from controller import Controller



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title('Сортировка файлов по расширению')
        self.root.geometry('700x600+200+100')

       
        # create a view and place it on the root window
        view = View(self.root)
        view.grid(row=0, column=0, padx=10, pady=10)     
        
        # create a model
        model = Model(view.ent_src, view.ent_dst, view.ent_expancion)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()