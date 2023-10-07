# Crie uma função que receba como parâmetro um número inteiro. A função
# deve retornar um número inteiro, conforme a seguir:
# a) Retornar 1 se o número recebido é positivo
# b) Retornar -1 se o número recebido é negativo
# c) Retornar 0 se o número recebido é zero

def verificacao(n1):
    if n1 > 0:
        return 1
    elif n1 < 0:
        return -1
    else:
        return 0

def main():
    numero = int(input("Informe o valor: "))
    retorno = verificacao(numero)
    if retorno == 1:
        print(f"Resultado da verificação é : {retorno} e o número : {numero} é positivo!")
    elif retorno == -1:
        print(f"Resultado da verificação é : {retorno} e o número : {numero} é negativo!")
    else:
        print(f"Resultado da verificação é : {retorno} e o número : {numero} é zero!")


main()