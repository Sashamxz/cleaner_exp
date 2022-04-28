import tkinter as tk
from model import Model
from view import View
from controller import Controller



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Сортировка файлов по расширению')
        self.geometry('700x600+200+100')

        # create a model
        model = Model(self,ent_dst, ent_src, ent_expancion)

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()