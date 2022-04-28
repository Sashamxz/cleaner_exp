from tkinter import messagebox as mb


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.but.config(command=self.model.main )
    

    def cleans(self, ent_dst, ent_src, ent_expancion):
        self.model.main()