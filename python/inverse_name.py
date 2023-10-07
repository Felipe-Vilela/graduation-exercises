# Faça um programa que permita ao usuário digitar o seu nome e emseguida o mostre de trás para frente utilizando somente letras maiúsculas.

nome = input("Digite seu nome: ").upper()

i = len(nome)-1

print("Nome invertido em maiúsculo: ")
while i >= 0:
    print(nome[i],end="")
    i-=1
    