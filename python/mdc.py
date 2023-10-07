# Faça um programa que calcule e apresente o mdc entre dois números. 

#MDC CALCULADO ATRAVÉS DE DIVISÕES SUCESSIVAS
#Primeiro divido numero maior pelo menor, depois vou dividindo até dar uma divisão exata, isso no primeiro if e else
#No segundo if e else é para mim pegar o divisor da divisão exata que no caso é o mdc

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

resto = 1
mdc = None

while resto != 0:

    if numero1 > numero2:
        resto = numero1 % numero2
        numero1 = resto
        
    else:
        resto = numero2 % numero1
        numero2 = resto
    
    if numero1 != 0:
        mdc = numero1
    else:
        mdc = numero2
    
print(f"MDC = {mdc}")

