# Faça um programa que solicite do usuário os elementos de uma matriz 3x 2 (matriz A).
# Em seguida, o programa deverá criar a matriz transpostade A (At).
# Ao final, deve ser mostrada a matriz original e sua respectivatransposta. 
# Lembre-se que a matriz transposta At será obtida a partir damatriz A trocando-se ordenadamente as linhas por colunas (ou ascolunas por linhas), 

def criar_matriz(linhas,colunas):
    mat=[]
    for i in range(linhas):
        mat.append([])
        for j in range(colunas):
            numero=int(input(f"Informe o valor para posição {[i]} {[j]}: "))
            mat[i].append(numero)
    return mat


def imprimir_matriz(linhas,colunas,mat):
    for i in range(linhas):
        for j in range(colunas):
            print(f"{mat[i][j]}",end=" ")
        print()

def gerar_matriz_transposta(linhas,colunas,mat):
    mat_transposta = []
    for i in range(linhas):
        mat_transposta.append([])
        for j in range(colunas):
            mat_transposta[i].append(mat[j][i])
    return mat_transposta

def main():

    m = 3
    n = 2

    matriz_original=criar_matriz(m,n)
    print("Matriz original: ")
    imprimir_matriz(m,n,matriz_original)
    print("Matriz transposta: ")
    matriz_transposta=gerar_matriz_transposta(n,m,matriz_original)
    imprimir_matriz(n,m,matriz_transposta)

main()