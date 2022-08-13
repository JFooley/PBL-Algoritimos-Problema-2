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
from arquivo2 import destaque, salvar_score, records, sobre

### Matriz onde os records são alocados
matriz_records = [
[' '*10,'|',''],
[' '*10,'|',''],
[' '*10,'|',''],
[' '*10,'|',''],
[' '*10,'|','']
    ]

### Comando para delimtar a tela
os.system("mode con: cols=45 lines=30")


### Looping de eventos do Menu
opcao = 0
att_tela = True
frame = 1
while frame != 0:
    time.sleep(0.1)

    menu = [
        [' '*15,'Jogar ',''],
        [' '*15,'Records ',''],
        [' '*15,'Sobre ',''],
        [' '*15,'Sair ','']
        ]

    if keyboard.is_pressed('down') and opcao < 3:
        opcao += 1
        att_tela = True

    elif keyboard.is_pressed('up') and opcao > 0:
        opcao -= 1
        att_tela = True

    menu[opcao][2] = '<'
    menu[opcao][0] = ' '*13 + '> '

    if keyboard.is_pressed('enter'):
        if opcao == 0:
            nome, score = jogo()
            matriz_records = salvar_score(nome, score, matriz_records)
            records(matriz_records)
            nome = ''
            score = 0
            
        elif opcao == 1:
            records(matriz_records)
            
        elif opcao == 2:
            sobre()
            
        elif opcao == 3:
            destaque('Encerrando...')
            time.sleep(1.5)
            quit()
            
        att_tela = True ### Informa ao programa que houve uma atualização

    if att_tela == True: ### Imprime a tela somente se houve alguma atualização
        os.system("cls")
        print('-'*40)
        print(
''.join(['   ___      _                 _     _     ']),'\n',
''.join([' / _ \    | |               (_)   | |     ']),'\n',
''.join(['/ /_\ \___| |_ ___ _ __ ___  _  __| |___  ']),'\n',
''.join(['|  _  / __| __/ _ \ |__/ _ \| |/ _` / __| ']),'\n',
''.join(['| | | \__ \ ||  __/ | | (_) | | (_| \__ \ ']),'\n',
''.join(['\_| |_/___/\__\___|_|  \___/|_|\__,_|___/ ']),'\n')
        for i in range(len(menu)):
            print(''.join(menu[i]))
        print('-'*40)
        att_tela = False

    
    
