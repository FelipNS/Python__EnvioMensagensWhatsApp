from tkinter import *
from tkinter.filedialog import askopenfilenames
from test_dataColector import WANavagation


class ListBoxManipulation:

    def __init__(self, lst='') -> None:
        self.lst = lst
        
    def insert_listbox(self, value, many_items=False):
        if many_items:
            for i in value:
                self.lst.insert(END, i)
        else:
            value = value.strip()
            self.lst.insert(END, value)
        
    def index_item_selected(self):
        tuple_lst = self.lst.get(0, END)
        return tuple_lst.index(self.lst.get(ANCHOR))

    def delete_item(self, descending: bool):
        selected_item = self.lst.curselection()
        if descending:
            for i in selected_item[::-1]:
                self.lst.delete(i)
        else:
            for i in selected_item:
                self.lst.delete(i)

    def up_item_list(self):
        value = self.lst.get(ANCHOR)
        pos = ListBoxManipulation(self.lst).index_item_selected()
        new_pos = pos - 1
        self.lst.insert(new_pos, value)
        ListBoxManipulation(self.lst).delete_item(True)


    def down_item_list(self):
        value = self.lst.get(ANCHOR)
        pos = ListBoxManipulation(self.lst).index_item_selected()
        new_pos = pos + 2
        self.lst.insert(new_pos, value)
        ListBoxManipulation(self.lst).delete_item(False)
    
    def selectFiles(self):
        return askopenfilenames()


