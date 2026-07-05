# Web Scraping de Criptomoedas

Projeto de estudos em Python que realiza web scraping no site CoinMarketCap para coletar informações básicas sobre criptomoedas listadas na página inicial.

O script acessa a página, interpreta o HTML com BeautifulSoup e organiza os dados extraídos em um dicionário Python.

## Objetivo de aprendizado

O objetivo do projeto é praticar conceitos iniciais de automação e coleta de dados na web, incluindo:

- Requisições HTTP com `requests`;
- Leitura e interpretação de HTML com `BeautifulSoup`;
- Uso de expressões regulares com `re`;
- Organização de dados em dicionários;
- Separação simples de responsabilidades em funções;
- Estrutura básica de projeto para publicação no GitHub.

## Tecnologias utilizadas

- Python
- Requests
- BeautifulSoup4
- Regex, biblioteca nativa `re`

## Funcionalidades

O projeto coleta, quando disponíveis na página, os seguintes dados:

- Nome da criptomoeda;
- Código ou símbolo;
- Preço atual;
- Market Cap;
- Volume de negociação;
- Variação percentual em 1 hora;
- Variação percentual em 24 horas;
- Variação percentual em 7 dias.

## Estrutura do projeto

```text
web-scraping-criptomoedas/
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    └── web_scraping.py
```

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/web-scraping-criptomoedas.git
```

2. Acesse a pasta do projeto:

```bash
cd web-scraping-criptomoedas
```

3. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute o script:

```bash
python src/web_scraping.py
```

## Observações

Este é um projeto de estudos. Sites como o CoinMarketCap podem alterar a estrutura do HTML, nomes de classes CSS ou regras de acesso. Por isso, o script pode precisar de ajustes caso a página seja modificada.

O projeto não utiliza API oficial. A coleta é feita diretamente a partir do HTML público da página.
