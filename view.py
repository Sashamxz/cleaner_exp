import tkinter as tk





class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()
        
        self.ent_dst_title = tk.Label(self, text='Введите абсолютный путь к каталогу назначения:')
        self.ent_src_title = tk.Label(self, text='Введите абсолютный путь к исходному каталогу:')
        self.ent_expansion_title = tk.Label(self, text='Введите расширения файла, например - (.txt) или " * " что бы выбрать все файлы: ')
        
        # data entry
        self.ent_src = tk.Entry(self, width=70 ) #Поле ввода исходного каталога
        self.ent_dst = tk.Entry(self, width=70 ) #Поле ввода  каталога назначения
        self.ent_expancion = tk.Entry(self, width=70) #Поле ввода расширения
        
        
        #grid
        self.ent_src_title.grid(column=0, row=2, padx=10, sticky=tk.W)
        self.ent_src.grid(column=0, row=3, padx=10, sticky=tk.W)
        self.ent_dst_title.grid(column=0, row=4, padx=10, sticky=tk.W)
        self.ent_dst.grid(column=0, row=5, padx=10, sticky=tk.W)
        self.ent_expansion_title.grid(column=0, row=6, padx=10, sticky=tk.W)
        self.ent_expancion.grid(column=0, row=7, padx=10, sticky=tk.W)

  
        # start button
        self.butt_start = tk.Button(self, width=2, height=2, text="Старт", bg="lightgreen" )
        self.butt_start.place(x=580, y=20)
        

     
        
  

        # self.window2 = tk.Toplevel()
        # self.window.geometry('600x400')
        # self.window.title('Help')
        # self.about = '''Абсолютный путь очень точно показывает где именно находится \n
        # файл, а относительный должен иметь обязательную привязку к какой-либо \n
        # отправной точкe, относительно которой и укзывается путь. \n
        # Например у нас есть картинка file.png на диске D:\\,  Абсолютный \n
        # путь к ней будет D:\\picture\\file.png, а относительно корневого \n
        # каталога можно указывать \\picture\\file.png '''
        
        # self.ent = tk.Entry(self, textvariable=var)
        # self.back = tk.Button(self, text="Browse",) #command = self._file_expancion
        # self.window_text.pack(side=tk.TOP, pady=5, padx=5 )
        # self.ent.pack(side=tk.TOP, pady=5, padx=5 )
        # self.back.pack(side=tk.TOP, pady=10)
        # self.text_help = tk.Label(self.window2 ,text=self.about)
        # self.text_help.pack(side=tk.LEFT, expand=True,padx=10, pady=10)

        # set the controller
        self.controller = None
        
        
    


    def initUI(self):

        mainmenu = tk.Menu(self.parent) 
        self.parent.config(menu=mainmenu) 
        self.filemenu = tk.Menu(mainmenu, tearoff=0)
        self.helpmenu = tk.Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="Файл", menu=self.filemenu)
        mainmenu.add_cascade(label="Справка", menu=self.helpmenu )

      

  

    
       

    def field_num(self):
        numb = { self.ent_src : 1,
                self.ent_dst  : 2,
                self.ent_expancion : 3
                }
        return numb


    def set_controller(self, controller):
        """
        Set the controller
       
        """
        self.controller = controller


    def start_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.main()
    

   
          
class ExpancionFile(tk.Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title('Определить расширение файла')
        window_text=tk.Label(self,text='Выберите файл чтобы узнать его расширение' )
        window_text.pack(side=tk.TOP, pady=5, padx=5 )
        self.button_sel = tk.Button(self, text='Browse')
        self.geometry('400x400')
        # self.label.pack(padx=20, pady=20)
        var = tk.StringVar()
        self.ent = tk.Entry(self, textvariable=var)
        self.ent.pack(side=tk.LEFT, pady=5, padx=5 )
        self.button_sel.pack(side=tk.LEFT, pady=5, ipadx=2, ipady=2)
        
        
