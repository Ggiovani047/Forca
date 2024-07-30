import random
import os
import sys

words = [
    {'Nome': 'BANANA', 'Dica': 'Fruta', 'Dificuldade': 'Fácil'},
    {'Nome': 'ELEFANTE', 'Dica': 'Animal', 'Dificuldade': 'Médio'},
    {'Nome': 'ASTRONAUTA', 'Dica': 'Profissão', 'Dificuldade': 'Difícil'},
    {'Nome': 'CACHORRO', 'Dica': 'Animal de estimação', 'Dificuldade': 'Fácil'},
    {'Nome': 'ESQUILO', 'Dica': 'Animal', 'Dificuldade': 'Médio'},
    {'Nome': 'BIBLIOTECARIO', 'Dica': 'Profissão', 'Dificuldade': 'Difícil'},
    {'Nome': 'ABOBORA', 'Dica': 'Vegetal', 'Dificuldade': 'Fácil'},
    {'Nome': 'HELICOPTERO', 'Dica': 'Meio de transporte', 'Dificuldade': 'Médio'},
    {'Nome': 'PALEONTOLOGO', 'Dica': 'Profissão', 'Dificuldade': 'Difícil'},
    {'Nome': 'CENOURA', 'Dica': 'Vegetal', 'Dificuldade': 'Fácil'},
    {'Nome': 'GIRAFA', 'Dica': 'Animal', 'Dificuldade': 'Médio'},
    {'Nome': 'METEOROLOGIA', 'Dica': 'Ciência', 'Dificuldade': 'Difícil'},
    {'Nome': 'GATO', 'Dica': 'Animal de estimação', 'Dificuldade': 'Fácil'},
    {'Nome': 'ORNITORRINCO', 'Dica': 'Animal', 'Dificuldade': 'Médio'},
    {'Nome': 'ELETROENCEFALOGRAMA', 'Dica': 'Exame médico', 'Dificuldade': 'Difícil'}
]

def adicionar_tracos(words):
    for word in words:
        nome = word['Nome']
        traços = '_' * len(nome)
        word['Tracos'] = traços

adicionar_tracos(words)
print('Jogo de Forca!')

palavra_escolhida = random.choice(words)
letras_erradas = []
letras_acertadas = []
letras_tentadas = []
chances = 6

if len(palavra_escolhida['Nome']) <= 5:
    chances = 3
elif len(palavra_escolhida['Nome']) >= 6 and len(palavra_escolhida['Nome']) <= 11:
    chances = 6
elif len(palavra_escolhida['Nome']) >= 12:
    chances = 10
else:
    print('Algo deu errado')
    sys.exit(1)

def exibir_palavra(palavra, letras_acertadas):
    resultado = ''
    for letra in palavra:
        if letra in letras_acertadas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

contador = 0

while True:
    print(f'A palavra tem {len(palavra_escolhida["Nome"])} letras')
    print(f'A dica é: {palavra_escolhida["Dica"]}')
    print(f'A dificuldade é: {palavra_escolhida["Dificuldade"]}')
    print(f'\nPalavra: {exibir_palavra(palavra_escolhida["Nome"], letras_acertadas)}')
    print(f'Letras erradas: {", ".join(letras_erradas)}')
    print(f'Chances restantes: {chances}')
    print('\n____________________________________________________')
    
    letra = input('Qual a letra você deseja tentar? ').strip().upper()
    if contador > 0:
        os.system('cls' if os.name == 'nt' else 'clear')

    contador += 1

    if not letra.isalpha() or len(letra) != 1:
        print('Entrada inválida. Digite apenas uma letra.')
        continue

    if letra in letras_tentadas:
        print('Você já tentou essa letra. Tente outra.')
        continue

    letras_tentadas.append(letra)
    
    if letra in palavra_escolhida['Nome']:
        print(f'Você acertou a letra {letra}')
        letras_acertadas.append(letra)
    else:
        print('Essa letra não está na palavra.')
        chances -= 1
        letras_erradas.append(letra)

    if exibir_palavra(palavra_escolhida['Nome'], letras_acertadas) == palavra_escolhida['Nome']:
        print(f'Parabéns! Você acertou a palavra {palavra_escolhida["Nome"]}!')
        break

    if chances <= 0:
        print('Suas chances acabaram!')
        print(f'A palavra era {palavra_escolhida["Nome"]}.')
        break
