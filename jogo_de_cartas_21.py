from random import randint
from time import sleep

def linha(tam=42, ):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

# def verificacaoSN(msg):
#     while True:
#         try:
#             n = str(input(msg))
#         except (ValueError, TypeError):
#             print('\033[31mERRO! Digite um número inteiro válido.\033[m')
#             continue
#         except (KeyboardInterrupt):
#             print('\n\033[31mEntrada de dados interrompida pelo usuário!\033[m')
#             return 0
#         else:
#             return n
cabecalho(' BEM VINDO AO JOGO DE CARTAS 21 ')

nome_Player1 = str(input('Digite seu nome/nickname: ')).title().strip()
print()

valor = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
naipe = ['Espadas', 'Copas', 'Paus', 'Ouros']


# SORTEIO DE 2 CARTAS (VALORES E NAIPES)
sorteio_valor1 = valor[randint(0, 12)]
sorteio_valor2 = valor[randint(0, 12)]

sorteio_naipe1 = randint(0, 3)
sorteio_naipe2 = randint(0, 3)


# MOSTRANDO O VALOR DA CARTA E O NAIPE
print('EMBARALHANDO AS CARTAS...')
sleep(1)

carta1 = f'{sorteio_valor1} de {naipe[sorteio_naipe1]}'
print(carta1)
sleep(1)

carta2 = f'{sorteio_valor2} de {naipe[sorteio_naipe2]}'
print(carta2)
sleep(1)

cartas_Player1 = []
cartas_Player1.append(carta1)
cartas_Player1.append(carta2)
print(cartas_Player1)


# CONDIÇÕES DAS CARTAS ALFABÉTICAS
if sorteio_valor1 == 'J':
    sorteio_valor1 = 10
if sorteio_valor1 == 'Q':
    sorteio_valor1 = 10
if sorteio_valor1 == 'K':
    sorteio_valor1 = 10

if sorteio_valor2 == 'J':
    sorteio_valor2 = 10
if sorteio_valor2 == 'Q':
    sorteio_valor2 = 10
if sorteio_valor2 == 'K':
    sorteio_valor2 = 10

if sorteio_valor1 == 'A':
    sorteio_valor1 = 1
if sorteio_valor2 == 'A':
    sorteio_valor2 = 1


print()
soma1 = sorteio_valor1 + sorteio_valor2
print(f'A soma das duas cartas: {soma1}.')
print()
print('-' * 40)

somaFinal_Player1 = soma1 + 0
vitoriasP1 = 0
vitoriasP2 = 0

while True:
    comprar = str(input(f'Deseja comprar mais uma carta {nome_Player1}? [S/N] ')).upper().strip()[0]
    print()
    if comprar == 'S':
        sorteio_valorExtra = valor[randint(0, 12)]
        sorteio_naipeExtra = randint(0, 3)
        carta_Extra = f'{sorteio_valorExtra} de {naipe[sorteio_naipeExtra]}'
        print(f'Carta Extra Sorteada: {carta_Extra}')
        print()

        if sorteio_valorExtra == 'J':
            sorteio_valorExtra = 10
        if sorteio_valorExtra == 'Q':
            sorteio_valorExtra = 10
        if sorteio_valorExtra == 'K':
            sorteio_valorExtra = 10
        if sorteio_valorExtra == 'A':
            sorteio_valorExtra = 1

        cartas_Player1.append(carta_Extra)
        print(f'Cartas do jogador {nome_Player1}: {cartas_Player1}')

        somaFinal_Player1 += sorteio_valorExtra
        print()
        print(f'Soma total: {somaFinal_Player1}')
        print('-' * 40)
        if somaFinal_Player1 == 21:
            print('Parabéns, você ganhou!'.upper())
            print('-' * 40)
            vitoriasP1 += 1
            break
            # continuar = str(input('Deseja jogar de novo?[S/N] ')).strip().upper()[0]
            # if continuar == 'S':
            #     somaFinal = 0
            #     break
            # else:
            #     print('ERRO! Digite "S" para SIM ou "N" para NÃO!')
        if somaFinal_Player1 > 21:
            print('Puxa que pena, estourou! Você perdeu!'.upper())
            break
        else:
            continue
    elif comprar == 'N':
        print(f'O jogador {nome_Player1} decidiu parar com a soma total de {somaFinal_Player1}.')
        print(f'Suas cartas foram: {cartas_Player1}')
        break
    else:
        print('ERRO! Digite "S" para SIM ou "N" para NÃO!')
        print()
        print('-' * 40)
        continue

# ENCERRAMENTO DO PROGRAMA
print('-' * 40)
sleep(1)
print('ENCERRANDO O PROGRAMA...')
sleep(1)
print(f'Total de Vitórias: {vitoriasP1}')
print()
print('Desenvolvido por: Danilo de Lúcio')