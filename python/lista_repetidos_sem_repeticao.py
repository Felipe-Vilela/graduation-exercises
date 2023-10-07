# Crie um programa que leia inicialmente uma sequencia de N números inteiros. Depois, o programa deve gerar e mostrar 2 novas listas apartir da primeira:
# uma sem repetição de elementos e outra com oselementos que se repetem na lista original.

seqOriginal = []
seqSemRepitidos = []
seqRepetidos = []

elementos = int(input("Informe o número de elementos: "))

for i in range(0, elementos):
    numero = int(input("Informe um valor: "))
    seqOriginal.append(numero)

    if numero not in seqSemRepitidos:
        seqSemRepitidos.append(numero)
    else:
        seqRepetidos.append(numero)

print(f"Sequência original: {seqOriginal}")
print(f"Sequência sem elementos repetidos: {seqSemRepitidos}")
print(f"Sequência somente com os elementos repetidos: {seqRepetidos}")