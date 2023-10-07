frase = input("Infome a frase: ").lower()
fraseSemEspacos = ""
fraseInversa = ""

for i in range(len(frase)):
    if frase[i] != ' ':
        fraseSemEspacos = fraseSemEspacos + frase[i]
        
for i in range(len(fraseSemEspacos)-1,-1,-1):
    fraseInversa = fraseInversa + fraseSemEspacos[i]

if fraseInversa == fraseSemEspacos:
    print("É palindromo")
else:
    print("Não é palindromo")





        
    
