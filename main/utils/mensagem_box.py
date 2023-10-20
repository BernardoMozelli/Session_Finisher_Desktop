from CTkMessagebox import CTkMessagebox

def consult_success():
    global show_consult_sucess
    show_consult_sucess = CTkMessagebox(
        title="Consulta",
        message="Sua consulta retornou alguns registros...",
        icon="check", option_1="Ok",
        fade_in_duration=(2))
consult_success
    
def consult_error():
    global show_consult_error
    show_consult_error = CTkMessagebox(
        title="Consulta",
        message="Sua consulta não retornou nenhum registro!!!",
        icon="warning", option_1="Ok",
        fade_in_duration=(2))
    resposta = show_consult_error.get()

    if resposta == "Ok":
     global show_consult_error2
     show_consult_error2 = CTkMessagebox(
         title="Consulta",
         message = "Verifique o nome de usuário informado e tente novamente!!!",
         icon="warning", option_1="Ok",
         fade_in_duration=(2))
consult_error

