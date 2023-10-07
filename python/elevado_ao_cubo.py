# Crie um programa que dada uma sequência de N elementos fornecidos pelo usuário mostre a sequência original e a sequência elevada ao cubo.

seqOriginal = []
seqCubo = []

elementos = int(input("Quantos elementos irá digitar : "))

for i in range(0,elementos):
    elemento = int(input("Digite um elemento: "))
    seqOriginal.append(elemento)
    elemento = elemento ** 3
    seqCubo.append(elemento)

print(f"Sequência original : {seqOriginal}")
print(f"Sequência elevada ao cubo : {seqCubo}")