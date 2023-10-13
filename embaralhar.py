import random

def embaralhar_palavras(texto):
    palavras = texto.split()
    texto_embaralhado = []

    for palavra in palavras:
        if len(palavra) > 2:
            letras_intermediarias = list(palavra[1:-1])
            random.shuffle(letras_intermediarias)
            palavra_embaralhada = palavra[0] + ''.join(letras_intermediarias) + palavra[-1]
            texto_embaralhado.append(palavra_embaralhada)
        else:
            texto_embaralhado.append(palavra)

    return ' '.join(texto_embaralhado)

texto_original = input("Digite o texto que você deseja embaralhar: ")
texto_embaralhado = embaralhar_palavras(texto_original)
print("Texto embaralhado: ", texto_embaralhado)

