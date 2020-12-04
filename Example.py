

materie = ('Informatica', 'Matematica', 'Italiano', 'Inglese', 'Storia', 'Arte')
voti = []

n = len(materie)  # ottengo la lunghezza della tupla

for i in range(n):
    v = int(input('Voto in ' + materie[i] + ': '))

    while v < 0 or v > 10:
        v = int(input('Voto in ' + materie[i] + ': '))

    voti.append(v)

s = 0
massimo = voti[0]
minimo = voti[0]

for i in range(n):
    print('Il voto in', materie[i], 'è', voti[i])
    s += voti[i]
    if voti[i] > massimo:
        massimo = voti[i]
    elif voti[i] < minimo:
        minimo = voti[i]

print('La media è', s / len(voti))


j = voti.index(minimo)
print('Voto più basso:', minimo, 'in', materie[j])

j = voti.index(massimo)
print('Voto più alto:', massimo, 'in', materie[j])


x = int(input('inserisci un numero: '))
y = input('inserisci un operando: ')
z = int(input('inserisci un numero: '))
if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
elif y == '/':
    print(x / z)

from random import *

semi = ['bastoni', 'coppe', 'denari', 'spade']
valori = ['asso', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'fante', 'cavallo', 're']

n = 40

carte = list(range(n))

shuffle(carte)

while True:
    estrai = input('Per estrarre premi invio, altrimenti premi E! ')
    if estrai == 'E':
        break
    estratta = carte.pop()
    n -= 1
    s = estratta // 10
    v = estratta % 10

    print('Hai due tentativi per indovinare il seme!')

    tentativo = 0

    for i in range(2):
        indovina = input('metti il seme: b, c, d oppure s: ')
        if indovina == 'b':
            indovina = 'bastoni'
        elif indovina == 'c':
            indovina = 'coppe'
        elif indovina == 'd':
            indovina = 'denari'
        elif indovina == 's':
            indovina = 'spade'
        else:
            print('Hai sbagliato a digitare')
        if indovina == semi[s]:
            print('Hai indovinato il seme! ')
            tentativo = 1
            break
        else:
            print('Non hai indovinato!')

    if tentativo == 1:
        print('Hai tre tentativi per indovinare il valore!')
        for i in range(3):
            numero = input('metti il valore: asso, due, tre, quattro , cinque, sei, sette, fante, cavallo, re: ')
            if numero == valori[v]:
                print('Hai indovinato! ')
                break
            else:
                print('Non hai indovinato! ')
                if i == 2:
                    print('La carta estratta era: ', valori[v], 'di', semi[s])

    print()






