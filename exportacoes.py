import csv
from openpyxl import Workbook
from config import ARQUIVO_CSV, ARQUIVO_EXCEL

def exportar_clientes_csv(clientes):
    with open(ARQUIVO_CSV, "w", encoding="utf-8", newline="") as arquivo:
        campos = ["nome", "email", "telefone"]


        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(clientes)

    print("Planilha de clientes gerada com sucesso.")



def exportar_clientes_excel(clientes):
    planilha_excel = Workbook()

    pagina_clientes = planilha_excel.active
    pagina_clientes.tittle = "clientes"

    pagina_clientes.append(["Nome", "E-mail", "Telefone"])

    for cliente in clientes:
        pagina_clientes.append([
            cliente["nome"],
            cliente["email"],
            cliente["telefone"]
        ])


    planilha_excel.save(ARQUIVO_EXCEL)

    print(f"Planilha Excel de clientes gerada com sucesso: {ARQUIVO_EXCEL}")