from tkinter import messagebox as mb
from view import Helpt

class Controller:
    def __init__(self, model, view, expanc_file):
        self.model = model
        self.view = view
        self.expanc_file = expanc_file
        self.helpt = Helpt
        self.view.butt_start.config(command=self.model.main)
        self.view.filemenu.add_command(label="Открыть", command= self.model.open_file)
        self.view.filemenu.add_command(label="Узнать расширение", command = self.open_window_file)
        self.view.filemenu.add_command(label="win/lin/mack", command = self.model.winlin)
        self.view.filemenu.add_command(label="Выход", command = self.model.exit_prog)
        self.view.helpmenu.add_command(label="Помощь", command = self.open_help)
        self.view.helpmenu.add_command(label="О программе", command=self.open_about_prog)
        
    #открывает окно для определения расширения файла 
    def open_window_file(self):
        window = self.expanc_file(self.view)
        window.button_sel.config(command = self.model.file_expancion)
        return window

    #открывает окно помощи 
    def open_help(self):
        window_h = self.helpt(self.view)
        window_h.help_user()
        return window_h

    # о програме 
    def open_about_prog(self):
        window_a = self.helpt(self.view)
        window_a.about_prog()   
        return window_a 