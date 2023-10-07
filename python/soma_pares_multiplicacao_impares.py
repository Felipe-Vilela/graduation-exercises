# Crie um programa que leia inicialmente uma sequência de N números inteiros e ao seu final mostre a sequência original,
# a soma de seus elementos que forem pares e a multiplicação dos elementos que forem ímpares.

sequencia = []
soma = 0
multiplicacao = 1
ehImpar = False

elementos = int(input("Informe a quantidade de elementos: "))

for i in range(0,elementos):
    numero = int(input("Informe um valor: "))
    sequencia.append(numero)

for i in range(len(sequencia)):
    if sequencia[i]%2==0:
        soma = soma + sequencia[i]
    else:
        ehImpar = True
        multiplicacao= multiplicacao + (multiplicacao * sequencia[i] )

if ehImpar == False:
    multiplicacao = 0
   

print(f"Sequencia = {sequencia}\nSoma = {soma}\nMultiplicacao = {multiplicacao}")
    

