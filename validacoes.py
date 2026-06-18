def pedir_campo_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor =="":
            print("Campo obrigatório. Tente novamente.")
            continue

        return valor



def validar_email(email):
    if "@" not in email:
        return False
    
    if "." not in email:
        return False


    if email.startswith("@") or email.endswith("@"):
        return False
    

    if email.startswith(".") or email.endswith("."):
        return False
    
    return True




def pedir_email_obrigatorio(mensagem):
    while True:
        email = pedir_campo_obrigatorio(mensagem)

        if validar_email(email):
            return email
        
        print("E-mail inválido. Tente novamente.")



def validar_telefone(telefone):
    if not telefone.isdigit():
        return False
    
    if len(telefone) < 8:
        return False
    
    return True

def pedir_telefone_obrigatorio(mensagem):
    while True:
        telefone = pedir_campo_obrigatorio(mensagem)

        if validar_telefone(telefone):
            return telefone
        
        print("Telefone inválido. Digite apenas números com pelo menos 8 dígitos.")

