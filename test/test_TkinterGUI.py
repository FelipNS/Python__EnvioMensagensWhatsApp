from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import errorcode
from test_TkinterFunctions import *


try:
    db_connection = conect_db()
    print("Database connection made!-TkinterGUI")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)

combobox_value = ''

class SelectClass:
    def __init__(self, master: Tk=None) -> None:
        """Constructor Class Frame

        Args:
            master (Tk, optional): Tk object. Defaults to None.
        """
        self.master = master
        self.lbf_classes = LabelFrame(self.master, text='  ESCOLHA A TURMA  ')
        self.cb_classes = ttk.Combobox(self.lbf_classes, postcommand=self.load_classes, width=33)
        self.cb_classes.bind('<<ComboboxSelected>>', self.combobox_value)
        self.btn_new_class = Button(self.lbf_classes, text='Editar turmas', command=lambda: ClassManipulation(self.master))
        self.lbf_classes.grid(row=1, column=0, columnspan=4, padx=10, sticky=W)
        self.cb_classes.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.btn_new_class.grid(row=0, rowspan=2, column=2, sticky=E, padx=8, pady=10)

    def load_classes(self):
        """Download class name of database
        """
        db_connection = conect_db()
        self.list_classes = []
        cursor = db_connection.cursor()
        cursor.execute('SELECT name FROM classesName')
        for names in cursor:
            name = names[0]
            self.list_classes.append(name)
        self.cb_classes.configure(values=self.list_classes)

    def combobox_value(self, event):
        """Update global variable 'combobox_value'

        Args:
            event: Defaut Tk for creation events
        """
        global combobox_value
        combobox_value = self.cb_classes.get()

class Title:
    def __init__(self, master=None) -> None:
        """Constructor Windows Title

        Args:
            master (Tk, optional): Tk object. Defaults to None.
        """
        self.master = master
        self.lb_title = Label(self.master, text='AUTOZAP', font='Verdana 20 bold')
        self.lb_title.grid(row=0,columnspan=10)

class AttachFiles:

    def __init__(self, master=None) -> None:
        """Constructor Attached listbox, Textbox, Label name frames

        Args:
            master (Tk, optional): Tk object. Defaults to None.
        """
        self.master = master
        #Listbox of attached files
        self.lbf_archive = LabelFrame(self.master, text='  ORDEM DE ENVIO  ')
        self.lst_archive = Listbox(self.lbf_archive, width=50, height=10, selectmode=SINGLE)
        self.lst_archive.bind('<<ListboxSelect>>', self.show_name_file)
        self.btn_send = Button(self.lbf_archive, text='ENVIAR', width=7, command=lambda: SendFiles(self.lst_archive, combobox_value, self.lst_archive, self.lb_name_file, SelectClass().cb_classes))
        self.btn_new_archive = Button(self.lbf_archive, text='ANEXAR ARQUIVO', command=lambda: ListBoxManipulation(self.lst_archive).insert_listbox(ListBoxManipulation().selectFiles(), many_items=True), width=15) 
        self.btn_up = Button(self.lbf_archive, text='↑', width=5, command=lambda: ListBoxManipulation(self.lst_archive).up_item_list())
        self.btn_down = Button(self.lbf_archive, text='↓', width=5, command=lambda: ListBoxManipulation(self.lst_archive).down_item_list())
        self.lbf_archive.grid(row=2, column=4, columnspan=4, padx=10, pady=10, sticky=E)
        self.lst_archive.grid(row=0, column=0, columnspan=4,sticky=W, padx=10)
        self.btn_send.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.btn_new_archive.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        self.btn_up.grid(row=1, column=2, pady=10, sticky=E)
        self.btn_down.grid(row=1, column=3, padx=10, pady=10, sticky=E)

        #Textbox of message
        self.lbf_mensage = LabelFrame(self.master, text='  DIGITE A MENSAGEM QUE DESEJA ENVIAR  ')
        self.txt_mensage = Text(self.lbf_mensage, width=45, height=10, font='Arial 10')
        self.btn_add_list = Button(self.lbf_mensage, text='Adicionar à lista de envio', command=lambda: ListBoxManipulation(self.lst_archive).insert_listbox(self.txt_mensage.get(1.0, END),widget=self.txt_mensage))
        self.lbf_mensage.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=W)
        self.txt_mensage.grid(row=0, column=0, sticky=W, padx=10)
        self.btn_add_list.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        
        #Label's name file
        self.master = master
        self.lbf_name_file = LabelFrame(self.master, text='  NOME DO ARQUIVO  ')
        self.lb_name_file = Label(self.lbf_name_file, width=27, justify=LEFT)
        self.btn_delete = Button(self.lbf_name_file, text='Excluir Anexo', command=lambda: ListBoxManipulation(self.lst_archive).delete_item(True))
        self.lbf_name_file.grid(row=1, column=4, columnspan=4,padx=11, sticky=E)
        self.lb_name_file.grid(row=0,column=0, columnspan=2, sticky=W, padx=11, pady=10)
        self.btn_delete.grid(row=0, column=2, columnspan=2, sticky=W, padx=11, pady=10)

    def show_name_file(self, event):
        """Show name in label name

        Args:
            event: Defaut Tk for creation events
        """
        name_file = self.lst_archive.get(ANCHOR)
        if name_file.count('/') > 0:
            pos_start = len(name_file) - name_file[::-1].index('/')
            self.lb_name_file.configure(text=name_file[pos_start:])
        else:
            self.lb_name_file.configure(text=name_file)
        
class Main:
    def __init__(self, master=None) -> None:
        """Constructor all main window

        Args:
            master (Tk, optional): Tk object. Defaults to None.
        """
        SelectClass(master)
        Title(master)
        AttachFiles(master)

def main_aplication():
    """Defines basics window properties
    """
    root = Tk()
    width= 720
    height = 360
    x = root.winfo_screenwidth()
    y = root.winfo_screenheight()
    pos_x = int((x/2) - (width/2))
    pos_y = int((y/2) - (height/2))
    root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
    root.title('AUTOZAP')
    root.iconbitmap('C:/Users/USER/OneDrive/Documentos/Programação/Python/Projetos/Envio_Fotos_WhatsApp/Src/Image/iconzap-complete.ico')
    
    Main(root)
    root.mainloop()


if __name__ == '__main__':
    main_aplication()
