from tkinter import *
from tkinter import ttk
from TkinterFunctions import ListBoxManipulation, SendFiles

list_classes = ['1°e 2° PERÍODO PONTE NOVA', '1°ANO PONTE NOVA', "Mãe Linda♥"]
def show_name_file(event):
    name_file = lst_archive.get(ANCHOR)
    if name_file.count('/') > 0:
        pos_start = len(name_file) - name_file[::-1].index('/')
        lb_name_file.configure(text=name_file[pos_start:])
    else:
        lb_name_file.configure(text=name_file)


root = Tk()
root.geometry("720x360")

lb_title = Label(root, text='AUTOZAP', font='Verdana 20 bold')
lb_title.grid(row=0,columnspan=10)

lbf_classes = LabelFrame(root, text='  ESCOLHA A TURMA  ')
cb_classes = ttk.Combobox(lbf_classes, values=list_classes, width=49)
lbf_classes.grid(row=1, column=0, columnspan=4, padx=10, sticky=W)
cb_classes.grid(row=0,column=0,sticky=W, padx=10, pady=10)


lbf_archive = LabelFrame(root, text='  ORDEM DE ENVIO  ')
lst_archive = Listbox(lbf_archive, width=50, height=10, selectmode=SINGLE)
lst_archive.bind('<<ListboxSelect>>', show_name_file)
btn_send = Button(lbf_archive, text='ENVIAR', width=7, command=lambda: SendFiles(lst_archive, cb_classes.get()))
btn_new_archive = Button(lbf_archive, text='ANEXAR ARQUIVO', command=lambda: ListBoxManipulation(lst_archive).insert_listbox(ListBoxManipulation().selectFiles(), many_items=True), width=15) 
btn_up = Button(lbf_archive, text='↑', width=5, command=lambda: ListBoxManipulation(lst_archive).up_item_list())
btn_down = Button(lbf_archive, text='↓', width=5, command=lambda: ListBoxManipulation(lst_archive).down_item_list())
lbf_archive.grid(row=2, column=4, columnspan=4, padx=10, pady=10, sticky=E)
lst_archive.grid(row=0, column=0, columnspan=4,sticky=W, padx=10)
btn_send.grid(row=1, column=0, padx=10, pady=10, sticky=W)
btn_new_archive.grid(row=1, column=1, padx=10, pady=10, sticky=W)
btn_up.grid(row=1, column=2, pady=10, sticky=E)
btn_down.grid(row=1, column=3, padx=10, pady=10, sticky=E)

lbf_name_file = LabelFrame(root, text='  NOME DO ARQUIVO  ')
lb_name_file = Label(lbf_name_file, width=27, justify=LEFT)
btn_delete = Button(lbf_name_file, text='Excluir Anexo', command=lambda: ListBoxManipulation(lst_archive).delete_item(False))
lbf_name_file.grid(row=1, column=4, columnspan=4,padx=11, sticky=E)
lb_name_file.grid(row=0,column=0, columnspan=2, sticky=W, padx=11, pady=10)
btn_delete.grid(row=0, column=2, columnspan=2, sticky=W, padx=11, pady=10)

lbf_mensage = LabelFrame(root, text='  DIGITE A MENSAGEM QUE DESEJA ENVIAR  ')
txt_mensage = Text(lbf_mensage, width=45, height=10, font='Arial 10')
btn_add_list = Button(lbf_mensage, text='Adicionar à lista de envio', command=lambda: ListBoxManipulation(lst_archive).insert_listbox(txt_mensage.get(1.0, END)))
lbf_mensage.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=W)
txt_mensage.grid(row=0, column=0, sticky=W, padx=10)
btn_add_list.grid(row=1, column=0, padx=10, pady=10, sticky=W)

root.mainloop()