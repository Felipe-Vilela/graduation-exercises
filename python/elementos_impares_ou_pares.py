# Crie um programa que leia inicialmente uma sequência de N elementosinteiros positivos fornecidos pelo usuário e substitua seus elementos devalor ímpar por -1 e os pares por +1.
#Ao final imprima a sequênciaoriginal e a sequência alterada

seqOriginal = []
seqAlterada = []

elementos = int(input("Informe a quantidade de elemetos: "))

for i in range(0,elementos):
    numero = int(input("Informe um valor: "))
    seqOriginal.append(numero)

for i in range(len(seqOriginal)):
    if seqOriginal[i]%2==0:
        numero = seqOriginal[i] + 1
        seqAlterada.append(numero)
    else:
        numero = seqOriginal[i] - 1
        seqAlterada.append(numero)

print(f"Sequência original: {seqOriginal}")
print(f"Sequência alterada: {seqAlterada}") 


