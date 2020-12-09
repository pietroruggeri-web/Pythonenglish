import random
a11 = '[ ]'
a12 = '[ ]'
a13 = '[ ]'
a21 = '[ ]'
a22 = '[ ]'
a23 = '[ ]'
a31 = '[ ]'
a32 = '[ ]'
a33 = '[ ]'
n_mosse = 0
while True:

    print(a11,a12,a13)
    print(a21,a22,a23)
    print(a31,a32,a33)
    devi_muovere = True
    while devi_muovere:
        i =int(input('Inserisci riga '))
        j =int(input('Inserisci colonna '))
        devi_muovere = False
        if i == 1 and j == 1 and a11 == '[ ]':
            a11 = '[X]'
        elif i == 1 and j == 2 and a12 == '[ ]':
            a12 = '[X]'
        elif i == 1 and j == 3 and a13 == '[ ]':
            a13 = '[X]'
        elif i == 2 and j == 1 and a21 == '[ ]':
            a21 = '[X]'
        elif i == 2 and j == 2 and a22 == '[ ]':
            a22 = '[X]'
        elif i == 2 and j == 3 and a23 == '[ ]':
            a23 = '[X]'
        elif i == 3 and j == 1 and a31 == '[ ]':
            a31 = '[X]'
        elif i == 3 and j == 2 and a32 == '[ ]':
            a32 = '[X]'
        elif i == 3 and j == 3 and a33 == '[ ]':
            a33 = '[X]'
        else:
            print('Mossa non valida')
            devi_muovere = True
    n_mosse =+1
    #controllo tris giocatore
    r1 = a11 == '[X]' and a11 == a12 and a11 == a13
    r2 = a21 == '[X]' and a21 == a22 and a21 == a23
    r3 = a31 == '[X]' and a31 == a32 and a31 == a33

    c1 = a11 == '[X]' and a11 == a21 and a11 == a31
    c2 = a12 == '[X]' and a12 == a22 and a12 == a32
    c3 = a13 == '[X]' and a13 == a23 and a13 == a33

    d1 = a11 == '[X]' and a21 == a11 and a33 == a11
    d2 = a13 == '[X]' and a22 == a13 and a31 == a13

    v = r1 or r2 or c1 or c2 or c3 or r3 or d1 or d2
    if v:
        print('HAI VINTO')
        break
    if n_mosse == 9:
        print('HAI PAREGGIATO LA PARTITA')
        break
    n_mosse = +1
# MUOVE IL COMPUTER ##########################
    devi_muovere = True
    while devi_muovere:
        i = random.randint(1,3)
        j = random.randint(1,3)
        devi_muovere = False
        if i == 1 and j == 1 and a11 == '[ ]':
            a11 = '[O]'
        elif i == 1 and j == 2 and a12 == '[ ]':
            a12 = '[O]'
        elif i == 1 and j == 3 and a13 == '[ ]':
            a13 = '[O]'
        elif i == 2 and j == 1 and a21 == '[ ]':
            a21 = '[O]'
        elif i == 2 and j == 2 and a22 == '[ ]':
            a22 = '[O]'
        elif i == 2 and j == 3 and a23 == '[ ]':
            a23 = '[O]'
        elif i == 3 and j == 1 and a31 == '[ ]':
            a31 = '[O]'
        elif i == 3 and j == 2 and a32 == '[ ]':
            a32 = '[O]'
        elif i == 3 and j == 3 and a33 == '[ ]':
            a33 = '[O]'
        else:
            devi_muovere = True
    r1 = a11 == '[O]' and a11 == a12 and a11 == a13
    r2 = a21 == '[O]' and a21 == a22 and a21 == a23
    r3 = a31 == '[O]' and a31 == a32 and a31 == a33

    c1 = a11 == '[O]' and a11 == a21 and a11 == a31
    c2 = a12 == '[O]' and a12 == a22 and a12 == a32
    c3 = a13 == '[O]' and a13 == a23 and a13 == a33

    d1 = a11 == '[O]' and a22 == a11 and a33 == a11
    d2 = a13 == '[O]' and a22 == a13 and a31 == a13

    p = r1 or r2 or c1 or c2 or c3 or r3 or d1 or d2
    if p:
        print('HAI PERSO')
        break
    if n_mosse == 9:
        print('HAI PAREGGIATO LA PARTITA')
        break
