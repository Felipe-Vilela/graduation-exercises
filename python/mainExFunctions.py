#FALTA FAZER EX 11 DE ANAGRAMAS :)

def menu():
    print("MENU DE OPÇÕES")
    print("1, inteiro positivo") #EXERCÍCIO 1
    print("2, inteiro positivo ou negativo")#EXERCÍCIO 2
    print("3, real")#EXERCÍCIO 3
    print("4, verificar neg, pos ou zero")#EXERCÍCIO 4
    print("5, Media final") #EXERCÍCIO 5
    print("6, Fatorial")
    print("7, Unir ")
    print("8, Intersecção ")
    print("9, Diferença ")
    print("10, Calcular: União, Intersecção ou Diferença ")
    print("11, Sair")
    opcao = int(input("Escolha uma opção entre 1 e 10 ou escolha 11 para encerrar o programa: "))
    return opcao

def InteiroPositivo(n): #EXERCÍCIO 1
    ehInt = False
    contFalse = 0
    for i in range(len(n)):
        if i != 0:
            if n[i] == '-':
                contFalse+=1
        if n[i]=='0' or n[i]=='1' or n[i]=='2' or n[i]=='3' or n[i]=='4' or n[i]=='5' or n[i]=='6' or n[i]=='7' or n[i]=='8' or n[i]=='9' :
            ehInt = True
        else:
            contFalse +=1
        if contFalse != 0:
            ehInt = False
    return ehInt

def Inteiro(n): #EXERCÍCIO 2
    ehNum = False
    contFalse = 0
    for i in range(len(n)):
        if i != 0:
            if n[i] == '-':
                contFalse+=1
        if contFalse == 0:
            if n[i]=='0' or n[i]=='1' or n[i]=='2' or n[i]=='3' or n[i]=='4' or n[i]=='5' or n[i]=='6' or n[i]=='7' or n[i]=='8' or n[i]== '9' or n[i]=='-':
                ehNum = True
            else:
                contFalse +=1
        if contFalse != 0:
            ehNum = False
    return ehNum

def Real(n): #EXERCÍCIO 3
    ehReal = False
    contFalse = 0
    for i in range(len(n)):
        if i != 0:
            if n[i] == '-':
                contFalse+=1
        if contFalse == 0:
            
            if n[i]=='0' or n[i]=='1' or n[i]=='2' or n[i]=='3' or n[i]=='4' or n[i]=='5' or n[i]=='6' or n[i]=='7' or n[i]=='8' or n[i]== '9' or n[i]=='-' or n[i]=='.':
                ehReal = True
            else:
                contFalse +=1
        if contFalse != 0:
            ehReal = False
    return ehReal

def verificacao(n): #EXERCÍCIO 4
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def media_final(n): #EXERCÍCIO 5
    soma = 0
    for i in range(len(n)):
        soma = soma + n[i]
    media = soma / 4
    return media

def fatoria_num(n): #EXERCÍCIO 6
    ehIntPos = InteiroPositivo(n)
    fatorial = 1
    
    if ehIntPos == True:
        numero = int(n)
        while numero >= 1:
            fatorial = fatorial * numero
            numero-=1
        return fatorial

    else:
        return ehIntPos
def uniao(l1,l2): #EXERCÍCIO 7
    lista_uniao = []
    for i in range(len(l1)):
        if l1[i] not in lista_uniao:
            lista_uniao.append(l1[i])
    for i in range(len(l2)):
        if l2[i] not in lista_uniao:
            lista_uniao.append(l2[i])
    return lista_uniao

def interseccao(l1,l2): #EXERCÍCIO 8
    lista_interseccao = []
    for i in range(len(l1)):
        c = 0
        while c < len(l2):
            if l1[i] == l2[c]:
                lista_interseccao.append(l1[i])
            c+=1
    return lista_interseccao

def diferenca(l1,l2): #EXERCÍCIO 9
    lista_diferenca = []
    for i in range(len(l1)):
        if l1[i] not in l2:
            lista_diferenca.append(l1[i])
    for i in range(len(l2)):
        c=0
        while c < len(l1):
            if l2[i] not in l1 and l2[i] not in lista_diferenca:
                lista_diferenca.append(l2[i])
            c+=1
    return lista_diferenca

def calcular_UID(l1,l2,resposta):#EXERCÍCIO 10
    if resposta == 'u':
        return uniao(l1,l2)
    elif resposta == 'i':
        return interseccao(l1,l2)
    elif resposta == 'd':
        return diferenca(l1,l2)
    else:
        return False

def main():
    opcao = 1
    while opcao >=1 and opcao <12:
        opcao = menu()
        if opcao == 1:
            string = input("Informe a string: ")
            ehIntPos = InteiroPositivo(string)
            if ehIntPos == True:
                number = int(string)
                if number > 0:
                    print(f"o número {number} é positivo")
            else:
                print(f"A string '{string}' não é um número positivo")
        elif opcao == 2:
            string = input("Informe a string: ")
            ehNumero = Inteiro(string)
            if ehNumero == True:
                number = int(string)
                if number > 0:
                    print(f"o número {number} é positivo")
                elif number < 0:
                    print(f"o número {number} é negativo")
                else:
                    print(f"o número é zero!!")
            else:
                print(f"A string '{string}' não é um número")
        elif opcao==3:
            string = input("Informe a string: ")
            ehReal = Real(string)
            if ehReal == True:
                numReal = float(string)
                print(f"O número {numReal} é um número real.")
            else:
                 print(f"A string '{string}' não é um número")
        elif opcao==4:
            numero = int(input("Informe o valor desejado: "))
            returnFunction = verificacao(numero)
            if returnFunction == 1:
                 print(f"Resultado da verificação é : {returnFunction} e o número : {numero} é positivo!")
            elif returnFunction == -1:
                print(f"Resultado da verificação é : {returnFunction} e o número : {numero} é negativo!")
            else:
                print(f"Resultado da verificação é : {returnFunction} e o número : {numero} é zero!")
        elif opcao==5:
            notas = []
            print("Informe 4 notas:")
            i = 0
            while i < 4:
                string = input("Informe a nota: ")
                notaIsReal = Real(string)
                if notaIsReal == True:
                    nota = float(string)
                    notas.append(nota)
                    i+=1
            media = media_final(notas)
            print("A média final do aluno foi %.2f"%(media))
            #Mesmo print acima porém de outra maneira
            # print(f"A média final do aluno foi {media:.2f}")

        elif opcao == 6:
            string = input("Informe a string: ")

            retorno = fatoria_num(string)
            if retorno == False:
                print(f"A string '{string}' não é um número inteiro e positivo.")
            else:
                print(f"O fatorial de {string} é : {retorno}")

        elif opcao == 7:
            lista1 = []
            lista2 = []

            parar = int(input("Quantos elementos você irá digitar? "))
            i = 0
            while i < parar:
                numero = int(input("Informe o valor inteiro para primeiro conjunto: "))
                lista1.append(numero)
                numero = int(input("Informe o valor inteiro para segundo conjunto: "))
                lista2.append(numero)
                i+=1
            
            lista_uniao = uniao(lista1,lista2)
            print("Lista união:",end=" ")
            for i in range(len(lista_uniao)):
                if i ==len(lista_uniao)-1:
                    print(f"{lista_uniao[i]}")
                else:
                    print(f"{lista_uniao[i]}",end=",")


            print()
        elif opcao == 8:
            lista1 = []
            lista2 = []

            parar = int(input("Quantos elementos você irá digitar? "))
            i = 0
            while i < parar:
                numero = int(input("Informe o valor inteiro para primeiro conjunto: "))
                lista1.append(numero)
                numero = int(input("Informe o valor inteiro para segundo conjunto: "))
                lista2.append(numero)
                i+=1
            lista_interseccao = interseccao(lista1,lista2)
            print("Lista intersecção:",end=" ")
            for i in range(len(lista_interseccao)):
                if i ==len(lista_interseccao)-1:
                    print(f"{lista_interseccao[i]}")
                else:
                    print(f"{lista_interseccao[i]}",end=",")
            print()

        elif opcao == 9:
            lista1 = []
            lista2 = []

            parar = int(input("Quantos elementos você irá digitar? "))
            i = 0
            while i < parar:
                numero = int(input("Informe o valor inteiro para primeiro conjunto: "))
                lista1.append(numero)
                numero = int(input("Informe o valor inteiro para segundo conjunto: "))
                lista2.append(numero)
                i+=1
            lista_diferenca = diferenca(lista1,lista2)
            print("Lista diferença:",end=" ")
            for i in range(len(lista_diferenca)):
                if i ==len(lista_diferenca)-1:
                    print(f"{lista_diferenca[i]}")
                else:
                    print(f"{lista_diferenca[i]}",end=",")
            print()

        elif opcao == 10:
            lista1 = []
            lista2 = []

            parar = int(input("Quantos elementos você irá digitar? "))
            i = 0
            while i < parar:
                numero = int(input("Informe o valor inteiro para primeiro conjunto: "))
                lista1.append(numero)
                numero = int(input("Informe o valor inteiro para segundo conjunto: "))
                lista2.append(numero)
                i+=1
            calculo_escolhido = input("Informe o calculo desejado, para União 'U', para Intersecção 'I', para Diferença 'D':").lower()
            resultado = calcular_UID(lista1,lista2,calculo_escolhido)
            if resultado == False:
                print("Foi escolhido um calculo inválido !!!")
            else:
                for i in range(len(resultado)):
                    if i ==len(resultado)-1:
                        print(f"{resultado[i]}")
                    else:
                        print(f"{resultado[i]}",end=",")
            print()
        print("---" *25)

main()