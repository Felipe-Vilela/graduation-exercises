string = str(input("Digite a string: "))
letra = str(input("Digite a letra a ser removida: "))
novaString=""

for i in range(len(string)):
    if string[i] != letra:
        novaString = novaString + string[i]

print(f"String com a letra '{letra}' removida: {novaString}")