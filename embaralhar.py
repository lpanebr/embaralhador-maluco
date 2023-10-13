import random
import sys

def get_next_int_by_range(word, start_value, ranges):
    sorted_ranges = sorted(ranges) 
    current_value = start_value
    for cur_max in sorted_ranges:
        if len(word) <=cur_max:
            return current_value
        current_value += 1
    return current_value

def get_word_parts(word, start_size, end_size):
    if start_size < 0 or end_size < 0 or start_size + end_size > len(word):
        return "Erro: Tamanhos inválidos."
    inicio = word[:start_size]
    meio = word[start_size:-end_size] if start_size + end_size < len(word) else ""
    fim = word[-end_size:] if end_size > 0 else ""
    return [inicio, meio, fim]

def embaralhar_palavras(texto):
    palavras = texto.split()
    texto_embaralhado = []

    for palavra in palavras:
        start_size = end_size = get_next_int_by_range(palavra, 0, [3,5,8,12])
        if len(palavra) >= start_size + end_size:
            partes = get_word_parts(palavra, start_size, end_size)
            meio = list(partes[1])
            random.shuffle(meio)
            palavra_embaralhada = partes[0] + ''.join(meio) + partes[2]
            texto_embaralhado.append(palavra_embaralhada)
        else:
            texto_embaralhado.append(palavra)

    return ' '.join(texto_embaralhado)

texto_original = sys.argv[1]
texto_embaralhado = embaralhar_palavras(texto_original)
print(texto_embaralhado)
