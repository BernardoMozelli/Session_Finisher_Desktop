import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from shutil import copyfile
import os
from shutil import copyfile

def copiar_log():
    from session_finisher import entry_usuario
    #from utils.mensagem_box import msg_sucessoCons, msg_avisoC

    # Caminho onde se encontra o caminho do arquivo na pasta de rede
    source = (r"//10.1.100.4/log$/logon.LOG")
 
    # Destino
    destination =  os.path.join("C:/", "logon.LOG")
 
    # Copia o arquivo da pasta de rede para o C: da maquina
    copyfile(source, destination)

    global abrir_arquivo
    abrir_arquivo = open('C:/logon.LOG', 'r') #local onde se encontra o arquivo txt
copiar_log



