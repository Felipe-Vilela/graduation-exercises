#Faça um programa que leia um número inteiro >= 0 e calcule o seu fatorial.

numero = int(input("Digite um número: "))
multiplicacao = 1

if numero >= 0:
    print(f"{numero}! = ", end = "")
    while numero >= 1:
        if numero != 1:
            print(f"{numero} x ", end = "")
        else:
            print(f"{numero} = ", end = "")
        multiplicacao = numero * multiplicacao       
        numero -= 1
    print(f"{multiplicacao}")    


