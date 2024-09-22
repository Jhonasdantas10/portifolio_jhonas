import random

numero = random.randint(1,100)


advinha = 0
chances = 0
while advinha != numero and chances <3:
    chances += 1
    advinha = int(input("tente advinhar o numero: ""(entre 1 e 100:)"))
    if advinha < numero:
        print("muito baixo")
    elif advinha > numero:
        print("muito alto")
    else:
        print("acertou")
    
if advinha != numero:
    print("suas tentativas acabaram, o numero era",numero)
