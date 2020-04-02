# ------------------------------------------------------------- #
#                                         PyCoinAPI             #
#                                       Github:@WeDias          #
#                                    Licença: MIT License       #
#                                Copyright © 2020 Wesley Dias   #
# ------------------------------------------------------------- #

# Fonte: CoinMarketCap, https://coinmarketcap.com/

import requests
from bs4 import BeautifulSoup


def remover_virgulas(string):
    """
    :param string: string que terá suas vírgulas removidas
    :return: string sem vírgulas
    """
    if string.find(',') > 0:
        string = string.replace(',', '')

    return string


def buscar_dados(criptomoeda):
    """
    :param criptomoeda: Nome da criptomoeda para buscar os dados
    :return: dicionário com os dados da criptomoeda
    """
    nome = criptomoeda.lower()
    resposta = requests.get(f'https://coinmarketcap.com/currencies/{nome}/')
    dados = BeautifulSoup(resposta.text, 'html.parser')

    # ------------------------------------------------------------------------------------------------------------------
    # rank de mercado da criptomoeda
    rank_mercado = dados.find(class_='cmc-label cmc-label--success sc-13jrx81-0 FVuRP').get_text()
    rank_mercado = rank_mercado.replace('Rank ', '')
    rank_mercado = int(rank_mercado)

    # ------------------------------------------------------------------------------------------------------------------
    # preço em dólar
    preco = dados.find(class_='cmc-details-panel-price__price').get_text()[1:]
    preco = float(remover_virgulas(preco))

    # ------------------------------------------------------------------------------------------------------------------
    # variação da criptomoeda em relação ao dólar
    variacao = dados.find(class_='cmc--change-negative cmc-details-panel-price__price-change')
    if variacao is None:
        variacao = dados.find(class_='cmc--change-positive cmc-details-panel-price__price-change').get_text()[2:-2]
    else:
        variacao = variacao.get_text()[2:-2]
    variacao = float(variacao)

    # ------------------------------------------------------------------------------------------------------------------
    # preço em bitcoin
    preco_btc = dados.find(class_='cmc-details-panel-price__crypto-price').get_text()
    preco_btc = preco_btc.split()
    preco_btc = preco_btc[0]
    preco_btc = float(remover_virgulas(preco_btc))
    retornar = {'rank': rank_mercado, 'nome': nome, 'preco': preco, 'variação': variacao, 'preco_btc': preco_btc}

    return retornar
