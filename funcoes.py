from random import randint
from time import sleep


def idiom(language, msg1, msg2):
    if language == 1:
        print(msg1)
    elif language == 2:
        print(msg2)


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


def statusFinal(vitorias_p1, derrotas, empates, partidas):
    print(f'Total de Vitórias: {vitorias_p1}.')
    print(f'Total de Derrotas: {derrotas}.')
    print(f'Total de Empates: {empates}.')
    print(f'Total de Partidas: {partidas}.')


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


def Player1_Estourou(language):
    idiom(language,
          'So sad, your value is more than 21. You lose!',
          'Puxa que pena, estourou! Você perdeu!')
    print()
    sleep(1)


def BOT_Estourou(language):
    idiom(language,
          'The value from BOT is more than 21. You won!',
          'Vixe... o BOT estourou, você venceu!')
    print()
    sleep(1)


def BOT_venceu(language):
    idiom(language,
          'So sad! The BOT won!',
          'Poxa, que pena! O BOT venceu!')


def empate(language):
    print()
    sleep(1)
    idiom(language,
          f'Draw!',
          f'Eita, deu empate! Ele não quis comprar!')
    print()


def paradaPlayer(language, nome_player1, somafinal_player1):
    sleep(1)
    print()
    idiom(language,
          f'{nome_player1} decided to stop with the total sum {somafinal_player1}.',
          f'{nome_player1} decidiu parar com a soma total de {somafinal_player1}.')
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