

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
plus = '+'
less = '-'
multiplication = '*'
division = '/'

if y == plus:
    print(x + z)
elif y == less:
    print(x - z)
elif y == multiplication:
    print(x * z)
elif y == division:
    print(x / z)















