from test_dataColector import WANavagation

nameChat = str(input('Digite o nome do grupo: '))
mensage = str(input('Digite a mensagem: '))

WANavagation().open_chat_whatsapp(nameChat, mensage)
