from random import randint
from time import sleep

# CABEÇALHO
print('-' * 40)
print(' BEM VINDO AO JOGO DE CARTAS 21 ')
print('-' * 40)

# valor = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
#          '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
naipe = ['Espadas', 'Copas', 'Paus', 'Ouros']
cartas = []

# for c in valor:
#     espadas = f'{c}' + ' de Espadas'
#     copas = f'{c}' + ' de Copas'
#     paus = f'{c}' + ' de Paus'
#     ouros = f'{c}' + ' de Ouros'
#     cartas.append(espadas)
#     cartas.append(copas)
#     cartas.append(paus)
#     cartas.append(ouros)
# print(cartas.__len__())

# SORTEIO DE 2 CARTAS (VALORES E NAIPES)
sorteio_valor1 = randint(1, 10)
sorteio_valor2 = randint(1, 10)
sorteio_naipe1 = randint(0, 3)
sorteio_naipe2 = randint(0, 3)

# PRINTS DE VERIFICAÇÃO
# print('Sorteio cartas: ', end='')
# print(sorteio_valor1, sorteio_valor2)
# print('Soteio Naipes: ', end='')
# print(sorteio_naipe1, sorteio_naipe2)

print('EMBARALHANDO AS CARTAS...')
sleep(1)
print(f'{sorteio_valor1} de {naipe[sorteio_naipe1]}')
sleep(1)
print(f'{sorteio_valor2} de {naipe[sorteio_naipe2]}')
sleep(1)

print()
soma = sorteio_valor1 + sorteio_valor2
print(f'A soma das duas cartas: {soma}.')
print()
print('-' * 40)

somaFinal = soma + 0
vitorias = 0



while True:
    comprar = str(input('Deseja comprar mais uma?[S/N] ')).upper().strip()[0]
    print()
    if comprar == 'S':
        sorteio_valorExtra = randint(1, 10)
        sorteio_naipeExtra = randint(0, 3)
        print(f'Carta Extra Sorteada: {sorteio_valorExtra} de {naipe[sorteio_naipeExtra]}')
        print()
        somaFinal += sorteio_valorExtra
        print(f'Soma atual: {somaFinal}')
        print('-' * 40)
        if somaFinal == 21:
            print('Parabéns, você ganhou!'.upper())
            print('-' * 40)
            vitorias += 1
            # continuar = str(input('Deseja jogar de novo?[S/N] ')).strip().upper()[0]
            # if continuar == 'S':
            #     somaFinal = 0
            #     break
            # else:
            #     print('ERRO! Digite "S" para SIM ou "N" para NÃO!')
        if somaFinal > 21:
            print('Puxa que pena, estourou! Você perdeu!'.upper())
            break
        else:
            continue
    elif comprar == 'N':
        break
    else:
        print('ERRO! Digite "S" para SIM ou "N" para NÃO!')
        continue

# ENCERRAMENTO DO PROGRAMA
print('-' * 40)
sleep(1)
print('ENCERRANDO O PROGRAMA...')
sleep(1)
print(f'Total de Vitórias: {vitorias}')
print()