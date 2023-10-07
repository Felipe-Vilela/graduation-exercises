# Crie um programa que leia inicialmente uma sequência de N
# números inteiros fornecidos pelo usuário e mostre ao final da leitura a sequência original e a sequência invertida.

seqOriginal = []
seqInvertida = []

elementos = int(input("Informe a quantidade de elementos: "))

for i in range(0,elementos):
    elemento = int(input("Informe um elemento: "))
    seqOriginal.append(elemento)

for i in range(len(seqOriginal)-1, -1, -1):
    elemento = seqOriginal[i]
    seqInvertida.append(elemento)

#INVERTIDA COM WHILE 
i = len(seqOriginal) - 1
while i>=0:
    elemento = seqOriginal[i]
    seqInvertida.append(elemento)
    
    i-=1

print(f"Sequência original: ")
for i in range(len(seqOriginal)):
    print(seqOriginal[i],end=' ')
print(' ')
print(f"Sequência invertida: ")
for i in range(len(seqInvertida)):
    print(seqInvertida[i],end=' ')
print(' ')

