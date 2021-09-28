from tkinter import *
from tkinter import ttk
from test_dataColector import WANavagation
from test_filesManipulation import FolderAndFiles
from test_TkinterFunctions import ListBoxManipulation

list_classes = ['1°e 2° PERÍODO PONTE NOVA', '1°ANO PONTE NOVA', "Mãe Linda♥"]
def show_full_path(event):
    full_path = lst_archive.get(ANCHOR)
    if full_path.count('/') > 0:
        pos_start = len(full_path) - full_path[::-1].index('/')
        lb_full_path.configure(text=full_path[pos_start:])
    else:
        lb_full_path.configure(text=full_path)


root = Tk()
root.geometry("720x360")

lb_title = Label(root, text='AUTOZAP', font='Verdana 20 bold')
lb_title.grid(row=0,columnspan=10)

lbf_classes = LabelFrame(root, text='  ESCOLHA A TURMA  ')
cb_classes = ttk.Combobox(lbf_classes, values=list_classes, width=49)
lbf_classes.grid(row=1, column=0, columnspan=4, padx=10, sticky=W)
cb_classes.grid(row=0,column=0,sticky=W, padx=10, pady=10)

lbf_full_path = LabelFrame(root, text='  CAMINHO COMPLETO DO ARQUIVO  ')
lb_full_path = Label(lbf_full_path, width=42)
lbf_full_path.grid(row=1, column=4, columnspan=4,padx=11, sticky=E)
lb_full_path.grid(row=0,column=0, columnspan=4, sticky=W, padx=11, pady=10)
lbf_archive = LabelFrame(root, text='  ORDEM DE ENVIO  ')
lst_archive = Listbox(lbf_archive, width=50, height=10, selectmode=SINGLE)
lst_archive.bind('<<ListboxSelect>>', show_full_path)
btn_send = Button(lbf_archive, text='ENVIAR', width=7)
btn_new_archive = Button(lbf_archive, text='ANEXAR ARQUIVO', command=lambda: ListBoxManipulation(lst_archive).insert_listbox(ListBoxManipulation().selectFiles(), many_items=True), width=15) 
btn_up = Button(lbf_archive, text='↑', width=5, command=lambda: ListBoxManipulation(lst_archive).up_item_list())
btn_down = Button(lbf_archive, text='↓', width=5, command=lambda: ListBoxManipulation(lst_archive).down_item_list())
lbf_archive.grid(row=2, column=4, columnspan=4, padx=10, pady=10, sticky=E)
lst_archive.grid(row=0, column=0, columnspan=4,sticky=W, padx=10)
btn_send.grid(row=1, column=0, padx=10, pady=10, sticky=W)
btn_new_archive.grid(row=1, column=1, padx=10, pady=10, sticky=W)
btn_up.grid(row=1, column=2, pady=10, sticky=E)
btn_down.grid(row=1, column=3, padx=10, pady=10, sticky=E)


lbf_mensage = LabelFrame(root, text='  DIGITE A MENSAGEM QUE DESEJA ENVIAR  ')
txt_mensage = Text(lbf_mensage, width=45, height=10, font='Arial 10')
btn_add_list = Button(lbf_mensage, text='Adicionar à lista de envio', command=lambda: ListBoxManipulation(lst_archive).insert_listbox(txt_mensage.get(1.0, END)))
lbf_mensage.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=W)
txt_mensage.grid(row=0, column=0, sticky=W, padx=10)
btn_add_list.grid(row=1, column=0, padx=10, pady=10, sticky=W)


root.mainloop()