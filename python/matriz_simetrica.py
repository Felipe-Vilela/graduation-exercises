# Faça um programa que solicite do usuário um valor N, representandoa dimensão de uma matriz quadrada (matriz A).
# Em seguida, oprograma deverá solicitar do usuário os elementos da matriz A e, posteriormente, deverá verificar se A é simétrica.
# Obs: Matrizsimétrica: matriz quadrada de ordem n tal que A = At

def criar_matriz(linhas,colunas):
    mat=[]
    for i in range(linhas):
        mat.append([])
        for j in range(colunas):
            numero=int(input(f"Informe o valor para posição {[i]} {[j]}: "))
            mat[i].append(numero)
    return mat

def gerar_matriz_transposta(linhas,colunas,mat):
    mat_transposta = []
    for i in range(linhas):
        mat_transposta.append([])
        for j in range(colunas):
            mat_transposta[i].append(mat[j][i])
    return mat_transposta

def eh_simetrica(matA,matB,ordem):
    is_simetric = True
    for i in range(ordem):
        for j in range(ordem):
            if matA[i][j] != matB[i][j]:
                is_simetric = False
    return is_simetric

def imprimir_matriz(linhas,colunas,mat):
    for i in range(linhas):
        for j in range(colunas):
            print(f"{mat[i][j]}",end=" ")
        print()

def main():
    n = int(input("Informe a ordem da matriz quadrada: "))

    matriz = criar_matriz(n,n)
    matriz_transposta=gerar_matriz_transposta(n,n,matriz)

    if eh_simetrica(matriz,matriz_transposta,n) == True:
        print("A matriz: ")
        imprimir_matriz(n,n,matriz)
        print("é simetrica")
    else:
        print("A matriz: ")
        imprimir_matriz(n,n,matriz)
        print("não é simetrica")

main()