from pprint import pprint
import re

import requests
from bs4 import BeautifulSoup


URL = "https://coinmarketcap.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def obter_html(url):
    """Acessa a página e retorna o HTML."""
    resposta = requests.get(url, headers=HEADERS, timeout=10)
    resposta.raise_for_status()
    return resposta.text


def extrair_dados_criptomoedas(html):
    """Extrai os dados principais das criptomoedas listadas na página."""
    site = BeautifulSoup(html, "html.parser")
    tbody = site.find("tbody")

    if tbody is None:
        return {}

    linhas = tbody.find_all("tr")
    moedas = {}

    for linha in linhas:
        try:
            nome = linha.find(class_="coin-item-name").get_text(strip=True)
            codigo = linha.find(class_="coin-item-symbol").get_text(strip=True)

            valores = linha.find_all(string=re.compile(r"\$"))
            preco = valores[0]
            market_cap = valores[2]
            volume = valores[3]

            percentuais = linha.find_all(string=re.compile(r"%"))
            percentuais = ajustar_sinal_percentuais(percentuais)

            dados_moeda = {
                "Nome": nome,
                "Código": codigo,
                "Preço": preco,
                "Market Cap": market_cap,
                "Volume": volume,
                "1h %": percentuais[0],
                "24h %": percentuais[1],
                "7d %": percentuais[2],
            }

            moedas[nome] = dados_moeda

        except (AttributeError, IndexError, KeyError):
            continue

    return moedas


def ajustar_sinal_percentuais(percentuais):
    """Mantém a lógica original de identificar percentuais negativos pela classe CSS."""
    percentuais_ajustados = []

    for percentual in percentuais:
        classes = percentual.parent.get("class", [])
        valor = str(percentual)

        if "fDGzbr" in classes:
            valor = f"-{valor}"

        percentuais_ajustados.append(valor)

    return percentuais_ajustados


def main():
    html = obter_html(URL)
    moedas = extrair_dados_criptomoedas(html)
    pprint(moedas)


if __name__ == "__main__":
    main()
