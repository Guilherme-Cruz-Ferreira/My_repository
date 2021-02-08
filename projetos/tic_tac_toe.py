# jogo da velha/tic tac toe

# variáveis
p1 = 0
p2 = 0
tabuleiro = [1, 2, 3,\
             4, 5, 6,\
             7, 8, 9]
tabuleiro2 =['•', '•', '•',\
             '•', '•', '•',\
             '•', '•', '•']
l = ['X', 'O']

def banner(txt, np=60):
    print('-'*np)
    print(txt.center(np))
    print('-'*np)


def printGuia():
    print('\n-guia do tabuleiro-')
    print(f'{tabuleiro[0]} {tabuleiro[1]} {tabuleiro[2]}'.center(19))
    print(f'{tabuleiro[3]} {tabuleiro[4]} {tabuleiro[5]}'.center(19))
    print(f'{tabuleiro[6]} {tabuleiro[7]} {tabuleiro[8]}'.center(19))


def printTabuleiro2():
    print(tabuleiro2[0], tabuleiro2[1], tabuleiro2[2])
    print(tabuleiro2[3], tabuleiro2[4], tabuleiro2[5])
    print(tabuleiro2[6], tabuleiro2[7], tabuleiro2[8])


def Jogo():
    y = True
    tset = True
    cont = 2
    k = 0
    while tset: # recebe as opções dos jogadores
        selection = str(input(f'\nOpções restantes de marcadores {l}. selecionar qual?: '))[0].strip().upper()
        for n in l:
            if selection == n:
                p1 = n
                l.remove(p1)
                for o in l:
                    p2 = o
                    print(f'jogador 1: {p1}\njogador 2: {p2}')
                    tset = False
            else:
                print('marcador não encontrado, favor selecionar um existente!')
    
    printGuia()

    while y:
        if cont % 2 == 0:
            jogador_da_vez = p1
        else:
            jogador_da_vez = p2
        while True:
            n = str(input(f'por favor, digite o local onde o \033[32m{jogador_da_vez}\033[m vai ser colocado: '))
            if n.isnumeric():
                n = int(n)
                break
            else:
                print('Favor, digitar uma posição válida!!')
                print(f'As posições válidas são: {printGuia}')

        if n in tabuleiro:
                u = tabuleiro.index(n)
                tabuleiro2.pop(u)
                tabuleiro.pop(u)
                tabuleiro2.insert(u, jogador_da_vez)
                tabuleiro.insert(u, jogador_da_vez)
                printTabuleiro2()
                
                if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
                    banner(f'\033[32mO vencedor foi o {tabuleiro[0]}!!\033[m')
                    y = False
                elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
                    banner(f'\033[32mO vencedor foi o {tabuleiro[0]}!!\033[m')
                    y = False
                elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
                    banner(f'\033[32mO vencedor foi o {tabuleiro[0]}!!\033[m')
                    y = False
                elif tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
                    banner(f'\033[32mO vencedor foi o {tabuleiro[0]}!!\033[m')
                    y = False
                elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
                    banner(f'\033[32mO vencedor foi o {tabuleiro[3]}!!\033[m')
                    y = False
                elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
                    banner(f'\033[32mO vencedor foi o {tabuleiro[6]}!!\033[m')
                    y = False
                elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
                    banner(f'\033[32mO vencedor foi o {tabuleiro[0]}!!\033[m')
                    y = False
                elif tabuleiro[6] == tabuleiro[4] == tabuleiro[2]:
                    banner(f'\033[32mO vencedor foi o {tabuleiro[6]}!!\033[m')
                    y = False
                for n in tabuleiro:
                    if isinstance(n, str): 
                        k += 1
                    else:
                        continue
                if k == 9:
                    banner('Empate!!')
                    y = False      
                k = 0
                cont += 1
        else:
            if n in range(1, 10):
                print('\n\033[31mlocalização já está em uso!\033[m')
                print('localizações disponíveis:')
                printGuia()
            else:
                print('\033[31mlocalização não encontrada!\033[m')
                print('localizações disponíveis: ')
                printGuia()


banner('Jogo da velha')
Jogo()
