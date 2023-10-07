# Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte a quantidade de espaços em branco e 
# aquantidade de vezes que aparecem as vogais a, e, i, o, u.

string=input("Informe uma frase: ").lower()
espaco=0
a=0
e=0
i=0
o=0
u=0

for c in range(len(string)):
    if string[c] == ' ':
        espaco+=1
    elif string[c] == 'a':
        a+=1
    elif string[c] == 'e':
        e+=1
    elif string[c] == 'i':
        i+=1
    elif string[c] == 'o':
        o+=1
    elif string[c] == 'u':
        u+=1

print(f"Quantidade de espaços ' ' : {espaco}")
print(f"Quantidade de letras 'a'  : {a} ")
print(f"Quantidade de letras 'e'  : {e} ")
print(f"Quantidade de letras 'i'  : {i} ")
print(f"Quantidade de letras 'o'  : {o} ")
print(f"Quantidade de letras 'u'  : {u} ")
