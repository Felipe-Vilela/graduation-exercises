stringS = input("Digite a string: ")
caractereC = input("Digite o caractere: ")

qtdCaractereC = 0

for i in range(len(stringS)):
    if stringS[i] == caractereC:
        qtdCaractereC +=1

print(f"O caractere aparece {qtdCaractereC} vezes na string {stringS}")
