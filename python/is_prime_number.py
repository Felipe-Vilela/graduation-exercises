#. Faça um programa que receba um número inteiro maior que 1,
#verifique se o número é primo ou não e mostre a mensagem denúmero primo ou de número não primo.
# Obs: Um número éprimo quando é divisível apenas por 1 e por ele mesmo.


numero = int(input("Digite um número maior que um: "))

if numero > 1 :
    cont = 1
    qtdDivisores = 0
    divisao = None
    while cont <= numero:
        divisao = numero % cont 
        if divisao == 0:
            qtdDivisores += 1
        cont += 1

    if qtdDivisores == 2:
        print(f"O número : {numero} é primo")
    else:
        print(f"O número : {numero} não é primo")   
       
        
else:
    print("Número informado não é maior que 1")
    
    


