import re
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pattern = re.compile("^\w{0,10}$")
        self.label = tk.Label(self, text="Введите логин")
        vcmd = (self.register(self.validate_username), "%i", "%P")
        self.entry = tk.Entry(self, validate="key",
                              validatecommand=vcmd,
                              invalidcommand=self.print_error)
        self.label.pack()
        self.entry.pack(anchor=tk.W, padx=10, pady=10)

    def validate_username(self, index, username):
        print("Проверка символа" + index)
        return self.pattern.match(username) is not None

    def print_error(self):
        print("Запрещенный символ в логине")

if __name__ == "__main__":
    app = App()
    app.mainloop()