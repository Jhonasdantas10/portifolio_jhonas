palavra_valida = "jhonas"
tentativas = 0


letra = input("digite uma letra:")
tentativas += 1

if letra in palavra_valida:
    print(letra)

else:
    print("*")
    continue


print(tentativas)
