#campo minado
global tabuleiro
tabuleiro = [
['•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•'],
['•', '•', '•', '•', '•', '•', '•', '•']
]

def printTabuleiro():
    for i, v in enumerate(tabuleiro):
        cont = 0
        for k in tabuleiro[i]:
            cont += 1
            print(k, end=' ')
            if cont == 8:
                print(k)

printTabuleiro()