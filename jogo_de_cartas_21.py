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

# SINGLE PLAYER OR MULTIPLAYER MODE
playerMode = 0
while True:
    try:
        if language == 1:
            playerMode = int(input('[1] SINGLE PLAYER\n[2] 1 VS 1\n-> '))
        elif language == 2:
            playerMode = int(input('[1] UM JOGADOR\n[2] 1 CONTRA 1\n-> '))
    except:
        continue
    if playerMode == 1:
        linha()
        idiom(language,
              '<<< Single Player mode selected >>>',
              '<<< Modo de UM JOGADOR selecionado >>>')
        linha()
        break
    elif playerMode == 2:
        linha()
        idiom(language,
              '<<< 1 vs 1 mode selected >>>',
              '<<< Modo de 1 CONTRA 1 selecionado >>>')
        linha()
        break

# NAMES
nome_Player1 = ''
nome_Player2 = ''
if playerMode == 1:
    while True:
        try:
            if language == 1:
                nome_Player1 = str(input('Type your name: ')).title().strip()
            elif language == 2:
                nome_Player1 = str(input('Digite seu nome: ')).title().strip()
        except:
            msgERROR(language)
            continue
        if nome_Player1.isnumeric():
            msgERROR(language)
            continue
        elif nome_Player1 == '':
            msgERROR(language)
            continue
        else:
            break
if playerMode == 2:
    # PLAYER 1
    while True:
        try:
            if language == 1:
                nome_Player1 = str(input('Player1 name: ')).upper().strip()
            elif language == 2:
                nome_Player1 = str(input('Nome do Jogador1: ')).upper().strip()
        except:
            msgERROR(language)
            continue
        if nome_Player1 == '':
            msgERROR(language)
            continue
        elif nome_Player1.isnumeric():
            msgERROR(language)
            continue
        else:
            break

    # PLAYER 2
    while True:
        try:
            if language == 1:
                nome_Player2 = str(input('Player2 name: ')).upper().strip()
            elif language == 2:
                nome_Player2 = str(input('Nome do Jogador2: ')).upper().strip()
        except:
            msgERROR(language)
            continue
        if nome_Player2 == '':
            msgERROR(language)
            continue
        elif nome_Player2.isnumeric():
            msgERROR(language)
            continue
        else:
            break


print()

# ACUMULADORES 01
vitoriasP1 = vitoriasP2 = derrotas = empates = partidas = 0

# PLAYER 1 MODE
if playerMode == 1:
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
                paradaPlayer1(language, nome_Player1, somaFinal_Player1)

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

            if comprar == 'N' and somaFinal_BOT > somaFinal_Player1 and jogadaParada_BOT == 1:
                break

            if comprar == 'S' and somaFinal_BOT == somaFinal_Player1 and somaFinal_BOT >= 18:
                paradaBOT(language, somaFinal_BOT)
                jogadaParada_BOT = 1
                print()
                linha()
                continue

            if comprar == 'S' and somaFinal_BOT == somaFinal_Player1 and somaFinal_BOT < 18:
                # --------------------- / / ----------------------- #
                idiom(language,
                      'The BOT is taking a card... ',
                      'O BOT está comprando mais uma carta... ')
                sorteio_valor_extra_bot = valor[randint(0, 12)]
                sorteio_naipe_extra_bot = randint(0, 3)
                carta_extra_bot = f'{sorteio_valor_extra_bot} {de} {naipe[sorteio_naipe_extra_bot]}'
                sleep(1)
                print()
                idiom(language,
                      f'Extra card: {carta_extra_bot}',
                      f'Carta Extra Sorteada: {carta_extra_bot}')
                print()

                cartas_BOT.append(carta_extra_bot)
                somaFinal_BOT += validacaoLetras(sorteio_valor_extra_bot)

                sleep(1)
                idiom(language,
                      f'Total sum of the cards from BOT: {somaFinal_BOT}.',
                      f'Soma total das cartas do BOT: {somaFinal_BOT}.')
                linha()
                # --------------------- / / ----------------------- #

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

                elif somaFinal_BOT > somaFinal_Player1:
                    continue

            while comprar == 'N' and somaFinal_BOT == somaFinal_Player1 and somaFinal_BOT < 12:

                # --------------------- / / ----------------------- #
                idiom(language,
                      'The BOT is taking a card... ',
                      'O BOT está comprando mais uma carta... ')
                sorteio_valor_extra_bot = valor[randint(0, 12)]
                sorteio_naipe_extra_bot = randint(0, 3)
                carta_extra_bot = f'{sorteio_valor_extra_bot} {de} {naipe[sorteio_naipe_extra_bot]}'
                sleep(1)
                print()
                idiom(language,
                      f'Extra card: {carta_extra_bot}',
                      f'Carta Extra Sorteada: {carta_extra_bot}')
                print()

                cartas_BOT.append(carta_extra_bot)
                somaFinal_BOT += validacaoLetras(sorteio_valor_extra_bot)

                sleep(1)
                idiom(language,
                      f'Total sum of the cards from BOT: {somaFinal_BOT}.',
                      f'Soma total das cartas do BOT: {somaFinal_BOT}.')
                linha()
                # --------------------- / / ----------------------- #

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

                elif somaFinal_BOT > somaFinal_Player1:
                    break

            if comprar == 'N' and somaFinal_BOT == somaFinal_Player1:
                empate(language)
                empates += 1
                status(language, cartas_BOT, cartas_Player1, vitoriasP1)
                break

            while comprar == 'N' and somaFinal_BOT < somaFinal_Player1:
                print()
                # --------------------- / / ----------------------- #
                idiom(language,
                      'The BOT is taking a card... ',
                      'O BOT está comprando mais uma carta... ')
                sorteio_valor_extra_bot = valor[randint(0, 12)]
                sorteio_naipe_extra_bot = randint(0, 3)
                carta_extra_bot = f'{sorteio_valor_extra_bot} {de} {naipe[sorteio_naipe_extra_bot]}'
                sleep(1)
                print()
                idiom(language,
                      f'Extra card: {carta_extra_bot}',
                      f'Carta Extra Sorteada: {carta_extra_bot}')
                print()

                cartas_BOT.append(carta_extra_bot)
                somaFinal_BOT += validacaoLetras(sorteio_valor_extra_bot)

                sleep(1)
                idiom(language,
                      f'Total sum of the cards from BOT: {somaFinal_BOT}.',
                      f'Soma total das cartas do BOT: {somaFinal_BOT}.')
                linha()
                # --------------------- / / ----------------------- #

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

                elif somaFinal_BOT > somaFinal_Player1:
                    break

                elif somaFinal_BOT == somaFinal_Player1:
                    empate(language)
                    empates += 1
                    status(language, cartas_BOT, cartas_Player1, vitoriasP1)
                    break

            if comprar == 'N' and somaFinal_BOT == somaFinal_Player1:
                break

            if comprar == 'S' and somaFinal_BOT < somaFinal_Player1 and jogadaParada_BOT == 0:
                # --------------------- / / ----------------------- #
                idiom(language,
                      'The BOT is taking a card... ',
                      'O BOT está comprando mais uma carta... ')
                sorteio_valor_extra_bot = valor[randint(0, 12)]
                sorteio_naipe_extra_bot = randint(0, 3)
                carta_extra_bot = f'{sorteio_valor_extra_bot} {de} {naipe[sorteio_naipe_extra_bot]}'
                sleep(1)
                print()
                idiom(language,
                      f'Extra card: {carta_extra_bot}',
                      f'Carta Extra Sorteada: {carta_extra_bot}')
                print()

                cartas_BOT.append(carta_extra_bot)
                somaFinal_BOT += validacaoLetras(sorteio_valor_extra_bot)

                sleep(1)
                idiom(language,
                      f'Total sum of the cards from BOT: {somaFinal_BOT}.',
                      f'Soma total das cartas do BOT: {somaFinal_BOT}.')
                linha()
                # --------------------- / / ----------------------- #
                print(somaFinal_BOT)

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

                if comprar == 'N' and somaFinal_BOT == somaFinal_Player1:
                    empate(language)
                    empates += 1
                    status(language, cartas_BOT, cartas_Player1, vitoriasP1)
                    break

                if somaFinal_BOT < somaFinal_Player1:
                    continue

            if comprar == 'N' and somaFinal_BOT > somaFinal_Player1:
                print()
                break

            if comprar == 'S' and somaFinal_BOT > somaFinal_Player1:
                paradaBOT(language, somaFinal_BOT)
                jogadaParada_BOT = 1
                print()
                linha()
                continue

            if comprar == 'S' and somaFinal_BOT > 21:
                BOT_Estourou(language)
                vitoriasP1 += 1
                statusFinal(vitoriasP1, derrotas, empates, partidas)
                continue

            if somaFinal_BOT == somaFinal_Player1 and somaFinal_BOT < 15:

                # --------------------- / / ----------------------- #
                idiom(language,
                      'The BOT is taking a card... ',
                      'O BOT está comprando mais uma carta... ')
                sorteio_valor_extra_bot = valor[randint(0, 12)]
                sorteio_naipe_extra_bot = randint(0, 3)
                carta_extra_bot = f'{sorteio_valor_extra_bot} {de} {naipe[sorteio_naipe_extra_bot]}'
                sleep(1)
                print()
                idiom(language,
                      f'Extra card: {carta_extra_bot}',
                      f'Carta Extra Sorteada: {carta_extra_bot}')
                print()

                cartas_BOT.append(carta_extra_bot)
                somaFinal_BOT += validacaoLetras(sorteio_valor_extra_bot)

                sleep(1)
                idiom(language,
                      f'Total sum of the cards from BOT: {somaFinal_BOT}.',
                      f'Soma total das cartas do BOT: {somaFinal_BOT}.')
                linha()
                # --------------------- / / ----------------------- #

                continue

        # DEFININDO VENCEDOR

        if somaFinal_BOT < somaFinal_Player1 < 21 and jogadaParada_BOT == 1:
            vitoria(language)
            vitoriasP1 += 1
            print()
            linha()

        if somaFinal_Player1 < somaFinal_BOT < 21:
            BOT_venceu(language)
            derrotas += 1
            status(language, cartas_BOT, cartas_Player1, vitoriasP1)

        # CONTINUAR
        sleep(1)
        continuar = ''
        while True:
            try:
                if language == 1:
                    continuar = str(input('Do you wish to play again? [Y/N] ')).upper().strip()[0]
                    if continuar == 'Y':
                        continuar = 'S'
                elif language == 2:
                    continuar = str(input('Deseja jogar de novo? [S/N] ')).upper().strip()[0]
            except:
                msgERROR(language)
                continue
            if comprar == 'N' or comprar == 'S':
                partidas += 1
                break
            else:
                msgERROR(language)
                continue

        if continuar == 'N':
            break
        elif continuar == 'S':
            linha()
            print()
            continue
        else:
            print()
            msgERROR(language)
            continue

# 1 VS 1 MODE
elif playerMode == 2:
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

        sorteio_valor3 = valor[randint(0, 12)]
        sorteio_valor4 = valor[randint(0, 12)]
        while True:
            if sorteio_valor3 == sorteio_valor4:
                sorteio_valor3 = valor[randint(0, 12)]
            elif sorteio_valor3 != sorteio_valor4:
                break

        sorteio_naipe1 = randint(0, 3)
        sorteio_naipe2 = randint(0, 3)
        while True:
            if sorteio_naipe2 == sorteio_naipe1:
                sorteio_naipe2 = randint(0, 3)
            elif sorteio_naipe2 != sorteio_naipe1:
                break

        sorteio_naipe3 = randint(0, 3)
        sorteio_naipe4 = randint(0, 3)
        while True:
            if sorteio_naipe3 == sorteio_naipe4:
                sorteio_naipe3 = randint(0, 3)
            elif sorteio_naipe3 != sorteio_naipe4:
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
              f'Cards from the player {nome_Player2}:',
              f'Cartas do jogador {nome_Player2}:')

        sleep(1)
        carta3 = f'{sorteio_valor3} {de} {naipe[sorteio_naipe3]}'
        print(carta3)
        sleep(1)
        carta4 = f'{sorteio_valor4} {de} {naipe[sorteio_naipe4]}'
        print(carta4)
        sleep(1)
        cartas_Player2 = [carta3, carta4]

        # SOMA DAS CARTAS
        print()
        linha()
        soma1 = validacaoLetras(sorteio_valor1) + validacaoLetras(sorteio_valor2)
        soma2 = validacaoLetras(sorteio_valor3) + validacaoLetras(sorteio_valor4)

        if language == 1:
            print(f'The total sum of the two cards from {nome_Player1}: {soma1}')
            print()
            print(f'The total sum of the two cards from {nome_Player2}: {soma2}')
        elif language == 2:
            print(f'Soma total das duas cartas do {nome_Player1}: {soma1}')
            print()
            print(f'Soma total das duas cartas do {nome_Player2}: {soma2}')
        linha()

        # ACUMULADORES 02
        somaFinal_Player1 = soma1 + 0
        somaFinal_Player2 = soma2 + 0
        Player1_Parou = Player2_Parou = 0

        while True:
            comprar_Player1 = ''
            comprar_Player2 = ''

            # -------------------------- PLAYER 1 -------------------------- #

            while True and Player1_Parou == 0:
                try:
                    if language == 1:
                        comprar_Player1 = str(input(f'Do you wish to take another card {nome_Player1}? [Y/N] ')).upper().strip()[0]
                        if comprar_Player1 == 'Y':
                            comprar_Player1 = 'S'
                    elif language == 2:
                        comprar_Player1 = str(input(f'Deseja comprar mais uma carta {nome_Player1}? [S/N] ')).upper().strip()[0]
                except:
                    msgERROR(language)
                if comprar_Player1.isnumeric():
                    continue
                elif comprar_Player1 == 'N' or comprar_Player1 == 'S':
                    break

            if comprar_Player1 == 'N' and somaFinal_Player1 < somaFinal_Player2:
                break

            if comprar_Player1 == 'S':
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
                    vitoriaPlayer1(language, nome_Player1)
                    vitoriasP1 += 1
                    statusPlayers(language, nome_Player1, cartas_Player1, nome_Player2,
                                  cartas_Player2, vitoriasP1, vitoriasP2)
                    break

                if somaFinal_Player1 > 21:
                    Player1_Estourou(language)
                    vitoriasP2 += 1
                    statusPlayers(language, nome_Player1, cartas_Player1, nome_Player2,
                                  cartas_Player2, vitoriasP1, vitoriasP2)
                    break

                if Player2_Parou == 1 and somaFinal_Player1 > somaFinal_Player2:
                    break

                # if somaFinal_Player1 == somaFinal_Player2:
                #     empate(language)
                #     empates += 1
                #     status(language, cartas_BOT, cartas_Player1, vitoriasP1)
                #     break

            elif comprar_Player1 == 'N':
                paradaPlayer1(language, nome_Player1, somaFinal_Player1)
                Player1_Parou = 1
                continue

            if Player1_Parou == 1 and Player2_Parou == 1:
                break

            # -------------------------- PLAYER 2 -------------------------- #

            while True and Player2_Parou == 0:
                try:
                    if language == 1:
                        comprar_Player2 = \
                        str(input(f'Do you wish to take another card {nome_Player2}? [Y/N] ')).upper().strip()[0]
                        if comprar_Player2 == 'Y':
                            comprar_Player2 = 'S'
                    elif language == 2:
                        comprar_Player2 = \
                        str(input(f'Deseja comprar mais uma carta {nome_Player2}? [S/N] ')).upper().strip()[0]
                except:
                    msgERROR(language)
                if comprar_Player2.isnumeric():
                    continue
                elif comprar_Player2 == 'N' or comprar_Player2 == 'S':
                    break

            if comprar_Player2 == 'N' and somaFinal_Player1 > somaFinal_Player2:
                break

            if comprar_Player2 == 'S':
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

                cartas_Player2.append(carta_Extra)
                somaFinal_Player2 += validacaoLetras(sorteio_valorExtra)

                sleep(1)
                idiom(language,
                      f'Total sum: {somaFinal_Player2}.',
                      f'Soma total: {somaFinal_Player2}.')
                linha()

                if somaFinal_Player2 == 21:
                    vitoriaPlayer2(language, nome_Player2)
                    vitoriasP2 += 1
                    statusPlayers(language, nome_Player1, cartas_Player1, nome_Player2,
                                  cartas_Player2, vitoriasP1, vitoriasP2)
                    break

                if somaFinal_Player2 > 21:
                    Player2_Estourou(language)
                    vitoriasP1 += 1
                    statusPlayers(language, nome_Player1, cartas_Player1, nome_Player2,
                                  cartas_Player2, vitoriasP1, vitoriasP2)
                    break

                if Player1_Parou == 1 and somaFinal_Player2 > somaFinal_Player1:
                    break

            if comprar_Player1 == 'N' and comprar_Player2 == 'N':
                break

            elif comprar_Player2 == 'N':
                paradaPlayer2(language, nome_Player2, somaFinal_Player2)
                Player2_Parou = 1
                continue

            if Player1_Parou == 1 and Player2_Parou == 1:
                break

        # DECIDINDO VENCEDOR

        if somaFinal_Player2 < somaFinal_Player1 < 21:
            vitoriaPlayer1(language, nome_Player1)
            vitoriasP1 += 1
            statusPlayers(language, nome_Player1, cartas_Player1, nome_Player2,
                          cartas_Player2, vitoriasP1, vitoriasP2)

        elif somaFinal_Player1 < somaFinal_Player2 < 21:
            vitoriaPlayer2(language, nome_Player2)
            vitoriasP2 += 1
            statusPlayers(language, nome_Player1, cartas_Player1, nome_Player2,
                          cartas_Player2, vitoriasP1, vitoriasP2)

        elif somaFinal_Player1 == somaFinal_Player2:
            empate(language)
            empates += 1
            statusPlayers(language, nome_Player1, cartas_Player1, nome_Player2,
                          cartas_Player2, vitoriasP1, vitoriasP2)


        # CONTINUAR
        sleep(1)
        continuar = ''
        while True:
            try:
                if language == 1:
                    continuar = str(input('Do you wish to play another match? [Y/N] ')).upper().strip()[0]
                    if continuar == 'Y':
                        continuar = 'S'
                elif language == 2:
                    continuar = str(input('Deseja jogar outra partida? [S/N] ')).upper().strip()[0]
            except:
                msgERROR(language)
                continue
            if continuar == 'N' or continuar == 'S':
                partidas += 1
                break
            else:
                msgERROR(language)
                continue

        if continuar == 'N':
            break
        elif continuar == 'S':
            linha()
            print()
            continue
        else:
            print()
            msgERROR(language)
            continue

# ENCERRAMENTO DO PROGRAMA
linha()
sleep(1)
idiom(language,
      'FINALIZING SYSTEM...',
      'ENCERRANDO O PROGRAMA...')
sleep(1)
print()
if playerMode == 1:
    statusFinal(vitoriasP1, derrotas, empates, partidas)
elif playerMode == 2:
    statusFinalPlayers(language, nome_Player1, vitoriasP1, nome_Player2, vitoriasP2, empates, partidas)

sleep(1)
print()
assinatura(language)
sleep(20)
