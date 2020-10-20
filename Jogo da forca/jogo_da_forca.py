import random
import time

palavras = ('casa', 'abelha', 'cachueira', 'porta', 'mesa', 'lixeira', 'cadeado', 'guarda')
palavras = ('casa', 'casa')
sorteio_palavras = random.choice(palavras)  # Pegando palavras aleatorias
letras = []
tentantiva = 5

acertou = False

print('='*20 + ' JOGO DA FORCA ' + '='*20 + '\n')

print('Sorteando um palavra...')
# time.sleep(1.5)  # Criando um pequeno cronometro
print(f'A palavra sorteada possui {len(sorteio_palavras)} letras\n')

# Fazendo um for para substiruir as letras sortiadas por traços
for i in range(0, len(sorteio_palavras)):
    letras.append('-')

# Laço de repetição que executara enquanto
while acertou == False:
    enter_letras = str(input('Entre com uma letra: '))

    # Pecorre a palavra sorteada e inserir a letra acertada
    for i in range(0, len(sorteio_palavras)):
        if enter_letras == sorteio_palavras[i]:
            letras[i] = enter_letras
        print(letras[i])
    # acertou = True

    # Pecorre a palavra sorteada e conpara se ainda existe algum taço
    # Caso tenha contunua o laço
    # for x in range(0, len(sorteio_palavras)):
    #     if letras[x] == '-':
    #         acertou = False

    # OBS -> Ao entra nessas linhas do codigo a intenção é que a cada letra errada o numero de
    # tentativas seja - 1, o que realmente acontece, porem tambem as tentativas estão sendo subtraidas
    # caso a letra estejam certas.
    if enter_letras == sorteio_palavras:
    	print('acertou mizeravi',sorteio_palavras)
    	acertou = True
        # tentantiva = tentantiva
    elif letras == list(sorteio_palavras):
    	print('acertou mizeravi',sorteio_palavras)
    	acertou = True
    elif enter_letras not in sorteio_palavras:
        tentantiva -= 1
        print(f'Você possui {tentantiva} Tentativas.')
        # Comparando as tentativas
        if tentantiva <= 0:
            print('enforcado')
            print(sorteio_palavras)
            break
    # print(letras)
    # print(sorteio_palavras)
    # print(list(sorteio_palavras))
