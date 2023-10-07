n = int(input("informe a quantidade de numeros que deseja digitar: "))

listaNumeros = []
Impar = []
Par = []

i = 0
while i < n :
    numero = int(input("Digite um numero: "))
    listaNumeros.append(numero)
    i+=1

for i in range(len(listaNumeros)):
    if listaNumeros[i]%2==0:
        Par.append(listaNumeros[i])
    else:
        Impar.append(listaNumeros[i])

print("Números par:")
for i in range(len(Par)):
    print(f"{Par[i]}",end=" ")
    

print("\nNúmeros impar:")
for i in range(len(Impar)):
    print(f"{Impar[i]}",end=" ")

    


