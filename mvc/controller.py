from tkinter import messagebox as mb

class Controller:
    def __init__(self, model, view, about):
        self.model = model
        self.view = view
        self.about = about
        self.view.butt_start.config(command=self.model.main)
        self.view.filemenu.add_command(label="Открыть", command= self.model.open_file)
        self.view.filemenu.add_command(label="Узнать расширение", command = self.open_window)
        self.view.filemenu.add_command(label="win/lin/mack", command = self.model.winlin)
        self.view.filemenu.add_command(label="Выход", command = self.model.exit_prog)
        self.view.helpmenu.add_command(label="Помощь", command = self.model.help_user)
        self.view.helpmenu.add_command(label="О программе", command=self.model.about_prog)
        
    
    def open_window(self):
        window = self.about(self.view)
        window.button_sel.config(command = self.model.file_expancion)
        return window

   