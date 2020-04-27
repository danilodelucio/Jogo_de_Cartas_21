from funcoes import *
from random import randint
from time import sleep

# IDIOMA DO JOGO
language = 0
while True:
    try:
        language = int(input('[1] ENGLISH\n[2] PORTUGUÊS\n-> '))
    except:
        continue
    if language == 1:
        linha()
        print('<<< English language selected >>>')
        linha()
        break
    elif language == 2:
        linha()
        print('<<< Idioma em Português selecionado >>>')
        linha()
        break

idiom(language,
      ' WELCOME TO 21 CARD GAME \n',
      ' BEM VINDO AO JOGO DE CARTAS 21 \n')

# NOME DO JOGADOR
nome_Player1 = ''
while True:
    try:
        if language == 1:
            nome_Player1 = str(input('Type your name: ')).title().strip()
        elif language == 2:
            nome_Player1 = str(input('Digite seu nome: ')).title().strip()
    except:
        msgERROR(language)
    if nome_Player1.isnumeric():
        continue
    if nome_Player1 != '':
        break

print()

# ACUMULADORES 01
vitoriasP1 = derrotas = empates = partidas = 0

while True:
    valor = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    naipe = []
    if language == 1:
        naipe = ['Spades', 'Hearts', 'Clubs', 'Dimonds']
    elif language == 2:
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
            sorteio_naipe2_BOT = randint(0, 3)
        elif sorteio_naipe2_BOT != sorteio_naipe1_BOT:
            break

    # MOSTRANDO O VALOR DA CARTA E O NAIPE

    idiom(language,
          'SHUFFLING THE CARDS...',
          'EMBARALHANDO AS CARTAS...')

    print()
    sleep(1)

    idiom(language,
          f'Cards from the player {nome_Player1}:',
          f'Cartas do jogador {nome_Player1}:')

    sleep(1)
    de = ''
    if language == 1:
        de = 'of'
    elif language == 2:
        de = 'de'

    carta1 = f'{sorteio_valor1} {de} {naipe[sorteio_naipe1]}'
    print(carta1)
    sleep(1)
    carta2 = f'{sorteio_valor2} {de} {naipe[sorteio_naipe2]}'
    print(carta2)
    sleep(1)
    print()
    cartas_Player1 = [carta1, carta2]

    idiom(language,
          f'Cards from BOT:',
          f'Cartas do BOT:')

    sleep(1)
    carta3 = f'{sorteio_valor1_BOT} {de} {naipe[sorteio_naipe1_BOT]}'
    print(carta3)
    sleep(1)
    carta4 = f'{sorteio_valor2_BOT} {de} {naipe[sorteio_naipe2_BOT]}'
    print(carta4)
    sleep(1)
    cartas_BOT = [carta3, carta4]

    # SOMA DAS CARTAS
    print()
    linha()
    soma1 = validacaoLetras(sorteio_valor1) + validacaoLetras(sorteio_valor2)
    soma_BOT = validacaoLetras(sorteio_valor1_BOT) + validacaoLetras(sorteio_valor2_BOT)

    if language == 1:
        print(f'The total sum of the two cards from {nome_Player1}: {soma1}')
        print()
        print(f'The total sum of the two cards from BOT: {soma_BOT}')
    elif language == 2:
        print(f'Soma total das duas cartas do {nome_Player1}: {soma1}')
        print()
        print(f'Soma total das duas cartas do BOT: {soma_BOT}')
    linha()

    # ACUMULADORES 02
    somaFinal_Player1 = soma1 + 0
    somaFinal_BOT = soma_BOT + 0
    jogadaParada_BOT = 0

    while True:
        comprar = ''
        while True:
            try:
                if language == 1:
                    comprar = str(input(f'Do you wish to take another card {nome_Player1}? [Y/N] ')).upper().strip()[0]
                    if comprar == 'Y':
                        comprar = 'S'
                elif language == 2:
                    comprar = str(input(f'Deseja comprar mais uma carta {nome_Player1}? [S/N] ')).upper().strip()[0]
            except:
                msgERROR(language)
            if comprar.isnumeric():
                continue
            elif comprar == 'N' or comprar == 'S':
                break

        if comprar == 'S':
            # COMPRAR CARTA EXTRA
            sorteio_valorExtra = valor[randint(0, 12)]
            sorteio_naipeExtra = randint(0, 3)
            carta_Extra = f'{sorteio_valorExtra} {de} {naipe[sorteio_naipeExtra]}'
            sleep(1)
            print()

            idiom(language,
                  f'Extra card: {carta_Extra}.',
                  f'Carta Extra Sorteada: {carta_Extra}.')
            print()

            cartas_Player1.append(carta_Extra)
            somaFinal_Player1 += validacaoLetras(sorteio_valorExtra)

            sleep(1)
            idiom(language,
                  f'Total sum: {somaFinal_Player1}.',
                  f'Soma total: {somaFinal_Player1}.')
            linha()

            if somaFinal_Player1 == 21:
                vitoria(language)
                vitoriasP1 += 1
                status(language, cartas_BOT, cartas_Player1, vitoriasP1)
                break

            if somaFinal_Player1 > 21:
                Player1_Estourou(language)
                derrotas += 1
                status(language, cartas_BOT, cartas_Player1, vitoriasP1)
                break

            if somaFinal_Player1 == somaFinal_BOT and jogadaParada_BOT == 1:
                empate(language)
                empates += 1
                status(language, cartas_BOT, cartas_Player1, vitoriasP1)
                break

        elif comprar == 'N':
            paradaPlayer(language, nome_Player1, somaFinal_Player1)

        if jogadaParada_BOT == 1:
            idiom(language,
                  f'The BOT stopped in {somaFinal_BOT}.',
                  f'O BOT tinha parado no valor {somaFinal_BOT}.')
            linha()

            if somaFinal_BOT < somaFinal_Player1 < 21:
                break

            else:
                continue

        # JOGADA DO BOT
        sleep(1)
        idiom(language,
              "Now it's BOT's turn...",
              'Agora é a vez do BOT...')
        sleep(1)

        if somaFinal_BOT == 21:
            BOT_venceu(language)
            derrotas += 1
            status(language, cartas_BOT, cartas_Player1, vitoriasP1)
            break

        if somaFinal_BOT > 21:
            BOT_Estourou(language)
            vitoriasP1 += 1
            status(language, cartas_BOT, cartas_Player1, vitoriasP1)
            break

        if comprar == 'S' and somaFinal_BOT == somaFinal_Player1 and somaFinal_BOT >= 18:
            paradaBOT(language, somaFinal_BOT)
            jogadaParada_BOT = 1
            print()
            linha()
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

            cartas_BOT.append(carta_Extra_BOT)
            somaFinal_BOT += validacaoLetras(sorteio_valorExtra_BOT)

            sleep(1)
            print(f'Soma total das cartas do BOT: {somaFinal_BOT}.')
            linha()

            if somaFinal_BOT == 21:
                print('Poxa, que pena! O BOT venceu!')
                derrotas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
                break

            if somaFinal_BOT > 21:
                print(f'Vixe... o BOT estourou, você venceu!')
                vitoriasP1 += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
                break

            elif somaFinal_BOT > somaFinal_Player1:
                continue

        if comprar == 'N' and somaFinal_BOT == somaFinal_Player1:
            print()
            sleep(1)
            print(f'Eita, deu empate! Ele não quis comprar!')
            empates += 1
            print()
            print(f'As cartas do BOT: {cartas_BOT}.')
            print(f'Suas cartas: {cartas_Player1}.')
            print()
            print(f'Total de Vitórias: {vitoriasP1}.')
            linha()
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

            cartas_BOT.append(carta_Extra_BOT)
            somaFinal_BOT += sorteio_valorExtra_BOT

            sleep(1)
            print(f'Soma total das cartas do BOT: {somaFinal_BOT}.')
            linha()

            if somaFinal_BOT == 21:
                print('Poxa, que pena! O BOT venceu!')
                derrotas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
                break

            if somaFinal_BOT > 21:
                print(f'Vixe... o BOT estourou, você venceu!')
                vitoriasP1 += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
                break

            elif somaFinal_BOT > somaFinal_Player1:
                break

            elif somaFinal_BOT == somaFinal_Player1:
                print()
                sleep(1)
                print(f'Eita, deu empate!')
                empates += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
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

            cartas_BOT.append(carta_Extra_BOT)
            somaFinal_BOT += validacaoLetras(sorteio_valorExtra_BOT)

            sleep(1)
            print(f'Soma total das cartas do BOT: {somaFinal_BOT}.')
            linha()

            if somaFinal_BOT == 21:
                print('Poxa, que pena! O BOT venceu!')
                derrotas += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
                break

            if somaFinal_BOT > 21:
                print(f'Vixe... o BOT estourou, você venceu!')
                vitoriasP1 += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
                break

            if comprar == 'N' and somaFinal_BOT == somaFinal_Player1:
                print()
                sleep(1)
                print(f'Eita, deu empate! Ele não quis comprar!')
                empates += 1
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
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
            linha()
            continue

    # DEFININDO VENCEDOR

    if somaFinal_BOT < somaFinal_Player1 < 21 and jogadaParada_BOT == 1:
        sleep(1)
        print()
        print('Parabéns, você venceu!')
        vitoriasP1 += 1
        print()
        linha()

    if somaFinal_Player1 < somaFinal_BOT < 21:
        print(f'Vitória do BOT, com a soma total de {somaFinal_BOT}.')
        derrotas += 1
        sleep(1)
        print()
        print(f'As cartas do BOT: {cartas_BOT}.')
        print(f'Suas cartas: {cartas_Player1}.')
        linha()

    # CONTINUAR
    sleep(1)
    continuar = ''
    while True:
        try:
            continuar = str(input('Deseja jogar de novo? [S/N] ')).upper().strip()[0]
        except:
            msgERROR(language)
        if comprar.isnumeric():
            continue
        elif comprar == 'N' or comprar == 'S':
            partidas += 1
            break

    if continuar == 'N':
        break
    elif continuar == 'S':
        linha()
        print()
        continue
    else:
        print()
        print('ERRO! Digite "S" para SIM ou "N" para NÃO!')

# ENCERRAMENTO DO PROGRAMA
linha()
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
