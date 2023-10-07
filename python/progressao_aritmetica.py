# Escreva um programa que leia um número n (número de termos de uma progressão aritmética), a1 (o primeiro termo da progressão) e r (a razão da
# progressão) e apresenta os n termos desta progressão, bem como a soma de todos elementos. 

n = int(input("Digite número de termos de uma progressão aritmética: "))
al = float(input("Digite qual o primeiro termo da progressão: "))
r = float(input("Digite a razão da progressão: "))

somaPA = (n / 2.0) * (2 * al + (n - 1) * r)
termo = 1
while termo <= n:

    calculo = al + (termo -1) * r
    if termo == 1:
        print(f"Termos da PA = ( {calculo} , ", end = "")
    elif termo != 1 and termo != n:
        print(f"{calculo} , ", end = "")
    else:
        print(f"{calculo})")

    termo += 1



print(f"Soma dos termos da PA = {somaPA}")
print("----------\nAGORA COM FOR\n-----------")


for termo in range (1,n + 1):
    calculo = al + (termo -1) * r
    if termo == 1:
        print(f"Termos da PA = ( {calculo} , ", end = "")
    elif termo != 1 and termo != n:
        print(f"{calculo} , ", end = "")
    else:
        print(f"{calculo})")

print(f"Soma dos termos da PA = {somaPA}")



