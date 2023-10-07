#Faça um programa que mostre os 8 primeiros termos dasequência de Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8,13, 21,34, 55...

def formula(num1,num2):
    return num1 + num2

termo1 = 0
termo2 = 1
termox = formula(termo1,termo2)
cont = 3

print(f"Termo 1 : {termo1}\nTermo 2 : {termo2}")

while cont <= 8:
    print (f"Termo {cont} : {termox}")
    termo1 = termo2
    termo2 = termox
    termox = formula(termo1,termo2)
    cont += 1
    