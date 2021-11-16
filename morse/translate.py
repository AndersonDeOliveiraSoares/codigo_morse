from constants.constantes import CM_DICT
import re


def traduzir(texto):
    try:
        resposta = ''
        frase = texto.split(' ')
        for codigo in frase:
            if verificar_integridade(codigo) and codigo.strip() != '':
                resposta = resposta + CM_DICT[codigo]
            else:
                raise ValueError
        return resposta
    except ValueError:
        return "Erro traduzindo a mensagem"


def verificar_integridade(strg, search=re.compile(r'[^0-9.-]').search):
    return not bool(search(strg))
