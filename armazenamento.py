import json
from config import ARQUIVO_CLIENTES


def carregar_clientes():
    try:
        with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        
    except FileNotFoundError:
        return[]
    
    except json.JSONDecodeError:
        print("Arquivo de clientes vazio ou com formato inválido.")
        return[]
    

def salvar_clientes(clientes):
    with open(ARQUIVO_CLIENTES,"w", encoding="utf-8")as arquivo:
        json.dump(clientes, arquivo, ensure_ascii=False, indent=4)

