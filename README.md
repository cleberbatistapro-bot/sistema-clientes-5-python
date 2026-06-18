# Sistema de Clientes 5.0 — Python

Sistema de cadastro de clientes desenvolvido em Python, com foco em CRUD, validações, persistência em JSON e organização modular do projeto.

## Objetivo do projeto

Este projeto foi criado como parte do meu aprendizado em Python, com foco em automação de processos, organização de código e construção de uma base técnica para projetos futuros da OONATECH.

A proposta foi desenvolver um sistema simples, mas bem estruturado, permitindo cadastrar, listar, alterar e remover clientes, aplicando boas práticas iniciais de organização, validação de dados e separação de responsabilidades.

## Funcionalidades

* Cadastro de clientes
* Listagem de clientes
* Alteração de nome, e-mail e telefone
* Remoção de clientes com confirmação
* Validação de campos obrigatórios
* Validação simples de e-mail
* Validação de telefone
* Bloqueio de e-mail duplicado
* Persistência de dados em arquivo JSON
* Organização do projeto em módulos

## Tecnologias utilizadas

* Python
* JSON
* Git
* GitHub

## Estrutura do projeto

```text
sistema-clientes-5-python/
│
├── main.py
├── clientes.py
├── validacoes.py
├── armazenamento.py
├── config.py
├── clientes_5_limpo.json
├── sistema_clientes_5_limpo.py
├── .gitignore
└── README.md
```

## Responsabilidade dos arquivos

* `main.py`: controla o menu principal e inicia o sistema.
* `clientes.py`: contém as funções de cadastro, listagem, alteração, remoção e seleção de clientes.
* `validacoes.py`: contém as funções de validação de campos, e-mail e telefone.
* `armazenamento.py`: contém as funções responsáveis por carregar e salvar os dados em JSON.
* `config.py`: guarda configurações do projeto, como o nome do arquivo JSON.
* `clientes_5_limpo.json`: arquivo onde os dados dos clientes são armazenados.
* `sistema_clientes_5_limpo.py`: versão completa anterior do sistema em um único arquivo.

## Como executar o projeto

1. Clone o repositório ou baixe os arquivos.
2. Abra a pasta do projeto no VS Code ou em outro editor.
3. Execute o arquivo principal:

```bash
python main.py
```

## Aprendizados aplicados

Neste projeto, foram praticados conceitos como:

* Funções em Python
* Listas e dicionários
* Lista de dicionários
* Estrutura CRUD
* Validação de dados
* Tratamento de erros com `try/except`
* Leitura e escrita em JSON
* Modularização de código
* Controle de versão com Git
* Publicação de projeto no GitHub

## Próximos passos

Possíveis evoluções futuras:

* Exportação de dados para CSV ou Excel
* Uso de banco de dados SQLite
* Criação de uma API com FastAPI
* Interface web para o sistema
* Relatórios simples de clientes
* Testes automatizados

## Autor

Desenvolvido por Cleber Batista, como parte da jornada de aprendizado em Python, Inteligência Artificial e automação de processos para a construção da OONATECH.

