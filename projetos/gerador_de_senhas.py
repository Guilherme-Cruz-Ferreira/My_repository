import random, string, time

print('\n\033[32m ---Bem vindo ao gerador de senhas v1.0--- \033[m\n')

def printList(lst):
    for i, v in enumerate(lst):
        if i == len(lst):
            print(v)
        else:
            print(v, end='')
    
dc = ''
arm = list()
t = True
while t:
    
    nesse = True
    a = 0
    mesclagem_alfabetos = list()
    mesclagem_tudo = list()
    mesclagem_digito_maiuscula = list()
    mesclagem_digito_minuscula = list()
    arm = list()            
    
    alfabeto_caixa_baixa = list(string.ascii_lowercase)
    alfabeto_caixa_alta = list(string.ascii_uppercase)
    digitos = list(string.digits)

    for letra in alfabeto_caixa_alta:
        mesclagem_alfabetos.append(letra)
        mesclagem_tudo.append(letra)
        mesclagem_digito_maiuscula.append(letra)

    for letra in alfabeto_caixa_baixa:
        mesclagem_alfabetos.append(letra)
        mesclagem_tudo.append(letra)
        mesclagem_digito_minuscula.append(letra)

    for d in digitos:
        mesclagem_tudo.append(d)
        mesclagem_digito_maiuscula.append(d)
        mesclagem_digito_minuscula.append(d)

    random.shuffle(mesclagem_alfabetos)
    random.shuffle(alfabeto_caixa_baixa)
    random.shuffle(alfabeto_caixa_alta)
    random.shuffle(digitos)

    m = str(input('\nDigite [N] para uma senha contendo [números]\nDigite [L] para uma senha contendo [letras]\nDigite [A] para uma senha contendo [ambos]: '))[0].upper().strip()
    if m == 'N':
        x = int(input('\nDigite o número de caracteres que você deseja na senha: '))        
        for n in range(0, x):
            arm.append(random.choice(digitos))
        nesse = False
    elif m == 'L':
        x = int(input('\nDigite o número de caracteres que você deseja na senha: '))        
        while nesse:    
            vc = str(input('\nDigite [M] para [maiúsculas]\nDigite [N] para [minúsculas]\nDigite [A] para [ambos]: '))[0].upper().strip()
            if vc == 'A':
                for n in range(0, x):
                    arm.append(random.choice(mesclagem_alfabetos))
            elif vc == 'N':
                for n in range(0, x):
                    arm.append(random.choice(alfabeto_caixa_baixa))
            elif vc == 'M':
                for n in range(0, x):
                    arm.append(random.choice(alfabeto_caixa_alta))
            else:
                print('\nFavor digite um valor válido!')
                continue
            nesse = False
    elif m == 'A':
        x = int(input('\nDigite o número de caracteres que você deseja na senha: '))
        while nesse:
            vc = str(input('\nDigite [M] para incluir apenas [maiúsculas]\nDigite [N] para incluir apenas [minúsculas]\nDigite [A] para [ambos]: '))[0].upper().strip()
            if vc == 'M':
                for n in range(0, x):
                    arm.append(random.choice(mesclagem_digito_maiuscula))
            elif vc == 'N':
                for n in range(0, x):
                    arm.append(random.choice(mesclagem_digito_uula))
            elif vc == 'A':
                for n in range(0, x):
                    arm.append(random.choice(mesclagem_tudo))
            else:
                print('\nFavor digite um valor válido!')
                continue
            nesse = False
    else:
        print('\nFavor digitar um caratere válido!')
        continue

    print(f'\033[32mSua senha é: \033[m', end='')
    for pt in arm:
        print(pt, end='')
    dc = str(input(f'\n\nDeseja gerar outra senha?[S/N]: '))[0].strip().upper()
    if dc in 'N':
        print('\nObrigado por usar nosso programa! :)')
        print(f'\nO programa vai fechar em {5} segundos!')
        g = time.sleep(5)
        t = False
    else:
        continue