##/*******************************************************************************
##Autor: João Gabriel Lima Almeida
##Componente Curricular: Algoritmos I
##Concluido em: 20/04/2021
##Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
##trecho de código de outro colega ou de outro autor, tais como provindos de livros e
##apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
##de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
##do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
##******************************************************************************************/
import keyboard
import os
import time
import random

def dificuldade(pontuacao, quadro, linha):
    # Ajusta a velocidade dos meteoros
    if pontuacao < 501 and quadro == 4: # Dificuldade muito fácil = Velocidade 1
        linha += 1
    elif 500 < pontuacao and pontuacao < 2001: # Dificuldade fácil = Velocidade  2
        if quadro == 4 or quadro == 8:
            linha += 1
    elif 2000 < pontuacao and pontuacao < 3501: # Dificuldade média = Velocidade 3
        if quadro == 1 or quadro == 3 or quadro == 5 or quadro == 7:
            linha += 1
    elif 3500 < pontuacao and pontuacao < 6001: # Dificuldade alta = Velocidade 4
        if quadro == 1 or quadro == 2 or quadro == 4 or quadro == 5 or quadro == 7 or quadro == 8:
            linha += 1
    elif 6000 < pontuacao: # Dificuldade máxima = Velocidade 5
        linha += 1
    return linha

def disparo(matriz_disparo, check, linha, coluna, linha_nave, delay):
    if check == True:
        if linha < 0:
            check = False
            linha = linha_nave - 1
        else:
            if linha == linha_nave - 1: ### Frame 1 da animação de disparo
                matriz_disparo[linha][coluna] = 'X'
                matriz_disparo[linha][coluna + 1] = '-'
                matriz_disparo[linha][coluna - 1] = '-'
            elif linha == linha_nave - 2: ### Frame 2 da animação de disparo
                matriz_disparo[linha][coluna] = 'o'
                matriz_disparo[linha + 1][coluna + 2] = '-'
                matriz_disparo[linha + 1][coluna - 2] = '-'
            elif linha == linha_nave - 3: ### Frame 3 da animação de disparo
                matriz_disparo[linha][coluna] = 'o'
                if coluna < 31: ### Verificação para evitar que a animação saia da matriz
                    matriz_disparo[linha + 2][coluna + 3] = '-'
                elif coluna > 3: ### Verificação para evitar que a animação saia da matriz
                    matriz_disparo[linha + 2][coluna - 3] = '-'
            else: ### Demais frames da animação de disparo
                matriz_disparo[linha][coluna] = 'o'
            linha -= 1
    return matriz_disparo, check, linha, delay

def tela_gameover(matriz_gameover): ### Tela de Gameover
    frame = 1 
    while frame != 0: ### Looping de eventos
        time.sleep(0.15) ### Contagem de frames e delay
        frame += 1

        if frame == 2: # Frame 1 da animação de Gameover
            matriz_gameover = [
    ['-'*35],
    [''],
    [''],
    [' '*5,'╚═╝   ┴ ┴   └─┘    └─┘   '],
    ['-'*35]
    ]
        if frame == 3: # Frame 2 da animação de Gameover
            matriz_gameover = [
    ['-'*35],
    [''],
    [' '*5,'║ ╦   │││   │ │    ├┤    '],
    [' '*5,'╚═╝   ┴ ┴   └─┘    └─┘   '],
    ['-'*35]
    ]
        if frame == 4: # Frame 3 da animação de Gameover
            matriz_gameover = [
    ['-'*35],
    [' '*5,'╔═╗   ┌┬┐   ┌─┐    ┌─┐   '],
    [' '*5,'║ ╦   │││   │ │    ├┤    '],
    [' '*5,'╚═╝   ┴ ┴   └─┘    └─┘   '],
    ['-'*35]
    ]
        if frame == 5: # Frame 4 da animação de Gameover
            matriz_gameover = [
    ['-'*35],
    [' '*5,'╔═╗┌─┐┌┬┐┌─┐┌─┐┬  ┬┌─┐┬─┐'],
    [' '*5,'║ ╦   │││   │ │    ├┤    '],
    [' '*5,'╚═╝   ┴ ┴   └─┘    └─┘   '],
    ['-'*35]
    ]
        if frame == 6: # Frame 5 da animação de Gameover
            matriz_gameover = [
    ['-'*35],
    [' '*5,'╔═╗┌─┐┌┬┐┌─┐┌─┐┬  ┬┌─┐┬─┐'],
    [' '*5,'║ ╦├─┤│││├┤ │ │└┐┌┘├┤ ├┬┘'],
    [' '*5,'╚═╝   ┴ ┴   └─┘    └─┘   '],
    ['-'*35]
    ]
        if frame == 7: # Frame 6 da animação de Gameover
            frame = 0
            matriz_gameover = [
    ['-'*35],
    [' '*5,'╔═╗┌─┐┌┬┐┌─┐┌─┐┬  ┬┌─┐┬─┐'],
    [' '*5,'║ ╦├─┤│││├┤ │ │└┐┌┘├┤ ├┬┘'],
    [' '*5,'╚═╝┴ ┴┴ ┴└─┘└─┘ └┘ └─┘┴└─'],
    ['-'*35]
    ]
        ### Limpa e printa a matriz
        os.system("cls")
        for i in range(len(matriz_gameover)):
            print(''.join(matriz_gameover[i]))
    return matriz_gameover
            
def input_debug(matriz_gameover): ### Debuga o input do python apagando as telcas salvas no buffer
    nome = ''
    while nome != 'pass':
        nome = input()
        if keyboard.is_pressed('enter'):
            nome = 'pass'

        os.system("cls")
        for i in range(len(matriz_gameover)):
            print(''.join(matriz_gameover[i]))
        print('\nPressione Enter para continuar... ')
        time.sleep(0.1)

def jogo():
    ## Variável de pontiação
    score = 0

    ## Pause
    check_p = True

    ## Variáveis de movimentação
    col_nave = 17
    pos_nave = 22

    ## Variáveis de disparo
    check_disparo = False
    col_disparo = 0
    pos_disparo = pos_nave - 1
    delay_disparo = 0

    ## Variáveis dos meteoros
    check_meteoro1 = False
    pos_meteoro1 = 0
    contador_meteoro = random.randint(1, 2)
    vida = 0

    ### Looping de eventos do jogo
    frame = 1
    while not keyboard.is_pressed('esc') and frame != 0:
        time.sleep(0.03) ### Contagem de frames e delay
        frame += 1
        if frame > 8:
            frame = 1
            score += 10 # Score aumenta em função do tempo
        
        matriz = [
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##1 0
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##2 1
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##3 2
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##4 3
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##5 4
            [' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'], #1  5
            ['.',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], #2  6
            [' ','.',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ','+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], #3  7
            ['+',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], #4  8
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ','.',' ',' '], #5  9
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ',' ',' ',' ',' ',' ','+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], #6  10
            [' ','+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], #7  11
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.','+',' '], #8  12
            [' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], #9  13
            [' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.',' ',' ',' ',' ',' '], #10 14
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ',' ','*',' ',' ',' ',' ',' ',' '], #11 15
            ['+',' ',' ',' ',' ',' ',' ',' ',' ','+',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ','+',' ',' ','.',' ',' ',' ',' ',' ',' ',' '], #12 16
            [' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], #13 17
            ['.',' ',' ','+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.',' ',' ','+',' ',' '], #14 18
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' '], #15 19
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.','+',' ',' ',' ',' ',' '], #16 20
            [' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], #17 21
            [' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.'], #18 22
            [' ',' ',' ',' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ',' ',' ',' ','.',' ',' ',' ',' ',' ',' ',' ','+',' ',' ',' '], #19 23
            [' ','*',' ','+',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.',' ',' ',' ','.',' ',' ',' ','*'], #20 24
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##1 25
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##2 26
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##3 27
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '], ##4 28
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']  ##5 29
            ]

    ## Animação e Movimentção da nave
        if frame == 1 or frame == 5: ### Frame 1 da animação da nave
            matriz[pos_nave][col_nave] = 'Δ'
            matriz[pos_nave + 1][col_nave] = '0'
            matriz[pos_nave + 1][col_nave + 1] = '\\'
            matriz[pos_nave + 2][col_nave + 2] = '\\'
            matriz[pos_nave + 1][col_nave - 1] = '/'
            matriz[pos_nave + 2][col_nave - 2] = '/'
            matriz[pos_nave + 2][col_nave - 1] = '░'
            matriz[pos_nave + 2][col_nave + 1] = '▓'
            matriz[pos_nave + 2][col_nave] = 'º'
        elif frame == 2 or frame == 4 or frame == 6 or frame == 8: ### Frame 2 da animação da nave
            matriz[pos_nave][col_nave] = 'Δ'
            matriz[pos_nave + 1][col_nave] = '0'
            matriz[pos_nave + 1][col_nave + 1] = '\\'
            matriz[pos_nave + 2][col_nave + 2] = '\\'
            matriz[pos_nave + 1][col_nave - 1] = '/'
            matriz[pos_nave + 2][col_nave - 2] = '/'
            matriz[pos_nave + 2][col_nave - 1] = '▒'
            matriz[pos_nave + 2][col_nave + 1] = '▒'
            matriz[pos_nave + 2][col_nave] = 'º'
        else: ### Frame 3 da animação da nave
            matriz[pos_nave][col_nave] = 'Δ'
            matriz[pos_nave + 1][col_nave] = '0'
            matriz[pos_nave + 1][col_nave + 1] = '\\'
            matriz[pos_nave + 2][col_nave + 2] = '\\'
            matriz[pos_nave + 1][col_nave - 1] = '/'
            matriz[pos_nave + 2][col_nave - 2] = '/'
            matriz[pos_nave + 2][col_nave - 1] = '▓'
            matriz[pos_nave + 2][col_nave + 1] = '░'
            matriz[pos_nave + 2][col_nave] = 'º'
        
        if keyboard.is_pressed('right') and col_nave < 31 and col_nave >= 2: # Movimentar a nave para a direita
            col_nave += 1
        elif keyboard.is_pressed('left') and col_nave <= 31 and col_nave > 2: # Movimentar a nave para a esquerda
            col_nave -= 1

    ## Disparo e projétil
        # Faz o disparo aparecer na tela quando aperta espaço
        if keyboard.is_pressed('space') and check_disparo == False and delay_disparo == 0:
            check_disparo = True
            delay_disparo = 1
            col_disparo = col_nave
            
        # Controla a animação e a posição do disparo
        (matriz, check_disparo, pos_disparo, delay_disparo) = disparo(matriz, check_disparo, pos_disparo, col_disparo, pos_nave, delay_disparo)

        # Controla o delay do disparo
        if delay_disparo != 0:
            delay_disparo += 1
            if delay_disparo > 10:
                delay_disparo = 0

    ## Meteoro
        # Faz o meteoro aparecer na tela
        if frame == 8 and check_meteoro1 == False: 
            check_meteoro1 = True
            col_meteoro = random.randint(3, 29)

        # Movimenta o meteoro
        if check_meteoro1 == True:
            if pos_meteoro1 > 24: # Apaga o meteoro da tela se caso ele chegue na linha máxima
                check_meteoro1 = False
                pos_meteoro1 = 0
                vida += 1
            else:
                for X in range(3):
                    for Y in range(5):
                            if Y == 0 or Y == 4:
                                matriz[pos_meteoro1 + Y][col_meteoro + X] = '▒'
                            else:
                                matriz[pos_meteoro1 + Y][col_meteoro + X] = '▓'
                for Y in range(3):
                    matriz[pos_meteoro1 + 1 + Y][col_meteoro - 1] = '▒'
                    matriz[pos_meteoro1 + 1 + Y][col_meteoro + 3] = '▒'
                matriz[pos_meteoro1 + 2][col_meteoro - 2] = '░'
                matriz[pos_meteoro1 + 2][col_meteoro + 4] = '░'

                # Controla a dificuldade do jogo
                pos_meteoro1 = dificuldade(score, frame, pos_meteoro1)

                # Movimentação lateral para dificultar mais
                if score > 4500 and frame % 2 == 0:
                    if contador_meteoro == 1 and col_meteoro < 30:
                        col_meteoro += 1
                        if col_meteoro == 29:
                            contador_meteoro = 2
                    elif contador_meteoro == 2 and col_meteoro > 2:
                        col_meteoro -= 1
                        if col_meteoro == 3:
                            contador_meteoro = 1


    ## Colisão
        # Colisão meteoro e tiro
        if check_disparo == True:
            if matriz[pos_disparo][col_disparo] == '▓' or matriz[pos_disparo][col_disparo] == '▒' or matriz[pos_disparo][col_disparo] == '░': 
                check_meteoro1 = False
                pos_meteoro1 = 0
                check_disparo = False
                pos_disparo = pos_nave - 1
                score += 100
            
        # Colisão meteoro e nave
        nave = (matriz[pos_nave][col_nave], matriz[pos_nave + 1][col_nave], matriz[pos_nave + 1][col_nave + 1], matriz[pos_nave + 1][col_nave - 1])
        if '▓' in nave:
            frame = 0
        if '▒' in nave:
            frame = 0
        if '░' in nave:
            frame = 0
            
        # Quebra o looping se passam 10 meteoros
        if vida == 10:
            frame = 0
    ## Pausar
        if keyboard.is_pressed('p') == False:
            check_p = True
        if keyboard.is_pressed('p') and check_p:
            os.system("cls")
            print('\n\n', ' '*13, 'Jogo Pausado')
            time.sleep(0.5)
            keyboard.wait('p')
            check_p = False
            
            
    ## Printar a tela
        os.system("cls")
        print('Score:', score)
        print('-'*35) 
        for i in range(len(matriz)):
            if 4 < i and i < 25:
                print(''.join(matriz[i]))
        print('-'*35,'\nMeteoros que atingiram: ', vida)

    matriz = tela_gameover(matriz)
    input_debug(matriz)

    ### Recebe o nome do jogador que fez alguem score
    time.sleep(1)
    nome = input('\nDigite seu nome: ')
    nome = nome.upper()
    while nome == '':
        nome = input('Nome inválido! Insira novamente: ')
        nome = nome.upper()
    time.sleep(1)
    return nome, score
