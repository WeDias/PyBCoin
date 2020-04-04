# ------------------------------------------------------------- #
#                                       Monitor-Console         #
#                                       Github:@WeDias          #
#                                    Licença: MIT License       #
#                                Copyright © 2020 Wesley Dias   #
# ------------------------------------------------------------- #

import PyBCoin
from time import sleep

print('Monitor de preços'.center(50, '-'))
criptomoeda = str(input('Criptomoeda: '))
while True:
    try:
        coin = PyBCoin.buscar_dados(criptomoeda)
        print(f'''\rPreço: U${coin["preco"]} Variação: {coin["variação"]}%''', end='')
        sleep(1)

    except:
        sleep(1)
        criptomoeda = str(input('\rDigite um nome válido: '))
