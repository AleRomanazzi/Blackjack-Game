import random
from urllib import response

extra = 10

#Cartas especiales
As = ["as", 10]
jota = ["jota", 10]
reina = ["reina", 10]
rey = ["rey", 10]

#Baraja
baraja = [As, 2, 3, 4, 5, 6, 7, 8, 9, 10, jota, reina, rey]

#Composicion completa, 52 naipes
barajaFrancesa = {
    "trebol" : baraja,
    "diamante": baraja,
    "corazon": baraja,
    "pica" : baraja
}

#print(barajaFrancesa)

#Toma carta aleatoria de la baraja
def barajaAleatoria():
    azar2 = baraja[random.randint(1, len(baraja)-1)]
    return azar2


def carteo():
    azar = random.randint(1, 4)
    if azar == 1:
        carta = barajaAleatoria()
        print("trebol ", carta)
    elif azar == 2:
        carta = barajaAleatoria()
        print("diamante ", carta)
    elif azar == 3:
        carta = barajaAleatoria()
        print("corazon ", carta)
    elif azar == 4:
        carta = barajaAleatoria()
        print("pica ", carta)
    return carta
     
#Reparto de carta al crupier     
def crupier():
    cartaCrupier = carteo()
    return cartaCrupier

#Pedir otra carta
def pedir():
    ask = int(input("Quieres otra?\n1)Si\n2)No\n"))
    if ask == 1:
        cartaExtra = barajaAleatoria()
        print(f"Nueva carta: {cartaExtra} ")
    else:
        cartaExtra = 0
    return cartaExtra

#Checkear que no se pase de 21
def check(x):
    if x > 21:
        print(x, ", te pasaste.")
        a = 0
    else:
        print("Tus cartas son: ", x)
        a = 1
    return a

#Versus contra carta de crupier
def versus(x, y):
    if primeraCartaCrupier > reparto:
        print("Perdiste")
    elif primeraCartaCrupier < reparto:
        print("Ganaste")
    elif primeraCartaCrupier == reparto:
        print("Empate")


#Inicio - testeo

primeraCarta = carteo()
segundaCarta = carteo()
if type(primeraCarta) == list:
    primeraCarta = primeraCarta[1]
elif type(segundaCarta) == list:
    segundaCarta = segundaCarta[1]
reparto = primeraCarta+segundaCarta
print(f"Tus cartas suman: {reparto}")
primeraCartaCrupier = crupier()
if type(primeraCartaCrupier) == list:
    primeraCartaCrupier = primeraCartaCrupier[1]
print(f"Primera carta del dealer: {primeraCartaCrupier}")

while True:    
    c = pedir()
    if type(c) == list:
        c = c[1]
    if c == 0:
        break
    reparto+=c
    f = check(reparto)
    if f == 0:
        break
    otra = int(input(f"Tus cartas suman: {reparto}\nDeseas otra?\n"))
    if otra == 1:
        continue
    else:
        break
    
versus(reparto, primeraCartaCrupier)   



