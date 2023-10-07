# Faça um programa que leia três notas de provas de uma turma de 50 alunos (3 notas para cada aluno). Para cada aluno, o programa deve calcular a média
# ponderada como segue: Média = (nota1*2 + nota2*4 + nota3*3 ) / 10. Além de mostrar a média de cada aluno, o programa deve mostrar uma mensagem
# "Aprovado", caso a média seja maior ou igual a 6,0, e uma mensagem
# "Reprovado", caso contrário. Ao final, o programa deve calcular e apresentar a
# média geral da turma



aluno = 1
somaSala = 0

while aluno <= 50:
    print(f"Informe as notas do aluno {aluno}")
    nota1 = float(input("Digite o valor da primeira nota: "))
    nota2 = float(input("Digite o valor da segunda nota: "))
    nota3 = float(input("Digite o valor da terceira nota: "))
    mediaAluno = (nota1 * 2 + nota2 * 4 + nota3 * 3) / 9
    if mediaAluno >= 6.0:
        print(f"Aluno {aluno}, Aprovado com {mediaAluno:.2f}")
    else: 
        print(f"Aluno {aluno}, Reprovado com {mediaAluno:.2f}")
    somaSala = somaSala + mediaAluno
    print("=================================")
    aluno +=1

mediaSala = somaSala / 50.0
print(f"Média da sala = {mediaSala:.2f}")
