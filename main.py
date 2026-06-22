from armazenamento import carregar_clientes
from clientes import (
    cadastrar_clientes,
    listar_clientes,
    alterar_clientes,
    remover_cliente
)
from exportacoes import exportar_clientes_excel

def exibir_menu():
    print("\n==== SISTEMA DE CLIENTES 5.0 ====\n")
    print("1 - Cadastrar cliente")
    print("2 - Listar cliente")
    print("3 - Alterar cliente")
    print("4 - Remover cliente")
    print("5 - Gerar planilha de clientes")
    print("6 - Sair")



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
                exportar_clientes_excel(clientes)

            elif opcao ==6:
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida. Escolha opção entre 1 e 6.")

        except ValueError:
            print("Opção inválida. Digite apenas números.")

    
if __name__ == "__main__":
    main()

