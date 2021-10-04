from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showwarning, showinfo
from test_dataColector import WANavagation, start_browser, quit_browser
import mysql.connector
from mysql.connector import errorcode

def conect_db():
    db_connection = mysql.connector.connect(host='localhost', user='root', passwd='', database='classes')
    return db_connection

try:
    db_connection = conect_db()
    print("Database connection made!-TkinterFuncions")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)

def send_expression_mysql(expression: str):
    """Submit INSERT and DELETE query to Class table in database

    Args:
        expression (str): Expression write in MySQL sintax
    """
    cursor = db_connection.cursor()
    cursor.execute(expression)
    db_connection.commit()


class ListBoxManipulation:

    def __init__(self, lst='') -> None:
        """Set the listbox for manipulation

        Args:
            lst (str, optional): ListBox's name. Defaults to ''.
        """
        self.lst = lst
        
    def insert_listbox(self, value, many_items=False, widget=None):
        """Insert datas in listbox

        Args:
            value (str, tuple): Value for add in listbox
            many_items (bool, optional): True -> 2+ files to attach at the same time.
            False -> 1 file to attached. Defaults to False.
        """
        if many_items:
            for i in value:
                self.lst.insert(END, i)
        else:
            value = value.strip()
            widget.delete('1.0', END)
            self.lst.insert(END, value)
        
    def index_item_selected(self):
        """
        Returns:
            int: Return the index in listbox of item selected
        """
        tuple_lst = self.lst.get(0, END)
        return tuple_lst.index(self.lst.get(ANCHOR))

    def delete_item(self, ascending: bool):
        """Internal function used to delete item in listbox.
        It's used in the up_item_list and down_item_list functions 

        Args:
            ascending (bool): True to up_item_list || False to down_item_list
        """
        selected_item = self.lst.curselection()
        if ascending:
            for i in selected_item:
                self.lst.delete(i)
        else:
            for i in selected_item[::-1]:
                self.lst.delete(i)

    def up_item_list(self):
        """Command for button "↑" in the main window.
        """
        value = self.lst.get(ANCHOR)
        pos = ListBoxManipulation(self.lst).index_item_selected()
        new_pos = pos - 1
        self.lst.insert(new_pos, value)
        ListBoxManipulation(self.lst).delete_item(False)


    def down_item_list(self):
        """Command for button "↓" in the main window.
        """
        value = self.lst.get(ANCHOR)
        pos = ListBoxManipulation(self.lst).index_item_selected()
        new_pos = pos + 2
        self.lst.insert(new_pos, value)
        ListBoxManipulation(self.lst).delete_item(True)
    
    def selectFiles(self) -> None: 
        """

        Returns:
            None
        """
        return askopenfilenames()

class SendFiles:

    def __init__(self, widget: Listbox, class_name: str, *widget_clear) -> None:
        """Class constructor.

        Args:
            widget (tk.ListBox): Attached files listbox
            class_name (str): Class name on WhatsApp
            widget_clear (tk.widget): Widget to clear content
        """
        self.values = widget.get(0, END)
        if not self.is_empty(class_name):
            start_browser()
            WANavagation(class_name).open_chat_whatsapp()
            for i in self.values:
                if i[0:3] != 'C:/':
                    WANavagation(class_name).send_mensage(i)
                else:
                    WANavagation(class_name).send_midia(i)
            quit_browser()
            self.clear_widget(widget_clear)
            showinfo(title='Envio feito com sucesso!', message=f'O envio das menssagens para o {class_name} foi realizado com sucesso!', )
        else:
            showwarning(title='Nenhuma turma selecionada', message='Nenhuma turma selecionada. O programa foi interrompido!')

    def is_empty(self, class_name: str):
        """Analizes if str is empty or not

        Args:
            class_name (str): Name colected in 'Class Name' combobox 

        Returns:
            (bool): True if is empty || False if not empty
        """
        return True if class_name == '' else False

    def clear_widget(self, *widget):
        """Clears widget data according to widget type
        """
        j=0
        while j < len(widget[0]):
            str_widget = str(widget[0][j])
            if str_widget == '.!labelframe2.!listbox':
                wid = widget[0][j]
                wid.delete(0, END)
            elif str_widget == '.!labelframe4.!label':
                wid = widget[0][j]
                widget[0][j].configure(text='')
            elif str_widget == '.!labelframe5.!combobox':
                wid = widget[0][j]
                widget[0][j].configure(values='')
            j +=1

class ClassManipulation:

    def __init__(self, master):
        """Constructor Class

        Args:
            master (Tk): Tk object
        """
        self.master = master
        self.root = Toplevel(self.master)
        self.lbf_class = LabelFrame(self.root, text='  TURMAS REGISTRADAS  ')
        self.lbf_class.grid(row=0, rowspan=5, column=0, columnspan=4, padx=10, pady=10)
        self.lst_class = Listbox(self.lbf_class, selectmode=SINGLE, width=50)
        self.lst_class.grid(row=0, column=0, padx=5, pady=5)
        self.load_classes()
        self.lbf_new_class = LabelFrame(self.root, text='  NOVA TURMA  ')
        self.lbf_new_class.grid(row=0, rowspan=3, column=4, columnspan=2, padx=10, pady=(10,5))
        self.lb_new_class = Label(self.lbf_new_class, text='Digite o nome da nova turma')
        self.lb_new_class.grid(row=0, column=0, padx=10, pady=10)
        self.new_class = Entry(self.lbf_new_class)
        self.new_class.grid(row=1, column=0, padx=10, pady=10)
        self.btn_new_class = Button(self.lbf_new_class, text='ADICIONAR', command=lambda: self.add_class())
        self.btn_new_class.grid(row=2, column=0, padx=10, pady=10)

        self.btn_delete_item = Button(self.root, text='Excluir turma \nselecionada', justify=CENTER, width=10, command=lambda: self.delete_item())
        self.btn_delete_item.grid(row=3, rowspan=2, column=4, padx=10, pady=(5,10), sticky=W)
        self.btn_save =Button(self.root, text='Salvar', justify=CENTER, width=5, command=lambda: self.save_changes())
        self.btn_save.grid(row=3, rowspan=2, column=5, padx=10, pady=(5,10), sticky=E)


    def load_classes(self):
        """Colects class names in localhost database
        """
        cursor = db_connection.cursor()
        sql = 'SELECT name FROM classesName'
        cursor.execute(sql)
        for names in cursor:
            name = names[0]
            self.lst_class.insert(END, name)

    def add_class(self):
        """Adds name new class colected in Entry widget in listbox and database
        """
        self.lst_class.insert(END, self.new_class.get())
        send_expression_mysql(f"INSERT INTO classesName(name) VALUES('{self.new_class.get()}')")
        self.new_class.delete(0, END)
    
    def delete_item(self):
        """Deletes listbox selected name, of listbox and database
        """
        item_delete = self.lst_class.get(ANCHOR)
        send_expression_mysql(f"DELETE FROM classesName WHERE name='{item_delete}'")
        item_delete = self.lst_class.curselection()
        self.lst_class.delete(item_delete)
    
    def save_changes(self):
        """Destroy TopLevel object
        """
        self.root.destroy()
