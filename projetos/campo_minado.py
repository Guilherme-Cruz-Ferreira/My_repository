#campo minado
global tabuleiro
tabuleiro = [
['•', '•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•', '•']
]

def printTabuleiro():
    cont2 = 0
    print(' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'F')
    for i, v in enumerate(tabuleiro):
        cont = 0
        print(cont2, end=' ')
        cont2 += 1
        for k in tabuleiro[i]:
            cont += 1
            print(k, end=' ')
            if cont == len(tabuleiro[0]):
                print(' ')

def fazJogada(discover):
    printTabuleiro()
    coluna = int(input('coordenada número >>> ')) 
    fileira = str(input('coordenada letra >>> ')).upper()
    conversor = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'F':8}
    for i, v in conversor.items():
        if i == fileira:
            fileira = v
    
    for i, v in enumerate(tabuleiro):
        if i == coluna:
            for o, b in enumerate(tabuleiro):
                if o == fileira:
                    tabuleiro[i][o] = 'X'
    # printTabuleiro()
while True:
    fazJogada('X')

