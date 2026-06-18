from armazenamento import salvar_clientes
from validacoes import (
    pedir_campo_obrigatorio,
    pedir_email_obrigatorio,
    pedir_telefone_obrigatorio
)

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
