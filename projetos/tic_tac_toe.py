# jogo da velha/tic tac toe

# variáveis
p1 = p2 = 0 
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


def selection():
    tset = True
    while tset: # Seleciona X ou O / presente nos 2 gms
        selection = str(input(f'\nOpções restantes de marcadores {l}. selecionar qual?: '))[0].strip().upper()
        for n in l:
            if selection == n:
                p1 = n
                l.remove(p1)
                for o in l:
                    p2 = o
                    print(f'jogador 1: {p1}\njogador 2: {p2}')
                    tset = False
                return p1, p2
            else:
                print('marcador não encontrado, favor selecionar um existente!')


def condVitoria(bo):
    k = 0
    board = bo[:]
    if board[0] == board[1] == board[2] == 'X' or board[0] == board[1] == board[2] == 'O':
        banner(f'\033[32mO vencedor foi o {board[0]}!!\033[m')
        return True
    elif board[3] == board[4] == board[5] == 'X' or board[3] == board[4] == board[5] == 'O':
        banner(f'\033[32mO vencedor foi o {board[3]}!!\033[m')
        return True
    elif board[6] == board[7] == board[8] == 'X' or board[6] == board[7] == board[8] == 'O':
        banner(f'\033[32mO vencedor foi o {board[6]}!!\033[m')
        return True
    elif board[0] == board[3] == board[6] == 'X' or board[0] == board[3] == board[6] == 'O':
        banner(f'\033[32mO vencedor foi o {board[0]}!!\033[m')
        return True
    elif board[1] == board[4] == board[7] == 'X' or board[1] == board[4] == board[7] == 'O':
        banner(f'\033[32mO vencedor foi o {board[3]}!!\033[m')
        return True
    elif board[2] == board[5] == board[8] == 'X' or board[2] == board[5] == board[8] == 'O':
        banner(f'\033[32mO vencedor foi o {board[6]}!!\033[m')
        return True
    elif board[0] == board[4] == board[8] == 'X' or board[0] == board[4] == board[8] == 'O':
        banner(f'\033[32mO vencedor foi o {board[0]}!!\033[m')
        return True
    elif board[6] == board[4] == board[2] == 'X' or board[6] == board[4] == board[2] == 'O':
        banner(f'\033[32mO vencedor foi o {board[6]}!!\033[m')
        return True
    for n in board:
        if isinstance(n, str): 
            k += 1
        else:
            continue
    if k == 9:
        banner('Empate!!')
        return True
   

def npc(tab, tab2):
    aux2 = tab2[:]
    aux = tab
    pontos_disponiveis = list()
    for i, v in enumerate(aux):
        if v != '•' and v != 'X' and v != 'O':
            pontos_disponiveis.append(v)
    return pontos_disponiveis
    

def insereTabuleiro(Q1, Q2):
    y = True
    x = False
    cont = 2
    
    cond = m = True
    q1 = Q1
    q2 = Q2
    while y: # teste
        j1 = npc(tab=tabuleiro, tab2=tabuleiro2) 
        print(f'Disponíveis: {j1}')
        if cont % 2 == 0:
            jogador_da_vez = q1
        else:
            jogador_da_vez = q2
        while True:
            n = str(input(f'por favor, digite o local onde o \033[32m{jogador_da_vez}\033[m vai ser colocado\n(digite G para mostra a guia do tabuleiro)\n>>> ')).lower().strip()
            if n.isnumeric():
                n = int(n)
                break
            elif n == 'G':
                printGuia()
            else:
                print('As posições válidas são: ')
                printGuia()
                
        if n in tabuleiro:
            u = tabuleiro.index(n)
            tabuleiro2.pop(u)
            tabuleiro.pop(u)
            tabuleiro2.insert(u, jogador_da_vez)
            tabuleiro.insert(u, jogador_da_vez)
            printTabuleiro2()
            # condições vitória/empate
            x = condVitoria(tabuleiro)
            if x:
                y = False
        else:
            if n in range(1, 10):
                print('\n\033[31mlocalização já está em uso!\033[m')
                print('localizações disponíveis:')
                printGuia()
            else:
                print('\033[31mlocalização não encontrada!\033[m')
                print('localizações disponíveis: ')
                printGuia()
        cont += 1

def printGuia(pg=False):
    if pg == True:
        print('\n-guia do tabuleiro-')
    print(f'{tabuleiro[0]} {tabuleiro[1]} {tabuleiro[2]}'.center(19))
    print(f'{tabuleiro[3]} {tabuleiro[4]} {tabuleiro[5]}'.center(19))
    print(f'{tabuleiro[6]} {tabuleiro[7]} {tabuleiro[8]}'.center(19))


#def printVitoriaColorida()

def printTabuleiro2():
    print(tabuleiro2[0], tabuleiro2[1], tabuleiro2[2])
    print(tabuleiro2[3], tabuleiro2[4], tabuleiro2[5])
    print(tabuleiro2[6], tabuleiro2[7], tabuleiro2[8])


def Jogo():
    y = True
    cont = 2
    k = 0
    cond = True
    while cond:
        gm = str(input('1 - modo single-player\n2 - modo multi-player\n>>>'))

        if gm == '1':
            q1, q2 = selection() #q2 sempre vai ser o npc
            printGuia(pg=True)
            insereTabuleiro(q1, q2)
        elif gm == '2':
            q1, q2 = selection() #q2 sempre vai ser o npc
            printGuia(pg=True)
            insereTabuleiro(q1, q2)
        else:
            print('Favor selecionar uma opção válida!')
            continue
        cond = False

banner('Jogo da velha')
    
Jogo()
