#. Crie um algoritmo para resolver equações do 2º grau. Considere:
# ax2 + bx + c = 0 (a deve ser diferente de 0)
# delta = b2 - 4 * a * c
#Caso: delta < 0, não existe raiz real
#delta = 0, existe uma raiz real: x = (-b) / (2 * a)
#delta > 0, existem duas raízes reais:
#x1 = (- b + raiz quadrada de delta) / (2 * a)
#x2 = (- b - raiz quadrada de delta) / (2 * a)

import math

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

delta = (b ** 2) - 4 * a * c

if a != 0:
    if delta < 0:
        print("Não existe raiz real")
    elif delta == 0 :
        resultado = (-b) / (2 *a)
        print(f"Existe uma raiz real = {resultado} ")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a) #Utilizando a biblioteca math
        x2 = (-b - (delta ** 0.5)) / (2 * a ) #Sem função sqrt
        print(f"Existe duas raizes reais\n Raiz 1 = {x1:.2f}\n Raiz 2 = {x2:.2f}")
else:
    print("Não é possível resolver com A sendo 0");
    
    
    