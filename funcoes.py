from random import randint
from time import sleep


def idiom(language, msg1, msg2):
    if language == 1:
        print(msg1)
    elif language == 2:
        print(msg2)


def regras(language):
    linha()
    idiom(language,
          """
[GAME RULES]

This game was developed with the casual rules of the card game 21.
 
The goal is to score 21 points by adding the card values,
whoever exceeds this limit, loses the game instantly,
and the first one that makes 21, wins.

If player1 decides to stop buying, and player2 exceeds the amount of 
score for the player1 (without exceeding the total sum of 21 points), player1 loses.

If both players have the same value and decide
stop buying, the game draws.

Values of non-numeric cards:
A = 1
J, Q, K = 10

I hope you enjoy, good luck!
          """,
            """
[REGRAS DO JOGO]

Este jogo foi desenvolvido com as regras casuais do jogo de cartas 21.
 
O objetivo é fazer 21 pontos somando os valores das cartas,
quem ultrapassar esse limite, perde o jogo na hora, 
e quem fazer 21 primeiro, ganha.

Se o jogador1 decidir parar de comprar, e o jogador2 ultrapassar o valor que ele 
estava (sem ultrapassar a soma de 21 pontos), o jogador1 perde.

Se ambos jogadores possuírem o mesmo valor e decidirem 
parar de comprar, o jogo empata.

Valores das cartas não númericas:
A = 1
J, Q, K = 10

Espero que goste, boa sorte!
            """)
    linha()


def status(language, cartas_bot, cartas_player, vitorias):
    idiom(language,
          f"BOT's cards: {cartas_bot}.",
          f'As cartas do BOT: {cartas_bot}.')
    idiom(language,
          f'Your cards: {cartas_player}.',
          f'Suas cartas: {cartas_player}.')
    print()
    idiom(language,
          f'Total Victories: {vitorias}.',
          f'Total de Vitórias: {vitorias}.')
    linha()


def statusPlayers(language, nome_player1, cartas_player1, nome_player2, cartas_player2, vitorias_player1, vitorias_player2):
    idiom(language,
          f"{nome_player1}'s cards: {cartas_player1}.",
          f'Cartas de {nome_player1}: {cartas_player1}.')
    idiom(language,
          f"{nome_player2}'s cards: {cartas_player2}.",
          f'Cartas de {nome_player2}: {cartas_player2}.')
    print()
    idiom(language,
          f'Total Victories: {nome_player1} - {vitorias_player1} X {vitorias_player2} - {nome_player2}.',
          f'Total de Vitórias:\n{nome_player1} - {vitorias_player1} X {vitorias_player2} - {nome_player2}.')
    linha()


def statusFinal(vitorias_p1, derrotas, empates, partidas):
    print(f'Total de Vitórias: {vitorias_p1}.')
    print(f'Total de Derrotas: {derrotas}.')
    print(f'Total de Empates: {empates}.')
    print(f'Total de Partidas: {partidas}.')


def statusFinalPlayers(language, nome_player1, vitorias_p1, nome_player2, vitorias_p2, empates, partidas):
    idiom(language,
          f'Final result:\n{nome_player1} - {vitorias_p1} X {vitorias_p2} - {nome_player2}.',
          f'Placar final:\n{nome_player1} - {vitorias_p1} X {vitorias_p2} - {nome_player2}.')
    print()
    idiom(language,
          f'Total Draws: {empates}.',
          f'Total de Empates: {empates}.')

    idiom(language,
          f'Total Matches: {partidas}.',
          f'Total de Partidas: {partidas}.')
    print()


def linha():
    linha = ''
    print('-' * 70)
    return linha


def cabecalho(txt):
    print(linha())
    print(txt.center(70))
    print(linha())


def msgERROR(language):
    linha()
    idiom(language,
          'ERROR! Please type a valid value!',
          'ERRO! Por favor digite um valor válido!')
    linha()


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


def vitoria(language):
    if language == 1:
        print('Congratulations, you won!'.upper())
    elif language == 2:
        print('Parabéns, você ganhou!'.upper())


def vitoriaPlayer1(language, nome_player1):
    print()
    if language == 1:
        print(f'Congratulations, {nome_player1} won!'.upper())
        print()
    elif language == 2:
        print(f'Parabéns, {nome_player1} ganhou!'.upper())
        print()


def vitoriaPlayer2(language, nome_player2):
    print()
    if language == 1:
        print(f'Congratulations, {nome_player2} won!'.upper())
        print()
    elif language == 2:
        print(f'Parabéns, {nome_player2} ganhou!'.upper())
        print()


def Player1_Estourou(language):
    idiom(language,
          'So sad, your value is more than 21. YOU LOSE!',
          'Puxa que pena, estourou! VOCÊ PERDEU!')
    print()
    sleep(1)


def Player2_Estourou(language):
    idiom(language,
          'So sad, your value is more than 21. YOU LOSE!',
          'Puxa que pena, estourou! VOCÊ PERDEU!')
    print()
    sleep(1)


def BOT_Estourou(language):
    idiom(language,
          'The value from BOT is more than 21. YOU WON!',
          'Vixe... o BOT estourou, VOCÊ VENCEU!')
    print()
    sleep(1)


def BOT_venceu(language):
    idiom(language,
          'So sad! THE BOT WON!',
          'Poxa, que pena! O BOT venceu, VOCÊ PERDEU!')


def empate(language):
    print()
    sleep(1)
    idiom(language,
          f'Draw!',
          f'Eita, deu empate!')
    print()


def paradaPlayer1(language, nome_player1, somafinal_player1):
    sleep(1)
    print()
    idiom(language,
          f'{nome_player1} decided to stop with the total sum {somafinal_player1}.',
          f'{nome_player1} decidiu parar com a soma total de {somafinal_player1}.')
    linha()


def paradaPlayer2(language, nome_player2, somafinal_player2):
    sleep(1)
    print()
    idiom(language,
          f'{nome_player2} decided to stop with the total sum {somafinal_player2}.',
          f'{nome_player2} decidiu parar com a soma total de {somafinal_player2}.')
    linha()


def paradaBOT(language, somafinal_bot):
    sleep(1)
    print()
    idiom(language,
          f'BOT decided to stop with the total sum {somafinal_bot}.',
          f'O BOT decidiu parar com a soma total de {somafinal_bot}')


def assinatura(language):
    idiom(language,
          'Thanks for playing my friend!',
          'Obrigado por jogar meu consagrado!')
    print()
    idiom(language,
          'Developed by:\nDanilo de Lúcio',
          'Desenvolvido por:\nDanilo de Lúcio')
    print('Site: www.danilodelucio.com')
    print('GitHub: www.github.com/danilodelucio')