from tkinter import messagebox as mb


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    

    def main(self):
        try:
            self.cleaner()
            mb.showinfo('Perfect', 'All files moved! \n \
                    \n See "log.txt" for details ')
            return 1
        except Exception as ex:
            mb.showerror('error', ex)
            return 0    