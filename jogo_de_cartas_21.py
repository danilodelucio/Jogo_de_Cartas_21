from random import randint
from time import sleep

def linha(tam=70):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(70))
    print(linha())

tamanhoLinha = 70

cabecalho(' BEM VINDO AO JOGO DE CARTAS 21 ')

nome_Player1 = str(input('Digite seu nome: ')).title().strip()
print()

# ACUMULADORES 01
vitoriasP1 = derrotas = empates = 0
partidas = 1

while True:
    valor = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    naipe = ['Espadas', 'Copas', 'Paus', 'Ouros']


    # SORTEIO DE 2 CARTAS (VALORES E NAIPES) / CARTAS DE ENTRADA
    sorteio_valor1 = valor[randint(0, 12)]
    sorteio_valor2 = valor[randint(0, 12)]
    while True:
        if sorteio_valor2 == sorteio_valor1:
            sorteio_valor2 = valor[randint(0, 12)]
        elif sorteio_valor2 != sorteio_valor1:
            break

    sorteio_valor1_BOT = valor[randint(0, 12)]
    sorteio_valor2_BOT = valor[randint(0, 12)]
    while True:
        if sorteio_valor2_BOT == sorteio_valor1_BOT:
            sorteio_valor2_BOT = valor[randint(0, 12)]
        elif sorteio_valor2_BOT != sorteio_valor1_BOT:
            break

    sorteio_naipe1 = randint(0, 3)
    sorteio_naipe2 = randint(0, 3)
    while True:
        if sorteio_naipe2 == sorteio_naipe1:
            sorteio_naipe2 = randint(0, 3)
        elif sorteio_naipe2 != sorteio_naipe1:
            break

    sorteio_naipe1_BOT = randint(0, 3)
    sorteio_naipe2_BOT = randint(0, 3)
    while True:
        if sorteio_naipe2_BOT == sorteio_naipe1_BOT:
            sorteio_naipe2_BOT = randint(0 , 3)
        elif sorteio_naipe2_BOT != sorteio_naipe1_BOT:
            break


    # MOSTRANDO O VALOR DA CARTA E O NAIPE
    print('EMBARALHANDO AS CARTAS...')
    print()
    sleep(1)

    print(f'Cartas do jogador {nome_Player1}:')
    sleep(1)
    carta1 = f'{sorteio_valor1} de {naipe[sorteio_naipe1]}'
    print(carta1)
    sleep(1)
    carta2 = f'{sorteio_valor2} de {naipe[sorteio_naipe2]}'
    print(carta2)
    sleep(1)
    print()
    cartas_Player1 = [carta1, carta2]
    # print(cartas_Player1)
    # print()

    print(f'Cartas do BOT:')
    sleep(1)
    carta3 = f'{sorteio_valor1_BOT} de {naipe[sorteio_naipe1_BOT]}'
    print(carta3)
    sleep(1)
    carta4 = f'{sorteio_valor2_BOT} de {naipe[sorteio_naipe2_BOT]}'
    print(carta4)
    sleep(1)
    # print()
    cartas_BOT = [carta3, carta4]
    # print(cartas_BOT)

    # CONDIÇÕES DAS CARTAS ALFABÉTICAS PARA O JOGADOR
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

    # CONDIÇÕES DAS CARTAS ALFABÉTICAS PARA O BOT
    if sorteio_valor1_BOT == 'J':
        sorteio_valor1_BOT = 10
    if sorteio_valor1_BOT == 'Q':
        sorteio_valor1_BOT = 10
    if sorteio_valor1_BOT == 'K':
        sorteio_valor1_BOT = 10

    if sorteio_valor2_BOT == 'J':
        sorteio_valor2_BOT = 10
    if sorteio_valor2_BOT == 'Q':
        sorteio_valor2_BOT = 10
    if sorteio_valor2_BOT == 'K':
        sorteio_valor2_BOT = 10

    if sorteio_valor1_BOT == 'A':
        sorteio_valor1_BOT = 1
    if sorteio_valor2_BOT == 'A':
        sorteio_valor2_BOT = 1

    # SOMA DAS CARTAS
    print()
    print('-' * tamanhoLinha)
    soma1 = sorteio_valor1 + sorteio_valor2
    soma_BOT = sorteio_valor1_BOT + sorteio_valor2_BOT
    print(f'Soma total das duas cartas do {nome_Player1}: {soma1}')
    print()
    print(f'Soma total das duas cartas do BOT: {soma_BOT}')
    print('-' * tamanhoLinha)

    # ACUMULADORES 02
    somaFinal_Player1 = soma1 + 0
    somaFinal_BOT = soma_BOT + 0
    jogadaParada_BOT = 0

    while True:
        comprar = str(input(f'Deseja comprar mais uma carta {nome_Player1}? [S/N] ')).upper().strip()[0]

        if comprar == 'S':
            sorteio_valorExtra = valor[randint(0, 12)]
            sorteio_naipeExtra = randint(0, 3)
            carta_Extra = f'{sorteio_valorExtra} de {naipe[sorteio_naipeExtra]}'
            sleep(1)
            print()
            print(f'Carta Extra Sorteada: {carta_Extra}.')
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
            somaFinal_Player1 += sorteio_valorExtra

            sleep(1)
            print(f'Soma total: {somaFinal_Player1}.')
            print('-' * tamanhoLinha)

            if somaFinal_Player1 == 21:
                print('Parabéns, você ganhou!'.upper())
                vitoriasP1 += 1
                partidas += 1
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

            if somaFinal_Player1 > 21:
                print('Puxa que pena, estourou! Você perdeu!')
                derrotas += 1
                partidas += 1
                print()
                sleep(1)
                print(f'Vitória do BOT, com a soma total de {somaFinal_BOT}.')
                sleep(1)
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print('-' * tamanhoLinha)
                break

            if somaFinal_Player1 == somaFinal_BOT and jogadaParada_BOT == 1:
                print()
                sleep(1)
                print(f'Eita, deu empate! Ele não quis comprar!')
                partidas += 1
                empates += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

        elif comprar == 'N':
            print()
            print(f'{nome_Player1} decidiu parar com a soma total de {somaFinal_Player1}.')
            sleep(1)
            print()
            print(f'Suas cartas foram: {cartas_Player1}.')
            print()
            print('-' * tamanhoLinha)

        else:
            print()
            print('ERRO! Digite "S" para SIM ou "N" para NÃO!')
            print()
            print('-' * tamanhoLinha)
            continue

        if jogadaParada_BOT == 1:
            print(f'O BOT tinha parado no valor {somaFinal_BOT}.')
            print('-' * tamanhoLinha)

            if somaFinal_BOT < somaFinal_Player1 < 21:
                break

            else:
                continue

        # JOGADA DO BOT
        sleep(1)
        print('Agora é a vez do BOT...')
        sleep(1)

        if somaFinal_BOT == 21:
            print('Poxa, que pena! O BOT venceu!')
            partidas += 1
            derrotas += 1
            print()
            print(f'As cartas do BOT: {cartas_BOT}.')
            print(f'Suas cartas: {cartas_Player1}.')
            print()
            print(f'Total de Vitórias: {vitoriasP1}.')
            print('-' * tamanhoLinha)
            break

        if somaFinal_BOT > 21:
            print(f'Vixe... o BOT estourou, você venceu!')
            vitoriasP1 += 1
            partidas += 1
            print()
            print(f'As cartas do BOT: {cartas_BOT}.')
            print(f'Suas cartas: {cartas_Player1}.')
            print()
            print(f'Total de Vitórias: {vitoriasP1}.')
            print('-' * tamanhoLinha)
            break

        if comprar == 'S' and somaFinal_BOT == somaFinal_Player1 and somaFinal_BOT >= 18:
            sleep(1)
            print()
            print(f'O BOT decidiu parar com a soma total de {somaFinal_BOT}')
            jogadaParada_BOT = 1
            print()
            print('-' * tamanhoLinha)
            continue

        if comprar == 'S' and somaFinal_BOT == somaFinal_Player1 and somaFinal_BOT < 18:
            print()
            print('O BOT está comprando mais uma carta... ')
            sorteio_valorExtra_BOT = valor[randint(0, 12)]
            sorteio_naipeExtra_BOT = randint(0, 3)
            carta_Extra_BOT = f'{sorteio_valorExtra_BOT} de {naipe[sorteio_naipeExtra_BOT]}'
            sleep(1)
            print()
            print(f'Carta Extra Sorteada: {carta_Extra_BOT}')
            print()

            if sorteio_valorExtra_BOT == 'J':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'Q':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'K':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'A':
                sorteio_valorExtra_BOT = 1

            cartas_BOT.append(carta_Extra_BOT)
            somaFinal_BOT += sorteio_valorExtra_BOT

            sleep(1)
            print(f'Soma total das cartas do BOT: {somaFinal_BOT}.')
            print('-' * tamanhoLinha)

            if somaFinal_BOT == 21:
                print('Poxa, que pena! O BOT venceu!')
                partidas += 1
                derrotas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

            if somaFinal_BOT > 21:
                print(f'Vixe... o BOT estourou, você venceu!')
                vitoriasP1 += 1
                partidas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

            elif somaFinal_BOT > somaFinal_Player1:
                continue

        if comprar == 'N' and somaFinal_BOT == somaFinal_Player1:
            print()
            sleep(1)
            print(f'Eita, deu empate! Ele não quis comprar!')
            partidas += 1
            empates += 1
            print()
            print(f'As cartas do BOT: {cartas_BOT}.')
            print(f'Suas cartas: {cartas_Player1}.')
            print()
            print(f'Total de Vitórias: {vitoriasP1}.')
            print('-' * tamanhoLinha)
            break

        while comprar == 'N' and somaFinal_BOT < somaFinal_Player1:
            print()
            print('O BOT está comprando mais uma carta... ')
            sorteio_valorExtra_BOT = valor[randint(0, 12)]
            sorteio_naipeExtra_BOT = randint(0, 3)
            carta_Extra_BOT = f'{sorteio_valorExtra_BOT} de {naipe[sorteio_naipeExtra_BOT]}'
            sleep(1)
            print()
            print(f'Carta Extra Sorteada: {carta_Extra_BOT}')
            print()

            if sorteio_valorExtra_BOT == 'J':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'Q':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'K':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'A':
                sorteio_valorExtra_BOT = 1

            cartas_BOT.append(carta_Extra_BOT)
            somaFinal_BOT += sorteio_valorExtra_BOT

            sleep(1)
            print(f'Soma total das cartas do BOT: {somaFinal_BOT}.')
            print('-' * tamanhoLinha)

            if somaFinal_BOT == 21:
                print('Poxa, que pena! O BOT venceu!')
                partidas += 1
                derrotas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

            if somaFinal_BOT > 21:
                print(f'Vixe... o BOT estourou, você venceu!')
                vitoriasP1 += 1
                partidas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

            elif somaFinal_BOT > somaFinal_Player1:
                break

            elif somaFinal_BOT == somaFinal_Player1:
                print()
                sleep(1)
                print(f'Eita, deu empate!')
                partidas += 1
                empates += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

        if comprar == 'N' and somaFinal_BOT == somaFinal_Player1:
            break

        if comprar == 'S' and somaFinal_BOT < somaFinal_Player1 and jogadaParada_BOT == 0:
            print()
            print('O BOT está comprando mais uma carta... ')
            sorteio_valorExtra_BOT = valor[randint(0, 12)]
            sorteio_naipeExtra_BOT = randint(0, 3)
            carta_Extra_BOT = f'{sorteio_valorExtra_BOT} de {naipe[sorteio_naipeExtra_BOT]}'
            sleep(1)
            print()
            print(f'Carta Extra Sorteada: {carta_Extra_BOT}')
            print()

            if sorteio_valorExtra_BOT == 'J':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'Q':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'K':
                sorteio_valorExtra_BOT = 10
            if sorteio_valorExtra_BOT == 'A':
                sorteio_valorExtra_BOT = 1

            cartas_BOT.append(carta_Extra_BOT)
            somaFinal_BOT += sorteio_valorExtra_BOT

            sleep(1)
            print(f'Soma total das cartas do BOT: {somaFinal_BOT}.')
            print('-' * tamanhoLinha)

            if somaFinal_BOT == 21:
                print('Poxa, que pena! O BOT venceu!')
                partidas += 1
                derrotas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

            if somaFinal_BOT > 21:
                print(f'Vixe... o BOT estourou, você venceu!')
                vitoriasP1 += 1
                partidas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

            if comprar == 'N' and somaFinal_BOT == somaFinal_Player1:
                print()
                sleep(1)
                print(f'Eita, deu empate! Ele não quis comprar!')
                partidas += 1
                empates += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                print('-' * tamanhoLinha)
                break

            if somaFinal_BOT < somaFinal_Player1:
                continue

        if comprar == 'N' and somaFinal_BOT > somaFinal_Player1:
            print()
            break

        if comprar == 'S' and somaFinal_BOT > somaFinal_Player1:
            sleep(1)
            print()
            print(f'O BOT decidiu parar com a soma total de {somaFinal_BOT}')
            jogadaParada_BOT = 1
            print()
            print('-' * tamanhoLinha)
            continue


    # DEFININDO VENCEDOR

    if somaFinal_BOT < somaFinal_Player1 < 21 and jogadaParada_BOT == 1:
        sleep(1)
        print()
        print('Parabéns, você venceu!')
        partidas += 1
        vitoriasP1 += 1
        print()
        print('-' * tamanhoLinha)

    if somaFinal_Player1 < somaFinal_BOT < 21:
        print(f'Vitória do BOT, com a soma total de {somaFinal_BOT}.')
        partidas += 1
        derrotas += 1
        sleep(1)
        print()
        print(f'As cartas do BOT: {cartas_BOT}.')
        print(f'Suas cartas: {cartas_Player1}.')
        print('-' * tamanhoLinha)

    # CONTINUAR
    sleep(1)
    continuar = str(input('Deseja jogar de novo? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    elif continuar == 'S':
        print('-' * tamanhoLinha)
        print()
        continue
    else:
        print()
        print('ERRO! Digite "S" para SIM ou "N" para NÃO!')


# ENCERRAMENTO DO PROGRAMA
print('-' * tamanhoLinha)
sleep(1)
print('ENCERRANDO O PROGRAMA...')
sleep(1)
print()
print(f'Total de Vitórias: {vitoriasP1}.')
print(f'Total de Derrotas: {derrotas}.')
print(f'Total de Empates: {empates}.')
print(f'Total de Partidas: {partidas}.')

sleep(1)
print()
print('Obrigado por jogar meu consagrado!')
print()
print('Desenvolvido por:\nDanilo de Lúcio')
print('Site: www.danilodelucio.com')
print('GitHub: www.github.com/danilodelucio')