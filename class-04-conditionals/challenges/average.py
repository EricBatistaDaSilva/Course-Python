# Crie um programa que receba as notas dos alunos
# Faça um função que calcule sua média
# Apresente na tela SE o aluno foi aprovado (média 7)


def calc_avg(grade1, grade2):
    grades = (grade1 + grade2) / 2
    return round(grades, 2)

try:
    grade1 = float(input("Digite a primeira nota: "))
    grade2 = float(input("Digite a segunda nota: "))

    grades = calc_avg(grade1, grade2)

    if grades >= 7:
        print(f"Aprovado com {grades}")
    else:
        print(f"Reprovado com {grades}")
except ValueError:
    print("Valor inválido!")
except:
    print("erro na operação!")