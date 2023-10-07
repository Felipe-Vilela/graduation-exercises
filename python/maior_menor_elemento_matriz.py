# Crie um programa que solicita do usuário um valor N representando aquantidade linhas e um valor M representando 
#a quantidade de colunas de uma matriz. Depois, o programa deverá solicitar do usuário N x M elementos para serem incluídos na matriz. Por fim,
# o programa deverá percorrer a matriz para encontrar e imprimir o seu maior elemento e o seu menor elemento.

def criar_matriz(linhas,colunas):
    mat=[]
    for i in range(linhas):
        mat.append([])
        for j in range(colunas):
            numero=int(input(f"Informe o valor para posição {[i]} {[j]}: "))
            mat[i].append(numero)
    return mat

def eh_maior(linhas,colunas,mat):
    maior = mat[0][0]

    for i in range(linhas):
        for j in range(colunas):
            if mat[i][j] > maior:
                maior=mat[i][j]
    return maior

def eh_menor(linhas,colunas,mat):
    menor = mat[0][0]

    for i in range(linhas):
        for j in range(colunas):
            if mat[i][j] < menor:
                menor=mat[i][j]
    return menor

def imprimir_matriz(m,n,mat):
    for i in range(m):
        for j in range(n):
            print(f"{mat[i][j]}",end=" ")
        print()


def main():

    m=int(input("Informe o numero de linhas: "))
    n=int(input("Informe o numero de colunas: "))

    matriz = criar_matriz(m,n)
    maior = eh_maior(m,n,matriz)
    menor = eh_menor(m,n,matriz)

    print(f"Maior valor na lista : {maior}")
    print(f"Menor valor na lista : {menor}")

    print("Matriz: ")
    imprimir_matriz(m,n,matriz)
 





main()


