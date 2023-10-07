# Faça um programa que solicite o nome do usuário e imprima-o na
# vertical e em formato de escada.

nome =str(input("Escreva o seu nome: "))
letrasNome = []

for i in range(len(nome)):
    letrasNome.append(nome[i])


for i in range(len(letrasNome)):
    j = 0
    while j <= i:
        print(letrasNome[j],end="")
        j+=1
    print()
    
    
       
