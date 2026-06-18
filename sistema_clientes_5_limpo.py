import json

ARQUIVO_CLIENTES = "clientes_5_limpo.json"


#FUNÇÕES DE ARMAZENAMENTO
def carregar_clientes():
    try:
        with open(ARQUIVO_CLIENTES,"r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        

    except FileNotFoundError:
        return[]
    
    except json.JSONDecodeError:
        print("Arquivo de clientes vazio ou com formato inválido.")
        return[]



def salvar_clientes(clientes):
    with open(ARQUIVO_CLIENTES,"w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, ensure_ascii=False, indent=4)



#FUNÇÕES DE VALIDAÇÃO
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

#REGRAS DE NEGOCIO
def email_ja_cadastrado(clientes, email):
    for cliente in clientes:
        if cliente["email"] == email:
            return True
        
    return False


#FUNÇÕES AUXILIARES
def selecionar_cliente(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return None
    
    for indice, cliente, in enumerate(clientes):
        print(f"{indice + 1} - {cliente['nome']}  | {cliente['email']}")


    try:
        escolha = int(input("Escolha um número do cliente: "))

        if escolha <1 or escolha > len(clientes):
            print(f"Escolha cliente entre 1 e {len(clientes)}")
            return None
        
        indice_real = escolha - 1
        return indice_real
    
    except ValueError:
        print("Opção inválida. Digite apenas números.")
        return None


# FUNÇÕES PRINCIPAIS DO SISTEMA
def cadastrar_clientes(clientes):
    nome = pedir_campo_obrigatorio("Digite o nome do cliente: ")
    email = pedir_email_obrigatorio("Digite o e-mail do cliente: ")

    if email_ja_cadastrado(clientes, email):
        print("Este e-mail já foi cadastrado. Cadastro cancelado.")
        return
    
    telefone = pedir_telefone_obrigatorio("Digite o telefone do cliente: ")

    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone
    }


    clientes.append(cliente)
    salvar_clientes(clientes)
    
    print(f"Cliente cadastrado com sucesso: {nome}")


def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    print("\n=== LISTA DE CLIENTES ===")

    for indice, cliente in enumerate(clientes):
        print(f"\nCliente {indice + 1}")
        print(f"Nome: {cliente['nome']}")
        print(f"email: {cliente['email']}")
        print(f"Telefone: {cliente['telefone']}")


def alterar_clientes(clientes):
    indice = selecionar_cliente(clientes)

    if indice is None:
        return
    
    cliente = clientes[indice]


    print("\n=== ALTERAR CLIENTE ===")
    print(f"Cliente selecionado: {cliente['nome']}")
    print("1- Alterar nome")
    print("2- Alterar e-mail")
    print("3- Alterar telefone")
    print("4- Voltar")


    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            novo_nome = pedir_campo_obrigatorio("Digite o novo nome: ")
            cliente["nome"] = novo_nome
            salvar_clientes(clientes)
            print("Nome alterado com sucesso.")


        elif opcao ==2:
            novo_email = pedir_email_obrigatorio("Digite o novo e-mail: ")
            
            if novo_email != cliente['email'] and email_ja_cadastrado(clientes, novo_email):
                print("Este e-mail já está cadastrado. Alteração cancelada.")
                return
            
            cliente["email"] = novo_email
            salvar_clientes(clientes)
            print("E-mail alterado com sucesso.")


        elif opcao ==3:
            novo_telefone = pedir_telefone_obrigatorio("Digite o novo telefone: ")
            cliente["telefone"] = novo_telefone
            salvar_clientes(clientes)
            print("Telefone alterado com sucesso.")


        elif opcao ==4:
            print("Alteração cancelada.")

        else:
            print("Opção inválida. Escolha entre 1 e 4")

    except ValueError:
        print("Opção inválida. Digite apenas números.")



def remover_cliente(clientes):
    indice = selecionar_cliente(clientes)

    if indice is None:
        return
    
    cliente = clientes[indice]

    print("\n=== REMOVER CLIENTES ===")
    print(f"cliente selecionado: {cliente['nome']}")
    print(f"E-mail: {cliente['email']}")
    print(f"Telefone: {cliente['telefone']}")


    confirmacao = input("Tem certeza que deseja remover este cliente? (s/n): ").strip().lower()

    if confirmacao =="s":
        cliente_removido = clientes.pop(indice)
        salvar_clientes(clientes)
        print(f"Cliente removido com sucesso: {cliente_removido['nome']}")


    elif confirmacao == "n":
        print("Remoção cancelada.")

    else:
        print("Opção inválida. Remoção cancelada.")



#MENU
def exibir_menu():
    print("\n==== SISTEMA DE CLIENTES 5.0 ====")
    print("1 - Cadastrar cliente")
    print("2 - Listar cliente")
    print("3 - Alterar cliente")
    print("4 - Remover cliente")
    print("5 - Sair")


#FUNÇÃO PRINCIPAL
def main():
    clientes = carregar_clientes()

    while True:
        exibir_menu()

        try:

            opcao = int(input("Escolha uma opção: "))

            if opcao ==1:
                cadastrar_clientes(clientes)

            elif opcao ==2:
                listar_clientes(clientes)

            elif opcao ==3:
                alterar_clientes(clientes)

            elif opcao ==4:
                remover_cliente(clientes)

            elif opcao ==5:
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida. Escolha opção entre 1 e 5.")

        except ValueError:
            print("Opção inválida. Digite apenas números.")

    
if __name__ == "__main__":
    main()








