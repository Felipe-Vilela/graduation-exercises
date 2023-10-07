# Faça um programa que gere aleatoriamente um número entre 0 e 100. Em seguida, o programa deve pedir que o usuário tente acertar qual o número gerado. Por
# exemplo, suponha que o programa gere o número 21 e o usuário tente adivinhálo digitando o número 50. O programa deve, então, imprimir a mensagem:
# “Número incorreto, tente um valor menor”. O usuário digita, então, o número 10.
# Após a análise deste número, o programa deverá imprimir a mensagem “Número incorreto, tente um valor maior”. O processo deve continuar até que o usuário
# acerte o número gerado pelo programa. O programa deve finalizar informando o número de tentativas até o acerto.

import random

aleatorio = random.randint(0,100)
tentativas = 1

numeroDigitado = int(input("Tente adivinhar o número: "))

while numeroDigitado != aleatorio:
    tentativas += 1
    if numeroDigitado > aleatorio:
        numeroDigitado = int(input("Número incorreto, tente um número menor: "))
    else:
        numeroDigitado = int(input("Número incorreto, tente um número maior: "))

print(f"Parabéns!! você acertou após {tentativas} tentativas")