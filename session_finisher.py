#Desenvolvido por Bernardo Mozelli de Medeiros - M2b Sistemas
#Data: 09/11/2023
#Objetivo: Finalizar sessões de usuários de forma remota.
#Versão 1.0
#--------------------------------------------------------------------

import customtkinter
import tkinter
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox
import pandas
import os
import sys
import subprocess
import customtkinter as ctk

################# Estilo das páginas ###############

co1 = "white"  # branca
co2 = "#1c999d"   # Verde água
co3 = "#1f538d"  # Azul 2

# Escolhendo tema padrão dos widgets
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

#####################################################

janela_consulta = customtkinter.CTk()
janela_consulta.title("Ending Session")
janela_consulta.iconbitmap(default="C:/Session Finisher/imagens/logo_icone.ico")
janela_consulta.geometry("600x500")
janela_consulta.geometry("1000x550+250+70")
janela_consulta.resizable(False, False)

# Inserindo imagem de fundo
img_logo = ImageTk.PhotoImage(Image.open("C:/Session Finisher/imagens/logo.png"))
label_logo = customtkinter.CTkLabel(master=janela_consulta,
                                    text="",
                                    width=50,
                                    height=70,
                                    image=img_logo)
label_logo.place(x=250, y=10)
label_logo.pack()


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
label_titulo.place(x=210, y=40, anchor=tkinter.CENTER)


# Criando e configurando a label usuario
label_usuario = customtkinter.CTkLabel(master=frame,
                                       text="USUÁRIO",
                                       font=('Poppins bold', 12),
                                       width=50,
                                       height=20,
                                       fg_color=co3,
                                       corner_radius=8)
label_usuario.place(x=83, y=103, anchor=tkinter.CENTER)

# Criando e configurando a entry usuário
entry_consulta = customtkinter.CTkEntry(master=frame,
                                        width=310,
                                        height=30,
                                        font=('Century gothic', 14),
                                        fg_color="transparent",
                                        bg_color="transparent",
                                        placeholder_text='Insira o nome do usuário',
                                        justify='center')
entry_consulta.place(x=203, y=135, anchor=tkinter.CENTER)

# Criando e configurando a label ano
label_data = customtkinter.CTkLabel(master=frame,
                                    text="DATA",
                                    font=('Poppins bold', 12),
                                    width=45,
                                    height=20,
                                    fg_color=co3,
                                    corner_radius=8)
label_data.place(x=72, y=178, anchor=tkinter.CENTER)


# Criando e configurando a entry usuário
entry_data = customtkinter.CTkEntry(master=frame,
                                        width=310,
                                        height=30,
                                        font=('Century gothic', 14),
                                        fg_color="transparent",
                                        bg_color="transparent",
                                        placeholder_text='Insira o mês e o ano da busca',
                                        justify='center')
entry_data.place(x=203, y=210, anchor=tkinter.CENTER)

def format_data(event=None):
    entry_data.get()
    text = entry_data.get().replace("/", "")[:6]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for index in range(len(text)):

         if not text[index] in "0123456789":
                continue
         if index in [1]:
               new_text += text[index] + "/"
         elif index == 1:
                new_text += text[index] + "/"
         else:
               new_text += text[index]

         entry_data.delete(0, "end")
         entry_data.insert(0, new_text)
format_data 

entry_data.bind('<KeyRelease>', format_data)


# Criando e configurando o botão esqueceu a senha
button_consultar = customtkinter.CTkButton(master=frame, text="Clique aqui para consultar",
                                           width=15,
                                           height=20,
                                           font=('Poppins Bold', 10),
                                           fg_color="transparent",
                                           hover_color=co2)

button_consultar.place(x=210, y=245, anchor=tkinter.CENTER)


# Criando e configurando a label nome do computador
label_nomedopc = customtkinter.CTkLabel(master=frame,
                                    text="NOME DO COMPUTADOR",
                                    font=('Poppins bold', 12),
                                    width=45,
                                    height=20,
                                    fg_color=co3,
                                    corner_radius=8)
label_nomedopc.place(x=128, y=293, anchor=tkinter.CENTER)

# Criando e configurando a entry nome do computador
entry_nomedopc = customtkinter.CTkEntry(master=frame,
                                        width=310,
                                        height=30,
                                        font=('Century gothic', 14),
                                        fg_color="transparent",
                                        bg_color="transparent",
                                        placeholder_text='Insira o nome do computador',
                                        justify='center')
entry_nomedopc.place(x=204, y=325, anchor=tkinter.CENTER)

# Armazena os dados inseridos nas entrys
def armazenar():
    entry_consulta.get()
    entry_data.get()
    entry_nomedopc.get() 
armazenar

# Criando e configurando o botão finalizar sessão
button_finalizar = customtkinter.CTkButton(master=frame, text="FINALIZAR SESSÃO",
                                           width=30,
                                           height=30,
                                           font=('Poppins', 13),
                                           fg_color=co3,
                                           hover_color=co2)

button_finalizar.place(x=214, y=370, anchor=tkinter.CENTER)

# Função responsável por ler o arquivo e buscar o nome informado pelo usuário
def ler_arquivo(event=None):
    
    #Armazena o conteudo da entry em uma variável global
    usuario_consulta = entry_consulta.get()
    ano_consulta = entry_data.get()
    
    #Abre o arquivo e executa uma busca no mesmo de acordo com o que foi informado nas entrys (Nome de usuário e Data)
    with open(r"//10.1.100.4/log$/logon.LOG") as arquivo:
        log = arquivo.readlines()
    
    logon = open('C://logon.csv', "w")

    #Se as as referencias inseridas forem localizadas no arquivo, armazena em um arquivo .csv
    found = False
    for linha in log :
        if usuario_consulta in linha and ano_consulta in linha:
            logon.write(linha)
            found = True
    logon.close()
    
    #Exibe mensagem de erro caso a condição do primeiro if seja falsa
    if not found:
        global show_aviso1, resposta2
        show_aviso1 = CTkMessagebox(
            title="Session Finisher - Consulta",
            message="Sua consulta não retornou nenhum registro!!!",
            icon="warning", option_1="Ok",
            fade_in_duration=(2))
        resposta2 = show_aviso1.get()
        if resposta2 == "Ok":
            sys.exit()
    
    #Exibe mensagem de sucesso caso a condição do primeiro if seja verdadeira
    global show_consult_sucess
    show_consult_sucess = CTkMessagebox(
        title="Session Finisher - Consulta",
        message="Sua consulta retornou alguns registros. Aguarde, gerando arquivo csv...",
        icon="check", option_1="Exibir",
        fade_in_duration=(2))
    resposta = show_consult_sucess.get()
    
    #Quando o usuário clica no botão "Exibir", da mensagem de sucesso, arquivo que armazena o resultado da busca é aberto.
    #Após copiar o nome do computador, é necessário fechar o arquivo para continuar a execução do sistema.
    if resposta == "Exibir":
        os.system('C://logon.csv')

ler_arquivo

#Executa comando para exibir usuários logados no computador informado
def comando_01():
    global var_nomedopc
    global var_usuario   
    var_nomedopc = entry_nomedopc.get()
    var_usuario = entry_consulta.get()
    
    #Executa o comando no cmd e armazena a saída em uma variável
    cmd_to_run = ('qwinsta /server:{} {}'.format(var_nomedopc.lstrip(), var_usuario))
    results_id = subprocess.run(cmd_to_run, shell=False, text=True, stdout=subprocess.PIPE)
    resultado_txt = (str(results_id.stdout))
    
    with open('C://comando_id.txt', 'w') as arquivo_id:
        arquivo_id.write(str(resultado_txt))     
    arquivo_id.close()

comando_01

def comando_02():
    df = pandas.read_fwf('C://comando_id.txt')
    var_id = (df.iat[0,2])
    
    resultado_finalID = var_id
    
    cmd_to_run2 = ('logoff /server:{} {}'.format(var_nomedopc.lstrip(), resultado_finalID))
    valida = subprocess.run(cmd_to_run2, shell=True, text=True, stdout=subprocess.PIPE)
    
    comando_status = True
    if comando_status:
         #Exibe mensagem de sucesso caso a condição do primeiro if seja verdadeira
        global show_comandsucess
        show_comandsucess = CTkMessagebox(
            title="Session Finisher",
            message="Sessão do usuário " + var_usuario + " foi finalizada com sucesso!!!",
            icon="check", option_1="Ok",
            fade_in_duration=(2))
        resposta = show_comandsucess.get()
        if resposta == "Ok":
            return var_usuario
    if not comando_status:
        global show_comanderro
        show_comanderro = CTkMessagebox(
            title="Session Finisher",
            message='Falha ao finalizar sessão do usuário ' + var_usuario + ".",
            icon="check", option_1="Ok",
            fade_in_duration=(2))
        resposta = show_comanderro.get()
        if resposta == "Ok":
            return var_usuario
    
comando_02

#Consultando usuário e retornando a ultima informação salva no log no momento da execução
button_consultar.configure(command=lambda: [armazenar(), ler_arquivo()])

#Executa os comandos no cmd para finalizar a sessão do usuário
button_finalizar.configure(command=lambda: [armazenar(), comando_01(), comando_02()])

janela_consulta.mainloop()


