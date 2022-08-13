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
import time
import os
from arquivo1 import jogo

def destaque(TXT): ### Função para destacar texto 
    print(30*'-')
    print(TXT)
    print(30*'-')
    print('')

def salvar_score(nome, pontuacao, matriz): ### Função para salvar o score
    # Cria lista com todos os scores
    lista = [] 
    for i in range(len(matriz)):
        if matriz[i][2].isnumeric():
            lista.append(int(matriz[i][2]))
        else:
            lista.append(0)
        
    # Adiciona o score, organiza em ordem decrescente e remove o score mais baixo
    while pontuacao in lista: 
        pontuacao += 5 # Adiciona + 5 para desempatar se caso alguem ja tenha feito a mesma pontuação
    lista.append(pontuacao)
    lista.sort()
    lista.reverse()
    lista.pop()

    # Cria uma lista com os nomes segundo a ordem dos scores
    lista_nomes = []
    for i in range(len(lista)):
        for j in range(5):
            if matriz[j][2] == '':
                continue
            elif int(matriz[j][2]) == lista[i]:
                lista_nomes.append(matriz[j][0])
                break
        if lista[i] == pontuacao:
            lista_nomes.append(nome)
            
    # Re-cria a matriz onde os records estão colocados
    for i in range(len(matriz)):
        if lista[i] == 0:
            matriz[i][0] == ' '*10
        else:
            matriz[i][0] = lista_nomes[i] 
            matriz[i][2] = str(lista[i])

    return matriz
        
def records(matriz): ### Função que mostra os records
    os.system("cls")
    print(' '*13,'RECORDS\n')
    for i in range(len(matriz)):
        time.sleep(0.2)
        print(''.join(matriz[i]))
    print('\n')
        
    time.sleep(0.5)
    print(' '*3,'Pressione enter para voltar ao menu...\n')
    keyboard.wait('enter')

def sobre(): ### Função que exibe na tela informações sobre o jogo
    os.system("cls")
    print(' '*15,'SOBRE')
    print('''Esse é um jogo é uma re-imaginação do
clássico dos fliperamas, Asteroids, lançado
a Atari em 1982 e faz parte do processo de
seleção da Rookie Software Inc.''')
    print('\n',' '*13,'CONTROLES')
    print(' <- - Para mover a esquerda\n',
          '-> - Para mover a direita\n',
          'espaço - Para disparar\n',
          'esc - Cancela a partida\n')

    time.sleep(0.5)
    print(' '*3,'Pressione enter para voltar ao menu...\n')
    keyboard.wait('enter')
