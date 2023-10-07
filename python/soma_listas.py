# Crie um programa que leia inicialmente duas sequências de Nelementos cada uma
#  e ao final mostre as duas sequências originais e asequência resultante da soma de seus elementos

listaA = []
listaB = []
listaSoma = []

n1 = int(input("Quantos elementos vai ter na lista A ? "))
n2 = int(input("Quantos elementos vai ter na lista B ? "))


for i in range(0,n1):
    numero = int(input("Digite um número para lista A: "))
    listaA.append(numero)

for i in range(0,n2):
    numero = int(input("Digite um número para lista B: "))
    listaB.append(numero)

print(f"Lista A:")
for i in range(len(listaA)):
    print(listaA[i],end=' ')
print(" ")

print(f"Lista B:")
for i in range(len(listaB)):
    print(listaB[i],end=' ')
print(" ")

#VERIFICAR SE TEM A MESMA QTD DE ELEMENTOS E ADC 0 NO FINAL CASO SEJA NECESSARIO
subtracaoElementos = len(listaA) - len(listaB)
while subtracaoElementos != 0:
    if subtracaoElementos < 0:
        listaA.append(0)
    else:
        listaB.append(0)
    subtracaoElementos = len(listaA) - len(listaB)

#SOMA DAS LISTAS
i = 0
while i < len(listaA) or i < len(listaB):
    numero = listaA[i] + listaB[i]
    listaSoma.append(numero) 
    i += 1

print(f"Lista com as Somas: ")
for i in range(len(listaSoma)):
    print(listaSoma[i],end=' ')



