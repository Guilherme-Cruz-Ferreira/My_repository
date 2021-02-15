# jogo da velha/tic tac toe
# empate: 1 5 7 4 6 8 2 3 9
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

def tabVirtual(tab, qNPC, qPLAYER): 
    import random 
    mp = [qNPC, qPLAYER]
    pd = Pdisponiveis(tab)
    movimento = 0
    for g in mp:
        for i, v in enumerate(tab):
            if v in range(1, 10):
                copiaTabuleiro = tab[:]
                # print(f'pd: {pd}')
                # print(f'copiaTabuleiro: {copiaTabuleiro}')
                # print(f'i: {i}')
                # print(f'g: {g}')
                copiaTabuleiro[i] = g
                
                if condVitoria(copiaTabuleiro, g) == True:
                    print('retornou na condição de vitória')
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
        print('retornou em cantos')
        return movimento
    else:
        print('retornou em cantos')
        movimento = cantos[0]
        return movimento

    for i, v in enumerate(pd):
        if v == 5:
            movimento = v
            print('retornou 5')
            return movimento
    
    meios = []
    for i, v in enumerate(pd):
        if v in (2, 4, 6, 8):
            meios.append(v)
            movimento = random.choice(meios)
            print('retornou meios')
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
    y = True
    x = False
    cont = 2
    cond = m = True
    q1 = Q1
    q2 = Q2
    while y: # faz as jogadas
        
        j1 = Pdisponiveis(tab=tabuleiro) 
        #print(f'Disponíveis: {j1}')
        
        if cont % 2 == 0:
            jogador_da_vez = q1
        else:
            jogador_da_vez = q2
            
        while True:
            if not NPC:
                n = str(input(f'por favor, digite o local onde o \033[32m{jogador_da_vez}\033[m vai ser colocado\n(digite G para mostra a guia do tabuleiro)\n>>> ')).lower().strip() # se gm == sp - só aparece na vez do jogador (q1)
                if n.isnumeric():
                    n = int(n)
                    break
                elif n == 'G':
                    printGuia()
                else:
                    print('As posições válidas são: ')
                    printGuia()
            elif NPC:
                if jogador_da_vez == q1:
                    n = str(input(f'>>> ')).lower().strip() # se gm == sp - só aparece na vez do jogador (q1)
                    if n.isnumeric():
                        n = int(n)
                        break
                    elif n == 'G':
                        printGuia()
                    else:
                        print('As posições válidas são: ')
                        printGuia()
                elif jogador_da_vez == q2:
                    if isinstance(n, int):
                        n = tabVirtual(tabuleiro, q2, q1)
                        break
                    else:
                        print(n)
                        quebra = input('quebra')
                        print('erro na 136, amigo')
                        y = False
                else:
                    print('não encontrado')
        if n in tabuleiro:
            u = tabuleiro.index(n) #procura o valor n e retorn em u
            tabuleiro2.pop(u) #retira o valor no índice u
            tabuleiro.pop(u)
            tabuleiro2.insert(u, jogador_da_vez)#insere no indice u
            tabuleiro.insert(u, jogador_da_vez)
            if jogador_da_vez == q2:
                print(f'npc jogou no {n}')
            printTabuleiro2()
            x = condVitoria(tabuleiro, jogador_da_vez)
            cont += 1
            if x:
                print('------')
                printTabuleiro2()
                print('------')
                banner(f'O vencedor foi o \033[32m{jogador_da_vez}!!\033[m')
                y = False
            if isbordfull(tabuleiro):
                printTabuleiro2()
                banner('Empate')
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


banner('Jogo da velha')
Jogo()