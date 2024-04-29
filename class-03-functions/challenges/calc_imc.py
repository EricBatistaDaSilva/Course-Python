# Crie uma função que receba altura e peso e retorne o IMC

def calc_imc(weight, height):
    imc = weight / (height**2)
    return round(imc, 2)

print(calc_imc(47, 1.58))

weight = float(input("Digite seu peso(km): "))
height = float(input("Digite sua altura(m): "))
imc = calc_imc(weight, height)

print(f"Seu IMC é {imc:.2f}")