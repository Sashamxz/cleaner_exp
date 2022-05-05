import tkinter as tk


version = "1.4.3"


class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

        # поля ввода
        self.ent_dst_title = tk.Label(
            self, text='Введите абсолютный путь к каталогу назначения:')
        self.ent_src_title = tk.Label(
            self, text='Введите абсолютный путь к исходному каталогу:')
        self.ent_expansion_title = tk.Label(
            self,
            text='Введите расширения файла, например - (.txt) или " * " что бы выбрать все файлы: ')


        # поля entry
        self.ent_src = tk.Entry(self, width=67)  # Поле ввода исходного каталога
        self.chose_src = tk.Button(
            self, text='...', command=lambda: [
                self.ent_src.delete(
                    '1', tk.END), self.ent_src.insert(
                    0, self.file_folder())])
        self.chose_src.config(width=1, height=1)
        self.ent_dst = tk.Entry(self, width=67) # Поле ввода  каталога назначения
        self.chose_dst = tk.Button(
            self, text='...', command=lambda: [
                self.ent_dst.delete(
                    '1', tk.END), self.ent_dst.insert(
                    0, self.file_folder())])
        self.chose_dst.config(width=1, height=1)
        self.ent_expancion = tk.Entry(self, width=67)  # Поле ввода расширения
        self.ent_expancion.insert(0, '.txt')


        # кнопка старт
        self.butt_start = tk.Button(self, text=" Старт ", bg="lightgreen")
        self.butt_start.config(width=3, height=2)


        # расположение
        self.ent_src_title.grid(column=0, row=2, padx=5, sticky=tk.W)
        self.ent_src.grid(column=0, row=3, padx=5, sticky=tk.W)
        self.chose_src.grid(column=0, row=3, sticky=tk.E)
        self.ent_dst_title.grid(column=0, row=4, padx=5, sticky=tk.W)
        self.ent_dst.grid(column=0, row=5, padx=5, sticky=tk.W)
        self.chose_dst.grid(column=0, row=5, sticky=tk.E)
        self.ent_expansion_title.grid(column=0, row=6, padx=5, sticky=tk.W)
        self.ent_expancion.grid(column=0, row=7, padx=5, sticky=tk.W)
        self.butt_start.grid(column=1, row=7, sticky=tk.E)

        # set the controller
        self.controller = None


    def initUI(self):
        mainmenu = tk.Menu(self.parent)
        self.parent.config(menu=mainmenu)
        self.filemenu = tk.Menu(mainmenu, tearoff=0)
        self.helpmenu = tk.Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="Файл", menu=self.filemenu)
        mainmenu.add_cascade(label="Справка", menu=self.helpmenu)


    @classmethod
    def file_folder(cls):
        cls.folder = tk.filedialog.askdirectory()
        return cls.folder

    def field_num(self):
        numb = {self.ent_src: 1,
                self.ent_dst: 2,
                self.ent_expancion: 3
                }
        return numb


    def set_controller(self, controller):
        """
        установка контроллера

        """
        self.controller = controller

    def start_button_clicked(self):
        """
        обработчик нажатий
        :return:
        """
        if self.controller:
            self.controller.main()




class ExpancionFile(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title('Определить расширение файла')
        window_text = tk.Label(
            self, text='Выберите файл чтобы узнать его расширение')
        window_text.pack(side=tk.TOP, pady=5, padx=5)
        self.button_sel = tk.Button(self, text='Browse')
        self.geometry('400x400')
        var = tk.StringVar()
        self.ent = tk.Entry(self, textvariable=var)
        self.ent.pack(side=tk.LEFT, pady=5, padx=5)
        self.button_sel.pack(side=tk.LEFT, pady=5, ipadx=2, ipady=2)


class Helpt(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.about_prog
        self.help_user
        self.version = version


    # окно помощи пользователю
    def help_user(self):
        self.title('Help')
        self.geometry('550x300')
        about = '''
        Абсолютный путь очень точно показывает где именно находится \n
        файл, а относительный должен иметь обязательную привязку к какой-либо \n
        отправной точкe, относительно которой и укзывается путь. \n
        Например у нас есть картинка file.png на диске D:\\,  Абсолютный \n
        путь к ней будет D:\\picture\\file.png, а относительно корневого \n
        каталога можно указывать \\picture\\file.png '''
        text_help = tk.Label(self, justify=tk.LEFT, text=about)
        text_help.pack(side=tk.LEFT, expand=True, padx=10, pady=10)
        self.about_prog



    # о програме + версия
    def about_prog(self):
        self.geometry('600x400')
        self.title('About')
        about = 'Cleaner expansion-програма для сортировки файлов по рассширению \n  Version - %s' % (
            self.version)
        text_help = tk.Label(self, text=about)
        text_help.pack(side=tk.LEFT, expand=True, padx=10, pady=10)
