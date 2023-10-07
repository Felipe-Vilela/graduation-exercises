#Faça um programa que crie uma lista com 10 números inteiros fornecidos pelo usuário. Após criar a lista, o programa deverá imprimir:
#O maior elemento da lista
#O menor elemento da lista
#A soma de todos os elementos da lista
#Os elementos ímpares
#Os elementos maiores do que 18
#15,10,12,23,40,9,8,1,55,26


numeros = []

for i in range(0,10):
    numero = int(input("Digite o número: "))
    numeros.append(numero)

    i+=1

print(f"\nLista de números: {numeros}")

maior = numeros[0]
for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
print(f"\nMaior = {maior}")

i = 0
menor = numeros[0]
while i < len(numeros):
    if numeros[i] < menor:
        menor = numeros[i]
    i+=1
print(f"\nMenor = {menor}")

soma = 0
for i in range(len(numeros)):
    soma = soma + numeros[i]
print(f"\nSoma = {soma}\n")

i=0
while i < len(numeros):
    if i == 0:
        print("Impares: ", end = "")
    if numeros[i]%2!=0:
        print(f"{numeros[i]} ", end = "")
        
    i+=1
print("\n")
for i in range(len(numeros)):
    if i == 0:
        print(f"Maiores que 18: ", end = "")
    if numeros[i] > 18:
        print(f"{numeros[i]} ", end = "")
print("\n")




