''''
print('ciao Pietro')  # Comando Base per scrivere qualsiasi cosa
print('Oggi studio Python!')
x = 3
x = 4
print(x)
print(5)

y = 'Ciao Roberto'
print(y)

x = 3+4
print(x)

x = 5
y = 10
z = x + y
print(z)

x = input('inserisci un numero ')
k= int(x)
z = k * 3

x = int(input('inserisci primo numero '))
y = int(input('inserisci secondo numero'))
print(x*y)



po = float(input('Inserisci numero '))
op = input('Inserisci un operando ')
to = float(input('Inserisci '))
if op== '+':
    print(po + to)

# incremento
x = 0
x += 1 # x = x + 1
print(x)

# operazioni elementari particolari

x = 4
x = x ** 2  # elevamento a potenza
print(x)

x = x % 3 # resto della divisione intera

x = 1.2
y = 1.0
print(x-y)
import random
import math  # import vanno all'inizio del programma
x = math.sin(3.14)
print(x)

y = math.log(10,2)
print(y)

y1  = random.randint(1,100)  # Genera numeri random da 1 e 100
print(y1)

# Istruzione condizionale (If)
password = input('Inserisci password ')

if password== '123':  # Uguale
    print('Esegui il programma')  # eseguire in maniera condizionale diverse sezioni del mio programma
    x = int(input('inserisci primo numero'))
    y = int(input('inserisci primo numero'))
    print(x,'*',y)
if password!= '123':  # Diverso
    print('Non puoi eseguire il programma')
# PRIMI ESERCIZI

who = input('chi ha ragione?\n')
if who == 'Marco':
    print('risposta corretta')
else:  #  Alternativa per non ripetere l'if se non è marco allora stampa risposta errata
    print('risposta errata')

a = float(input('Inserisci il primo operando \n'))
o = input('Inserisci una operazione \n')
b = float(input('Inserisci il secondo operando \n'))
if o == '+':
    print(a,o,b, '=', a + b)  #  Legare if tra di loro , altrimenti potrebbe essere
elif o == '-':
    print(a,o,b, '=', a - b)  #  Stampa direttamente il risultato
elif o == '*':
    print(a,o,b, '=', a * b)
elif o == '/':
    print(a,o,b, '=', a / b)
if o != ('+','-','*','/'):
    print('Operazione non valida')

x = 4
if x >= 1:
    if x <= 10:
        print(x,'è nell\'intervallo')
    else:
        print(x,'non è nell\'intervallo')
else:
    print(x, 'non è nell\'intervallo')

# OPERAZIONI BOOLEANE (AND, OR E NOT)
# AND mettere insieme due condizioni
# OR mette a contfronto due condudiziono o la prima o la seconda
# NOT serve per negare if x not(...) invece che mettere il diverso !=...
x = 5
if x >= 1 and x <=10:
    print(x, 'è nell\'intervallo')
else:
    (x, 'non è nell\'intervallo')

Ax=int(input('inserisci un numero'))
Ay=int(input('inserisci un numero'))
Bx=int(input('inserisci un numero'))
By=int(input('inserisci un numero'))
Cx=int(input('inserisci un numero'))
Cy=int(input('inserisci un numero'))
Dx=int(input('inserisci un numero'))
Dy=int(input('inserisci un numero'))

if Ax == (Bx,Cx,Dx):
    print(Ax,'Il rettangolo è disgiunto')
if Cx > Bx:
    print('i rettangoli non si toccano')

Colore = input('Inserisci un colore')
Modello = int(input('Inserisci un modello'))
Km_fatti = int(input('Km percorsi con la vettura'))
Produttore_Car = input('Inserisci un costruttore')
if Colore == 'Rosso':
    print('Si la compro')
    if Modello > 2010:
        print('Si la compro')
    else:
        x = input('Ha meno di 500000?')
        print(x)

        if x < '500000':
            print('la compro')
        else:
            print('non la compro')

if Colore  != 'Rosso':
    print('Non la compro')
if Produttore_Car == 'Ferrari':
    print('Si la compro')
else:
    print('Non la compro')

# CICLI
x = 0
while x < 100:  # Finchè
    print(x,'Ciao')
    x +=1
print('Fine')

x = ''
while x !='1234':  # TESTO LA CONDIZIONE E POI IL CRITERIO QUINDI è UNA SORTA DI LOOP
    x = input('inserisci password\n')
print('Bravo!')


n = int(input('Inserisci il numero di numeri da sommare\n'))
x = 0
s = 0
while x < n:  # WHILE FUNZIONA SOLO CON UNA CONDIZIONE SENZA ESSA NO
    y = int(input('Inserisci il numero\n'))
    s += y
    x += 1
print('La somma è',s)

i = 0
n = 2
s = 0
while i < 100:
    s += n
    print(n,'la somma per adesso è',s)
    n += 2
    i += 1
print('la somma dei primo numeri pari è',s)

 # IL CICLO FOR SINTETIZZA QUELLO CHE SI VUOLE FARE CON IL WHILE, UNA OPERAZIONE AL POSTO DI 3

for x in range(0,100):  # PRIMO NUMERO INCLUSO SECONDO ESCLUSO, POSSIAMO METTERCI ANCHE UN UNICO PARAMETRO
    if i%2 ==0:
        continue  # CONTINU FINCHE NON HAI DATO IL RISULTATO QUINDI SKIPPA
    print(x,'ciao')
    break  #  SERVE PER USCIRE DAL PROGRAMMA
    i = 999 # SE CAMBIO LA I ALL'INTERNO DELLA FUNZIONE NON VIENE TOCCATA NELLA FORMULA
            # IL CICLO FOR RENDE TUTTO PIù SEMPLICE

# LISTE (importanti nella programazzione), scaffale contenente tanti cassetini

a = [] # Per creare una lista, scaffale a
a.append(3)
a.append(4)
a.append('ciao')  # Memorizzare elementi nella lista

for i in range(3):
    print(a[i])
n = int(input('inserisci numero di numeri da sommare\n'))
a = []
for i in range(n):
    a.append(int(input('inserisci numero\n')))
print(a)

s = 0
for i in range(n):
    s += a[i]
print('la somma è',s)

for i in range(n):
    print(a[n-i-1])  # Leggere i numeri al contrario

# ESERCIZIO CALCOLO MEDIA E SCARTO QUADRATICO MEDIO

import math
n = int(input('inserisci numero di numeri\n'))
a = []
for i in range(n):
    a.append(int(input('inserisci valori\n')))
    print(a,'La media tra i valori della lista è',sum(a)/len(a))
    x = (math.sqrt(a[i]-(sum(a)/(len(a))/a[i])))
    print(a,'Lo scarto quadraitco medio della lista è',x)

# RIGUARDARE MA CAPITO PROCEDIMENTO
import math
n = int(input('inserisci n° da moltiplicare '))
a = int(input('inserisci n° da moltiplicare '))
for i in range(n,a):
    a1 = (int(input('inserisci valori ')))
    n1 = (int(input('inserisci valori ')))
    print((n1 * a1) + n1 + a1)
    print('il prodotto scalare tra le due liste è','--->')

import math
n = int(input('inserisci n° numeri della lista\n'))

a = []
for i in range(n):
    a.append(int(input('inserisci valori\n')))
    print(a)
a1 = input('Vuoi mettere un altro valore?')
if a1 == 'si':
    print(a.append(int(input('inserisci un altro valore '))))
if not a1:
    print(a)
print(a)


# COMANDI EXTRA CON LE LISTE

x = [3,4,5,6,7,'Pietro'] # La lista può contenere sia interi che numeri
print(len(x)) # Conta gli elementi della lista

for i in range(-1,-len(x)-1,-1):
    print(x[i])             # Leggere numeri al contrario della lista

x.insert(1,10)
print(x)

x.pop(1) # Eliminare elemento dalla lista
print(x)
x.remove(6)  #Elimina il valore dalla lista in base al contenuto
print(x)

i = x.index(6)
print(i)  # Qual'è l'indice dove trovo l'elemento 6
# WARNING DEVO APPLICARE QUESTE OPERAZIONI A ELEMENTI PRESENTI NELLA LISTA SE NO MI DA ERRORE
if 8 in x: # SE NON VOGLIO CHE IL PROGRAMMA MI DIA ERRORE UTILIZZARE 'IN'
    ...
    ...

x = list(range(10))
print(x)

for i in range(10):
    print(i)

x = ['a','b','c','d']
for i in range(len(x)):  # RANGE CREA UNA LISTA CON 0,1,2,3 IL FOR SCORRE LA LISTA CON 0,1,2,3 E POI ACCCEDO AGLI ELEMENTI,FOR SCORRE LA LISTA DEL RANGE
    print(x)

for i in x:     #  CONVIENE NON SCRIVERE PIù CON RANGE MA DIRETTAMENTE IL NOME DELLA LISTA COSì AL POSTO DI PASSARE I NUMERI PASSA DIRETTAMENTE I DATI DELLA LISTA
    print(i)
x = [4,2,1,3]
print(min(x))   # FUNZIONE MIN VALORE LISTA
print(max(x))   # FUNZIONE MAX VALORE LISTA
print(sum(x))   # FUNZIONE SOMMA DELLA LISTA

x.reverse() # PRENDE LA LISTA E LA GIRA AL CONTRARIO
print(x)

x.sort()    # ORDINA LA LISTA DAL PIù PICCOLO AL PIù GRANDE
print(x)

x =[9,1,4,5,8]
x.sort(reverse=True)  # ORDINA LA LISTA DAL PIù GRANDE AL PIù PICCOLO
x.sort(reverse=False) # ORDINA LA LISSTA DAL PIù PICCOLLO AL PIù GRANDE
print(x)
y = sorted(x)   #CREA UNA LISTA ORDINATA, UGUALE ALLA PRECEDENTE MA ORDINATA
print(y)
print(x)

# OPERAZIONI DI SLICING

y = x[:3]   # PRENDI I PRIMI TRE ELEMENTI DI X
y = x[1:3]  # IN QUESTO CASO PRENDI GLI ELEMENTI 1 E 3
y = x[:]    # CREO UNA COPIA DELLA LISTA

print(y)

# MODO IN CUI LE LISTE SONO MEMORIZZATE NELLA MEMORIA DEL COMPUTER

a = 2
b = a
a = 3
print(b)

ax = [1,2]  # QUANDO CI SONO LE QUADRE CREI UNA LISTA, CREARE COPIE IN MEMORIA OPERAZIONE ONEROSA PER IL PC
bx = ax
ax.append(3)    # SE VOGLIO UNA COPIA DEVO SPECIFICARLO (VEDIMO IN SEGUITO)
print(bx)

b = a # SHALLOW COPY, COPIA SUPERFICIALE

# DEEP COPY
a = [1,2]
b = []
for x in a:
    b.append(x)
print(b)
print(a)

b = a[:] # COPIARE UNA LISTA, versione contratta


lista_nome = ['Pietro','Fabrizio','Fabrizio','Matteo','Massimiliano']
print(lista_nome)
x = lista_nome.count((input('Quale nome compare più volte\n')))
print('Compare',x,'volte all\'interno della lista')

# SET

# Un set è una struttura dati come una lista, ma che non ammette duplicati

a = {1,2,3}
a.add(2)
print(a)
# trova elementi senza duplicati

x = [1,1,1,1,2,3,1,2,3,4]
a = set(x)
print(a)

# trova gli elementi che hanno duplicati
dup = set([y for y in x if x.count(y) > 1])
print(dup)

#trova elementi che non hanno duplicati
ndup = a.difference(dup) #intersezione, unione, ...
print(ndup)

freq = [{y:x.count(y)} for y in set(x)]
print(freq)

freq = {y:x.count(y) for y in set(x)}
print(freq)

for i#(PUOI METTERE QUALSIASI VARIABILE, I,X,O,U,V..)# in x(NELLA LISTA):


macchine = ['Ferrari','Mercedes','BMW']

popped_macchine= macchine.pop()  # MI RESTITUISCE L'ULTIMO ELEMENTO DELLA LISTA CHE HO APPENA CANCELLATO
print(macchine)
print(popped_macchine)

macchine.remove('Ferrari')  # CANCELLI IN BASE ALL'ELEMENTO CHE DESIDERI ELIMINARE
print(macchine)
'''
'''
# ESERCIZIO MENù STUDENTI CON MEDIA
s = []
v = []
while True:
        print('1.inserisci studente')
        print('2.inserisci media')
        print('3.stampa tutto')
        print('4.caclola media classe')
        print('5.esci')
        op = int(input('inserisci operazione \n'))
        if op == 1:
            nc = input('inserisci nome e cognome dello studente')
            s.append(nc)
            v.append(-1)
        if op ==2 :
            nc = input('inserisci nome e cognome dello studente')
            media = float(input('inserisici media'))
            if nc in s:
                i = s.index(nc)
                v[i] = media
        if op == 3:
            for i in range(len(s)):
                print(s[i],'-->',v[i])
        if op == 4:
            vr = [m for m in v if m> 0]
            media = sum(vr) / len(vr)
            print('la media dei voti della classe è',(sv/nv))
        if op == 5:
            break
 '''
'''
# ULTIMA LEZIONE DELLE LISTE, SET AND LIST COMPREHENSION
a = [1,2,3,4,5,6,7,8,9]

a = {1,2,3,4,5,6,7,8,9,1}  # I SET NON AMMETANO DUPLICATI

a.add(3)  # NEI SET SI AGGIUNGE CON AD MA SOLO SE L'ELEMENTO NON è PRESENTE
print(a)
a = list(a)  # CONVERTO UN SET IN UNA LISTA
a = set([1,2,3])  # CONVERTO UNA LISTA IN UN SET

# SET = INSIEME

a = {1,2,3}
b = {2}
print(a.intersection(b))  # HO FATTO L'INTERSEZIONE POTREIO FARE ANCHE LA DIFFERENZA O L'UNIONE INSIEMISTICA

# EXTRA 3

a = [1,2,3,4,5,6]
b = [3,6,8,9]
if len(set(a).intersection(set(b)))>0:
    print('le liste hanno alemno un elemento in comune')
else:
    print('Non hanno elementi in comune')

# LIST COMPRENSHION  #  SEMPLIFICO IL CODICE CHE UTILIZZO

a = [1,2,3,4]
b = []
for x in a:
    if x % 2 == 0:
        b.append(x*2)
print(b)        # TUTTA QUESTA COSA SI PUò RIASSUMERE IN UNA SOLA RIGA GRAZIE ALLE LIST

b = [x*2 for x in a if x%2==0]  # CREA UNA LISTA GLI ELEMNTI DI X MOLTIPLICATI PER DUE GLI ELEMENTI DI X SONO PRESI DA A,SE RISPECCHIANO QUESTA CONDIZIONE
print(b) # ESPRESSIONE FOR CONDIZIONE

# COME USARLE

b = [x for x in a if len(x) > 2]
print(b)
'''
# PARLIAMO DELL'ESAME
# CREARE UN PROGRAMMA E CONSEGNARE IL CODICE SORGENTE
# CREATO UNO STRUMENTO ONLINE EXAMCREATE.UPSPOT.COM, IDEA COME PREPARARSI E COME SARà L'ESAME
# PIATTAFORMA PER CREARE GLI ESAMI NOME FILE ESAME --> NOME COGNOME E IL CODICE SCRITTO SULL'ESAME
# CERCARE FILE NEL MIO DISCO COSA MOLTO IMPORTANTE

# DIZIONARI E STRUTTURE DATI COMPLESSE
# DIZIONARIAO = {CHIAVE,VALORE}
'''
d = { }
d['Mattia'] = 44  # NON SI UTILIZZA APPEND COME NELLE LISTE MA SI AGGIUNGE VHIAVE, VALORE
d['Pietro'] = 20
print(d)

d = {
    'Pietro':20,
    'Mattia':44  # UN PO COME IL DISCORSO VARIABILI
}
print(d['Mattia']   # TABELLE, NIENTE CHIAVI DUPLICATE, SE INSERISCI UNA CHIAVE GIà PRESENTE QUESTA VIENE SOVRASCRITTA
# SINTASSI MOLTO ESPRESSIVA
if 'Mattia' in d:
    d['Mattia'] = 33 # SE UNA DETERMINATA CHIAVE è PRESENTE ALL'INTERNO DEL DELZIONARIO

# SCORRERE GLI ELEMENTI NEL DIZIONARIO

for k in d.keys(): # RESTITUISCE UNA LISTA CO TUTTE LE CHIAVI PRESENTI NEL DIZIONARIO
    print(k,d[k])   # PER OGNUNA STAMPA LA CHIAVE E IL VALORE CORRISPETIVO

# ALTRO MEDOTO PIù COMPATTO PER SCORERERE GLI ELEMENTI NEL DIZIONARIO

for k,v in d.items():  # d.items = COPIA DI CHIAVI E VALORI
    print(k,'-->',v

# PER ELIMINARE ALL'INTERNO DEI DIZIOANRI

del d['Mattia']  # CANCELLA L'ELEMENTO (mattia) DALLA LISTA
'''
'''
x = [1,1,2,1,3]   # SCORRE ALL'INTERNO DELLA MIA LISTA
d = {}
for v in x:
    if v in d:
        d[v] += 1
    else:
        d[v] = 1
print(d)
'''
'''
# STRUTTURE DATI COMPLESSE

d = {
    'marco':[18,24,30],
    'roberta':[24,30,30] # OLTRE A METTERE IN MANIERA SEMPLICE CHIAVE VALORE NEL DIZIONARIO AL POSTO EL VALORE SINGOLO POSSO AGGIUNGERCI UNA LISTA
}

print(d['marco'][-1]) # L'ULTIMO VOTO PRESO DA...  # STO ACCEDENDO ALLA CHIAVE ASSOCIATA MARCO

# LE STRUTTUE LE POSSO COMBINARE IN MANIERA LIBERA COME MEGLIO DESIDERO AD ESEMPIO:

v = [                       #  QUESTA è UNA MATRICE
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(v[0][0])  # PER ACCEDERE AGLI ELEMENTI COME NELLE LISTE NORMALI

V = [
    {'nome':'Mattia','voti':[1,23,28,]}  #  POSSO COMBINARE IN MANIERA ALTERNATA SIA LISTE CHE DIZIONARI
]
for s in v:
    print(s['nome'])
v[0]['voti'][-1] #  ORGANIZZARE IN MANIERA IMPORTANTE I DATI è FONDAMENTALE PERCGè CI PERMETTE POI DI SCRIVERE UN CODICE IN MANIERA SEMPLICE, A PROBLEM WEEL REPRESETED IS HALF SOUL

#  ESERCIZO STUDENTI CON LISTE E DIZIONARI

studenti = []
while True:
    print('1.Inserisci studente'),
    print('2.Aggiungi voto a Studente')
    print('3.Stampa')
    print('4.Calcola media voti Studente')
    print('5.Esci')
    op = int(input('inserisci operazione\n'))
    if op ==1:
        n = input('inserisci nome\n')
        c = input('inserisci cognome\n')
        studenti.append({'nome':n,'cognome':c,'voti':[]})
    if op ==2:
        n = input('inserisci nome\n')
        c = input('inserisci cognome\n')
        for s in studenti:
            if s['nome']== n and s ['cognome']==c:
                v = int(input('inserisci voto\n'))
                s['voti'].append(v)
    if op ==3:
        for s in studenti:
            print(s['nome'],s['cognome'],'-->',s['voti'])
    if op ==4:
        n = input('inserisci nome\n')
        c = input('inserisci cognome\n')
        for s in studenti:
            if s['nome'] == n and s['cognome'] == c:
                print(n,c,'--->', sum(s['voti'])/len(s['voti']))
    if op ==5:
        break
'''

# MATRICI

mat = []
n = 2
'''
for i in range (n):
    r = []
    for j in range(n):
        r.append(int(input('Inserisci numero\n')))
    mat.append(r)

print(mat)
'''
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

for r in mat:
    for j in range(len(r)):
        print(r[j],end= ' ')
    print()

summ = 0
for r in mat:
    sum+= summ(r)
print(summ)

maxi = 0
for i in range(1,len(mat)):
    if sum(mat[maxi]) < sum(mat[i])
        maxi = i

print(mat[maxi])
'''