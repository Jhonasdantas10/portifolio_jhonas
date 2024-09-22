while True:

    numero1 = input("digite um numero:")
    numero2 = input("digite outro numero:")
    operador = input("digite um operador:")

    numeros_validos = None

    try:
         numero1_float = float(numero1)
         numero2_float = float(numero2)
         numeros_validos = True
    except:
         numeros_validos = None

    if numeros_validos is None:
         print("um ou ambos numeros digitados sao invalidos")
         continue ## volta pro inicio do codigo
    
    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
         print("digite um operado valido")
         continue

    if len(operador) >1:
         print("digite so um operador")
         continue

    print("seu resultado")
    if operador == '+':
     print(numero1_float + numero2_float)
         
     
     




    sair = input("digite [s]air, para sair:" ).lower().startswith('s')

    if sair is True:
         break 
    
