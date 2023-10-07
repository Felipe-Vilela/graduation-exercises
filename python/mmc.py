# Faça um programa que calcule e apresente o mmc entre dois números

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

multiplicador1 = 1
resultado1 = 0
resultado2 = 1


while resultado2 != resultado1   :
    resultado1 = multiplicador1 * numero1
    multiplicador2 = 1
    resultado2 = 1
    while resultado2 <= resultado1 and resultado1 != resultado2:
        resultado2 = multiplicador2 * numero2
        multiplicador2 += 1
    multiplicador1 += 1

mmc = resultado1 and resultado2
print(mmc)











