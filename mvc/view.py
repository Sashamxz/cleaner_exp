import tkinter as tk
from tkinter import ttk


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.ent_dst_title = ttk.Label(self, text='Введите абсолютный путь к каталогу назначения:')
        self.ent_src_title = ttk.Label(self, text='Введите абсолютный путь к исходному каталогу:')
        self.ent_expansion_title = ttk.Label(self, text='Введите расширения файла, например - (.txt) или " * " что бы выбрать все файлы: ')
        
        # data entry
        self.ent_src = ttk.Entry(self, width=70 ) #Поле ввода исходного каталога
        self.ent_dst = ttk.Entry(self, width=70 ) #Поле ввода  каталога назначения
        self.ent_expancion = ttk.Entry(self, width=70) #Поле ввода расширения
        
        #grid
        self.ent_src_title.grid(column=0, row=2, padx=10, sticky=ttk.W)
        self.ent_src.grid(column=0, row=3, padx=10, sticky=ttk.W)
        self.ent_dst_title.grid(column=0, row=4, padx=10, sticky=ttk.W)
        self.ent_dst.grid(column=0, row=5, padx=10, sticky=ttk.W)
        self.ent_expansion_title.grid(column=0, row=6, padx=10, sticky=ttk.W)
        self.ent_expancion.grid(column=0, row=7, padx=10, sticky=ttk.W)


        
        # start button
        self.but = ttk.Button(self, text="Старт",bg="lightgreen" , command=self.main )
        self.but.config(width=9, height=2, padx=10, pady=10)
        self.but.place(x=580, y=20)
        
        

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def start_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.main()

    # window = tk.Toplevel()
    # window.geometry('400x400')
    # window.title('Определить расширение файла')
    # var = tk.StringVar
    # window_text=tk.Label(window,text='Выберите файл чтобы узнать его расширение' )

    # window2 = tk.Toplevel()
    # window.geometry('600x400')
    # window.title('Help')
    # about = '''Абсолютный путь очень точно показывает где именно находится \n
    # файл, а относительный должен иметь обязательную привязку к какой-либо \n
    # отправной точкe, относительно которой и укзывается путь. \n
    # Например у нас есть картинка file.png на диске D:\\,  Абсолютный \n
    # путь к ней будет D:\\picture\\file.png, а относительно корневого \n
    # каталога можно указывать \\picture\\file.png '''
    # text_help = tk.Label(window2 ,text=about)
    # text_help.pack(side=ttk.LEFT, expand=True,padx=10, pady=10)



    # ent = ttk.Entry(window, textvariable=var)
    # # back = ttk.Button(window, text="Browse",command = self._file_expancion)
    # window_text.pack(side=ttk.TOP, pady=5, padx=5 )
    # ent.pack(side=ttk.TOP, pady=5, padx=5 )
    # # back.pack(side=ttk.TOP, pady=10)
       