#Escreva um programa que remove a primeira ocorrência de uma letra de uma string. A string e a letra devem ser fornecidas pelo usuário.

string = input("Digite a string: ")
letra = input("Informe a letra a ser retirada em sua primeira aparição: ")
stringComLetraRemovida = ""

aparicao = 0
pos = 0

for i in range(len(string)):
    if string[i] == letra and aparicao < 1:
        aparicao+=1
        pos = i
stringComLetraRemovida = string[:pos] + string[pos +1 :]
      
print(f"A letra a ser removida é: {letra}\nString após removar a letra em sua primeira aparição: \n{stringComLetraRemovida}")





        


