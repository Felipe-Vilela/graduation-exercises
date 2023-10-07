# Escreva um programa que leia inteiros positivos m e n e os elementosde uma matriz A de números inteiros de dimensão m x n
# e ao final mostra a quantidade de linhas e colunas que tem apenas zeros (linhasnulas e colunas nulas).

def criar_matriz(linhas,colunas):
    mat=[]
    for i in range(linhas):
        mat.append([])
        for j in range(colunas):
            numero=int(input(f"Informe o valor para posição {[i]} {[j]}: "))
            mat[i].append(numero)
    return mat

def qtd_null(linhas,colunas,mat):
    qtd_linhas_nulas=0
    for i in range(linhas):
        qtd_zeros=0
        for j in range(colunas):
            if mat[i][j]==0:
                qtd_zeros+=1
        if qtd_zeros == colunas:
            qtd_linhas_nulas+=1
    return qtd_linhas_nulas

def gerar_matriz_transposta(linhas,colunas,mat):
    mat_transposta = []
    for i in range(linhas):
        mat_transposta.append([])
        for j in range(colunas):
            mat_transposta[i].append(mat[j][i])
    return mat_transposta



            


def imprimir_matriz(linhas,colunas,mat):
    for i in range(linhas):
        for j in range(colunas):
            print(f"{mat[i][j]}",end=" ")
        print()


def main():
    m=int(input("Informe quantidade de linhas: "))
    n=int(input("Informe quantidade de colunas: "))

    matriz = criar_matriz(m,n)

    linhas_nulas=qtd_null(m,n,matriz)
    matriz_transposta=gerar_matriz_transposta(n,m,matriz)
    colunas_nulas=qtd_null(n,m,matriz_transposta)

    print("A matriz: ")
    imprimir_matriz(m,n,matriz)
    print(f"Quantidade de linhas nulas: {linhas_nulas}")
    print(f"Quantidade de colunas nulas: {colunas_nulas}")

   

        


main()