# conversor de código morse
# muita linha pra pouca coisa
import string
s2m = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',\
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J':'.---',\
    'L':'.-..', 'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',\
    'R':'.-.','S':'...', 'T':'-','U':'..-','V':'...-','W':'.--',\
    'X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---',\
    '3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',\
    '8':'---..','9':'----.','0':'-----'}
upca = list(string.ascii_uppercase)
t = True
while t:
    aux = []
    f = []
    o = i = b = True
    while i:        
        op = str(input('1 - string para morse\n2 - morse para string\n>>> '))[0].strip()
        if op == '1' or op == '2':
            i = False
        else:
            print('\033[31mFavor selecionar uma opção válida\033[m')

    while o: 
        if op == '1':
            inp = str(input('\ninsira o texto a ser codificado: ')).strip().upper()

            for n in inp:
                aux.append(n)
            for m in aux:
                for k, v in s2m.items():
                    if k == m:
                        f.append(v)
            if f == []:
                print(f'\033[31mNão é possível CODIFICAR [{inp}]\033[m')
            else:
                print(f'\033[32m{inp} codificado é: \033[m', end=' ')  
                for p in f:
                    print(p, end=' ')
                o = False
        elif op == '2':
            inp = str(input('\ninsira o texto a ser decodificado: '))
            aux = inp.split(' ')
            # print(aux)
            for m in aux:
                for k, v in s2m.items():
                    if v == m:
                        f.append(k)
            if f == []:
                print(f'\033[31m Não é possível DECODIFICAR [{inp}]\033[m')
            else:
                print(f'\033[32m{inp} decodificado é: \033[m', end=' ')        
                for p in f:
                    print(p, end=' ')
                o = False
        else:
            print('\033[31mFavor digitar um valor válido\033[m')

    dsc = str(input('\n\nDeseja sair do programa?[S/N]: '))[0].strip().lower()
    if dsc == 's':
        t = False
    else:
        continue