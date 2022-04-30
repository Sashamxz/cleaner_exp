from tkinter import messagebox as mb


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.but.config(command=self.model.main )
        self.view.but.config(command=self.model.exit_prog)
        self.view.show_expanc.back.config(command = self.model.file_expancion)
        self.view.filemenu.add_command(label="Открыть", command= self.model.open_file)
        self.view.filemenu.add_command(label="Узнать расширение", command = self.view.show_expanc)
        self.view.filemenu.add_command(label="win/lin/mack", command = self.model.winlin)
        self.view.filemenu.add_command(label="Выход", command = self.model.exit_prog)
        self.view.helpmenu.add_command(label="Помощь", command = self.model.help_user)
        self.view.helpmenu.add_command(label="О программе", command=self.model.about_prog)
       
        # self.mainmenu.add_command(label='Файл')
        # self.mainmenu.add_command(label='Справка')   

    # def cleans(self, ent_dst, ent_src, ent_expancion):
    #     self.model.main()