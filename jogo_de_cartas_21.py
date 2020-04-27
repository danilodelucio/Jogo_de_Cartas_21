from random import randint
from time import sleep

def linha():
    linha = ''
    print('-' * 70)
    return linha

def cabecalho(txt):
    print(linha())
    print(txt.center(70))
    print(linha())

def msgERROR():
    print('-' * tamanhoLinha)
    print('ERRO! Por favor digite um valor válido!')
    print('-' * tamanhoLinha)

def validacaoLetras(v1):
    if v1 == 'J':
        v1 = 10
    if v1 == 'Q':
        v1 = 10
    if v1 == 'K':
        v1 = 10
    if v1 == 'A':
        v1 = 1
    return v1


cabecalho(' BEM VINDO AO JOGO DE CARTAS 21 \n')

nome_Player1 = ''
while True:
    try:
        nome_Player1 = str(input('Digite seu nome: ')).title().strip()
    except:
        msgERROR()
    if nome_Player1.isnumeric():
        continue
    if nome_Player1 != '':
        break

print()

# ACUMULADORES 01
vitoriasP1 = derrotas = empates = partidas = 0

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


    # SOMA DAS CARTAS
    print()
    linha()
    soma1 = validacaoLetras(sorteio_valor1) + validacaoLetras(sorteio_valor2)
    soma_BOT = validacaoLetras(sorteio_valor1_BOT) + validacaoLetras(sorteio_valor2_BOT)
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
                comprar = str(input(f'Deseja comprar mais uma carta {nome_Player1}? [S/N] ')).upper().strip()[0]
            except:
                msgERROR()
            if comprar.isnumeric():
                continue
            elif comprar == 'N' or comprar == 'S':
                break

        if comprar == 'S':
            sorteio_valorExtra = valor[randint(0, 12)]
            sorteio_naipeExtra = randint(0, 3)
            carta_Extra = f'{sorteio_valorExtra} de {naipe[sorteio_naipeExtra]}'
            sleep(1)
            print()
            print(f'Carta Extra Sorteada: {carta_Extra}.')
            print()

            cartas_Player1.append(carta_Extra)
            somaFinal_Player1 += validacaoLetras(sorteio_valorExtra)

            sleep(1)
            print(f'Soma total: {somaFinal_Player1}.')
            linha()

            if somaFinal_Player1 == 21:
                print('Parabéns, você ganhou!'.upper())
                vitoriasP1 += 1
                print()
                print(f'Total de Vitórias: {vitoriasP1}.')
                linha()
                break

            if somaFinal_Player1 > 21:
                print('Puxa que pena, estourou! Você perdeu!')
                derrotas += 1
                print()
                sleep(1)
                print(f'Vitória do BOT, com a soma total de {somaFinal_BOT}.')
                sleep(1)
                print()
                print(f'As cartas do BOT: {cartas_BOT}.')
                print(f'Suas cartas: {cartas_Player1}.')
                linha()
                break

            if somaFinal_Player1 == somaFinal_BOT and jogadaParada_BOT == 1:
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

        elif comprar == 'N':
            print()
            print(f'{nome_Player1} decidiu parar com a soma total de {somaFinal_Player1}.')
            sleep(1)
            print()
            print(f'Suas cartas foram: {cartas_Player1}.')
            print()
            linha()

        if jogadaParada_BOT == 1:
            print(f'O BOT tinha parado no valor {somaFinal_BOT}.')
            linha()

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

        if comprar == 'S' and somaFinal_BOT == somaFinal_Player1 and somaFinal_BOT >= 18:
            sleep(1)
            print()
            print(f'O BOT decidiu parar com a soma total de {somaFinal_BOT}')
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
            msgERROR()
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