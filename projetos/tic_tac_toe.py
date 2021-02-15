# jogo da velha/tic tac toe
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


def tabVirtual(tab, qNPC, qPLAYER): 
    import random 
    mp = [qNPC, qPLAYER]
    pd = Pdisponiveis(tab)
    movimento = 0
    for g in mp:
        for i, v in enumerate(tab):
            if v in range(1, 10):
                copiaTabuleiro = tab[:]
                copiaTabuleiro[i] = g
                if condVitoria(copiaTabuleiro, g) == True:
                    if i != 9:
                        movimento = i+1
                    else:
                        movimento = i
                    return movimento
    cantos = []
    for i, v in enumerate(pd):
        if v in [1, 3, 7, 9]:
            cantos.append(v)
    
    if len(cantos) > 1:
        movimento = random.choice(cantos) 
        return movimento
    else:
        movimento = cantos[0]
        return movimento
    for i, v in enumerate(pd):
        if v == 5:
            movimento = v
            return movimento
    meios = []
    for i, v in enumerate(pd):
        if v in [2, 4, 6, 8]:
            meios.append(v)
    if len(meios) > 1:
        movimento = random.choice(meios) 
        return movimento
    else:
        movimento = meios[0]
        return movimento
    return random.choice(pd)
       

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


def isbordfull(bi):
    bd = bi[:]
    o = 0
    for n in bd:
        if n == 'X' or n == 'O':
            o += 1
    if o == len(bd):
        return True 


def condVitoria(bo, jdv):
    board = bo[:]
    if board[0] == board[1] == board[2] == jdv: 
        return True
    elif board[3] == board[4] == board[5] == jdv:
        return True
    elif board[6] == board[7] == board[8] == jdv:
        return True
    elif board[0] == board[3] == board[6] == jdv:
        return True
    elif board[1] == board[4] == board[7] == jdv:
        return True
    elif board[2] == board[5] == board[8] == jdv:
        return True
    elif board[0] == board[4] == board[8] == jdv:
        return True
    elif board[6] == board[4] == board[2] == jdv:
        return True


def Pdisponiveis(tab): # Retorna pontos disponíveis em lista
    aux = tab[:]
    pontos_disponiveis = list()
    for i, v in enumerate(aux):
        if v != '•' and v != 'X' and v != 'O':
            pontos_disponiveis.append(v)
    return pontos_disponiveis


def FazJogadas(Q1, Q2, NPC=False):
    cond = m = y = True
    x = False
    cont = 2
    q1 = Q1
    q2 = Q2
    while y:
        j1 = Pdisponiveis(tab=tabuleiro) 
        if cont % 2 == 0:
            jogador_da_vez = q1
        else:
            jogador_da_vez = q2
        while True:
            if not NPC:
                n = str(input(f'PLAYER [{jogador_da_vez}]>>>')).lower().strip()
                if n.isnumeric():
                    n = int(n)
                    break
                else:
                    print('As posições válidas são: ')
                    printGuia()
            elif NPC:
                if jogador_da_vez == q1:
                    n = str(input(f'[PLAYER]>>>')).lower().strip() 
                    if n.isnumeric():
                        n = int(n)
                        break
                    else:
                        print('As posições válidas são: ')
                        printGuia()
                elif jogador_da_vez == q2:
                    if isinstance(n, int):
                        n = tabVirtual(tabuleiro, q2, q1)
                        break
                else:
                    print('não encontrado')
        if n in tabuleiro:
            u = tabuleiro.index(n) #procura o valor n e retorn em u
            tabuleiro2.pop(u) #retira o valor no índice u
            tabuleiro.pop(u)
            tabuleiro2.insert(u, jogador_da_vez)#insere no indice u
            tabuleiro.insert(u, jogador_da_vez)
            if jogador_da_vez == q2:
                print(f'[NPC]>>>{n}')
            printTabuleiro2()
            x = condVitoria(tabuleiro, jogador_da_vez)
            cont += 1
            if x:
                print('------')
                printTabuleiro2()
                print('------')
                banner(f'O vencedor foi o {jogador_da_vez}!!')
                y = False
            if isbordfull(tabuleiro):
                
                banner('Empate')
                y = False
        else:
            if n in range(1, 10):
                print('localização já está em uso!')
                print('localizações disponíveis:')
                printGuia()
            else:
                print('localização não encontrada!')
                print('localizações disponíveis: ')
                printGuia()
        

def printGuia(pg=False):
    if pg == True:
        print('\n-guia do tabuleiro-')
    print(f'{tabuleiro[0]} {tabuleiro[1]} {tabuleiro[2]}'.center(19))
    print(f'{tabuleiro[3]} {tabuleiro[4]} {tabuleiro[5]}'.center(19))
    print(f'{tabuleiro[6]} {tabuleiro[7]} {tabuleiro[8]}'.center(19))


def printTabuleiro2():
    print(tabuleiro2[0], tabuleiro2[1], tabuleiro2[2])
    print(tabuleiro2[3], tabuleiro2[4], tabuleiro2[5])
    print(tabuleiro2[6], tabuleiro2[7], tabuleiro2[8])


def Jogo():
    banner('Jogo da velha')
    y = True
    cont = 2
    k = 0
    cond = True
    while cond:
        gm = str(input('1 - modo single-player\n2 - modo multi-player\n>>>'))
        if gm == '1':
            q1, q2 = selection() #q2 sempre vai ser o
            printGuia(pg=True)
            FazJogadas(q1, q2, NPC=True)
        elif gm == '2':
            q1, q2 = selection() #q2 sempre vai ser o npc
            printGuia(pg=True)
            FazJogadas(q1, q2)
        else:
            print('Favor selecionar uma opção válida!')
            continue
        cond = False


Jogo()
