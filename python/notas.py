# Crie um programa que leia inicialmente uma sequência de N notas dealunos fornecidas pelo usuário e ao final mostre a sequência e sua média aritmética. 
# Defina um critério de parada para a entrada denotas pelo usuário.

notas = []

soma = 0
divisor = 0
nota = float(input("Digite uma nota: "))
while nota >= 0:
    notas.append(nota)
    soma = soma + nota
    divisor += 1
    nota = float(input("Digite outra nota e caso deseje parar digite um valor negativo: "))
    
divisao = soma / divisor

print(f"Sequência : {notas}\nMédia : {divisao}")