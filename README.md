# Mini CRM Administrativo em Python

Sistema simples de gestão de clientes desenvolvido em Python, com foco em cadastro, organização de dados, validação de informações, persistência em JSON e geração de planilha Excel.

Este projeto foi criado como parte da minha evolução prática em Python, automação de processos, análise de dados e desenvolvimento de soluções administrativas.

## Objetivo do projeto

O objetivo do projeto é simular uma rotina administrativa simples de controle de clientes.

O sistema permite cadastrar clientes, consultar registros, alterar dados, remover clientes com confirmação e gerar uma planilha Excel organizada para uso administrativo.

Este projeto também serve como base para futuras evoluções, como sistemas de agendamento, CRM, relatórios, dashboards e automações para pequenas empresas.

## Funcionalidades

* Cadastrar clientes
* Listar clientes cadastrados
* Alterar dados de clientes
* Remover clientes com confirmação
* Validar campos obrigatórios
* Validar formato básico de e-mail
* Validar telefone com apenas números
* Impedir cadastro duplicado pelo mesmo e-mail
* Salvar dados em arquivo JSON
* Carregar dados automaticamente ao abrir o sistema
* Gerar planilha Excel de clientes
* Criar tabela oficial do Excel com filtros e formatação

## Tecnologias utilizadas

* Python
* JSON
* CSV
* openpyxl
* Git
* GitHub

## Estrutura do projeto

```text
sistema_cliente_5.0/
│
├── main.py
├── clientes.py
├── validacoes.py
├── armazenamento.py
├── exportacoes.py
├── config.py
├── clientes_5_limpo.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Responsabilidade dos arquivos

### `main.py`

Controla o fluxo principal do sistema.

É responsável por exibir o menu, receber a opção do usuário e chamar as funções corretas.

### `clientes.py`

Contém as funções principais do sistema:

* cadastrar clientes
* listar clientes
* alterar clientes
* remover clientes
* selecionar cliente
* verificar e-mail duplicado

### `validacoes.py`

Contém as funções de validação:

* campo obrigatório
* e-mail
* telefone

### `armazenamento.py`

Responsável por carregar e salvar os dados no arquivo JSON.

### `exportacoes.py`

Responsável por gerar arquivos externos, como CSV e Excel.

A principal saída atual do sistema é a planilha:

```text
clientes.xlsx
```

### `config.py`

Guarda os nomes dos arquivos usados no projeto.

### `requirements.txt`

Lista as bibliotecas externas necessárias para executar o projeto.

## Como executar o projeto

1. Clone este repositório:

```bash
git clone https://github.com/cleberbatistapro-bot/sistema-clientes-5-python.git
```

2. Acesse a pasta do projeto:

```bash
cd sistema-clientes-5-python
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o sistema:

```bash
python main.py
```

## Menu do sistema

```text
==== SISTEMA DE CLIENTES 5.0 ====

1 - Cadastrar cliente
2 - Listar clientes
3 - Alterar cliente
4 - Remover cliente
5 - Gerar planilha de clientes
6 - Sair
```

## Exemplo de uso

O usuário pode cadastrar clientes informando:

* nome
* e-mail
* telefone

Depois, o sistema salva os dados no arquivo JSON e permite gerar uma planilha Excel com os clientes cadastrados.

A planilha gerada possui:

* cabeçalho formatado
* filtros automáticos
* largura de colunas ajustada
* tabela oficial do Excel
* dados organizados para uso administrativo

## Aprendizados aplicados

Durante o desenvolvimento deste projeto, foram praticados conceitos como:

* funções
* listas
* dicionários
* lista de dicionários
* validação de dados
* tratamento de erros
* leitura e escrita em JSON
* modularização de código
* exportação para CSV
* geração de planilha Excel
* uso da biblioteca openpyxl
* versionamento com Git
* publicação no GitHub

## Possíveis melhorias futuras

* Normalizar e-mails para evitar duplicidade com diferença entre letras maiúsculas e minúsculas
* Melhorar a validação de telefone
* Adicionar busca de clientes
* Adicionar CPF ou outro identificador único
* Criar histórico de alterações
* Criar banco de dados SQLite
* Criar interface web
* Criar dashboard de análise de clientes
* Evoluir para um sistema de agendamento
* Integrar com automações administrativas

## Posicionamento do projeto

Este projeto representa uma base inicial de um Mini CRM Administrativo.

Ele pode ser usado como ponto de partida para soluções maiores, como:

* controle de clientes
* sistema de agendamentos
* CRM simples
* relatórios administrativos
* automações internas
* análise de dados
* dashboards empresariais

## Autor

Cleber Batista

Projeto desenvolvido como parte da construção de uma base técnica em Python, análise de dados, automação de processos e soluções administrativas para a OONATECH.
