import re
import requests

requisicao = requests.get('https://portal.trt12.jus.br/noticias/contatos-das-unidades-judiciarias')
padrão = re.findall(r"[\w-]+@\w+\.\w+\.\w.", requisicao.text)

if padrão:
    print(padrão)
else:
    print('padrão não encontrado')
