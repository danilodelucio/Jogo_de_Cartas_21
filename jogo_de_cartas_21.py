from random import randint
from time import sleep

def linha(tam=42, ):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

cabecalho(' BEM VINDO AO JOGO DE CARTAS 21 ')

# def sorteio()

valor = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
naipe = ['Espadas', 'Copas', 'Paus', 'Ouros']
cartas = []

# SORTEIO DE 2 CARTAS (VALORES E NAIPES)
sorteio_valor1 = valor[randint(0, 12)]
sorteio_valor2 = valor[randint(0, 12)]

sorteio_naipe1 = randint(0, 3)
sorteio_naipe2 = randint(0, 3)


# MOSTRANDO O VALOR DA CARTA E O NAIPE
print('EMBARALHANDO AS CARTAS...')
sleep(1)
print(f'{sorteio_valor1} de {naipe[sorteio_naipe1]}')
sleep(1)
print(f'{sorteio_valor2} de {naipe[sorteio_naipe2]}')
sleep(1)

# CONDIÇÕES DAS CARTAS AFABÉTICAS
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

somaFinal = soma1 + 0
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
print('Desenvolvido por: Danilo de Lúcio')