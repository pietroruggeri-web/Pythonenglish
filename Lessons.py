
#  WORKING WITH STRINGS

print("Giraffe\nAcademy")  # a capo
print("Giraffe\"Academy")  # per inserire le virgolette
phrase = "Giraffe Academy"
print(phrase + "is cool")  # concatenazione di stringhe
phrase = "Giraffe Academy"
print(phrase.lower())  # per avere tute le lettere minuscole viceversa upper
print(phrase.upper().isupper())  # operatori Boole
print(len(phrase))  # conta i caratteri
print(phrase[0])  # prima lettera della parola
print(phrase.index(
    "a"))  # cosa corrisponde il valore messo esempio a = 3/se il valore non è compreso da errore perchè non trova la lettera/numero
print(phrase.replace("Giraffe", "Elephant"))  # sostituire un valore con un altro

#  WORKING WITH NUMBERS

import math  # solo le operazioni di matematica base sono in pyhon per le altre devo importare la libreria math

print(3 + 5)
print(10 % 3)  # resto della divisione
my_num = 5
print(str(my_num) + "my favorite number")  # convertire numero in stringa, se non metto (str) mi da errore
print(abs(my_num))  # valore asoluto
print(pow(4, 2))  # elevamento a potenza
print(max(4, 6))  # massimo numero nell'intervallo
print(min(4, 6))  # minimo numero nell'intervallo
print(round(3.5))  # arrotonda il numero
print(math.sqrt(36))  # radice quadrata di un numero

#  GETTING INPUT FROM USERS

name = input("Enter your name: ")
age = input("Enter your age: ")  # int(input(...) si utilizza per le operazioni, mentre l'altro per le stringhe input...

print("Hello " + name + "!" " You are " + age)

#  BUILDING A BASIC CALCULATOR

num1 = int(input("Enter a number: "))  # int = numeri interi
num2 = float(input("Enter another number: "))  # float = numeri decimali
result = num1 + num2

print(result)

#  MAD LIBS GAME

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + "are blue")
print("I love " + celebrity)

#  LISTS

friends = ["Kevin", "Karen", "Rossi", "Tony"]  # puoi inderidci quello che vuoi stringhe,bool,numeri...
print(friends[0])  # Tira fuori il valore corrispondente [0,1,2...]
print(friends[0:2])  # Tira fuori i valori da 0 a 2 esclusi quindi in questo caso tutti i valori della lista
friends[1] = 'Mike'  # Sostituire il valore di una lista con un altro
print(friends[1])
print(friends[0:])  # Tira fuori i valori da 0 a tutta la lista

#  LIST FUNCTIONS

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Alfa", "Alfa", "Beta", "Gamma"]
friends.extend(lucky_numbers)  # Sommare due liste tra di loro
friends.append("Delta")  # Appendere = Aggiungere una qualcosa alla lista
friends.insert(1, "Kelly")
friends.remove("Gamma")
friends.pop()  # Cancella l'ultimo elemento dalla lista
friends.clear()

print(friends.index("Kelly"))  # Posizione dove si trova un elemento nella lista
friends.sort()  # Ordina gli elementi
print(friends.count("Beta"))  # Conta gli elementi della parola che cerco
lucky_numbers.reverse()  # Invertire gli elementi della lista
friends2 = friends.copy()  # Copiare la lista
print(friends2)

#  TUPLES

coordinates = (4, 5)  # Quando si crea una taple non si può modificare ne calcellare, se una lista puoi modificare ciò che vuoi
print(coordinates[0])

#  FUNCTIONS

def say_hi(name, age):
    print("Hello" + name + " , you are" + str(age))

say_hi("Mike", 35)
say_hi("John", 70)

#  RETURN STATEMENT

def cube(num):
    return num * num * num
result = cube(4)
print(result)
print(cube(3))

#  IF STATEMENTS

m = True
a = True

if a and m:
    print("You are a male or tall or both")
elif a and not m:
    print("")
else:
    print("You neither a male nor tall")

#  IF STATEMENTS AND COMPARISON

