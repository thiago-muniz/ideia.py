import urllib
import urllib.request
import re

def pegar_cotação_Dólar():

    # pegar contúdo da página
    try:
        site = urllib.request.urlopen('https://www.bcb.gov.br/')
        site = site.read()
    except urllib.error.URLError:
        print('Deu erro')
    else:
        #print('Deu certo')
        # obter valor de venda
        taxa_compra, taxa_venda = re.findall('[0,9],[0,9][0,9][0,9][0,9]', site)

        # retornando os valores
        return (taxa_compra, taxa_venda)


# Programa Principal
print(pegar_cotação_Dólar())