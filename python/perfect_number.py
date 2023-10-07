# . Escreva um programa que apresente os 5 primeiros números perfeitos. Um
# número perfeito é aquele que é igual a soma dos seus divisores (por exemplo, 6 =
# 1+2+3 e 28= 1+2+4+7+14). 


numero = 2
qtdNumeros = 0
while qtdNumeros < 5:
    c = 1
    soma = 0
    while c  <= numero // 2 +1  :
        if numero % c == 0:
            soma = soma + c
        c += 1
    if soma == numero:
        qtdNumeros += 1
        print(numero)
    numero+=1
    

