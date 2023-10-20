import customtkinter
import tkinter
import customtkinter  as ctk
from PIL import ImageTk,Image
from CTkMessagebox import CTkMessagebox
import sys
from utils.layout import *

janela_consulta = customtkinter.CTk()
janela_consulta.title("Ending Session")
janela_consulta.wm_iconbitmap(default="./imagens/logo_icone.ico")  # alterando o icone
janela_consulta.geometry("600x500")
janela_consulta.geometry("1000x550+250+70")
janela_consulta.resizable(False, False)


# Criando e configurando o frame
frame = customtkinter.CTkFrame(master=janela_consulta,
                               width=410, height=396,
                               border_width=2,
                               border_color=co3,
                               bg_color="transparent",
                               fg_color="transparent",
                               corner_radius=15)
frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Criando e configurando a label usuario
label_titulo = customtkinter.CTkLabel(master=frame,
                                      text="ENDING SESSION",
                                      font=('Poppins bold', 17),
                                      width=50,
                                      height=20,
                                      fg_color=co3,
                                      corner_radius=8)
label_titulo.place(x=210, y=70, anchor=tkinter.CENTER)


# Criando e configurando a label usuario
label_usuario = customtkinter.CTkLabel(master=frame,
                                      text="USUÁRIO",
                                      font=('Poppins bold', 12),
                                      width=50,
                                      height=20,
                                      fg_color=co3,
                                      corner_radius=8)
label_usuario.place(x=80, y=155, anchor=tkinter.CENTER)

# Criando e configurando a entry usuário
entry_consulta = customtkinter.CTkEntry(master=frame,
                                    width=310,
                                    height=30,
                                    font=('Century gothic', 14),
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    placeholder_text='Insira o nome do usuário',
                                    justify='center')
entry_consulta.place(x=203, y=187, anchor=tkinter.CENTER)

# #Criando e configurando o botão esqueceu a senha
button_consultar = customtkinter.CTkButton(master=frame, text="REALIZAR CONSULTA",
                                          width=30,
                                          height=15,
                                          font=('Poppins',13),
                                          fg_color=co3,
                                          hover_color=co2)

button_consultar.place(x=200, y=240, anchor=tkinter.CENTER)

def armazenar():
    entry_consulta.get()
armazenar

#Função responsável por ler o arquivo e buscar o nome informado pelo usuário
def ler_arquivo(event = None):
    #Armazena o conteudo da entry em uma variável global
    usuario_consulta = entry_consulta.get()
    
    with open("C://logon.LOG", 'r') as arquivo:
        log = arquivo.readlines()
    
    found = False
    for linha in log:
    
            if usuario_consulta in linha:
                print(linha)
                found = True
 
    if not found:
        print("Usuário não encontrado!!!")
        sys.exit()                

ler_arquivo

#button_consultar.bind("<Button-1>", ler_arquivo)
button_consultar.configure(command=lambda:[armazenar(), ler_arquivo()])

janela_consulta.mainloop()

