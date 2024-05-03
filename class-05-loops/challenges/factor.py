# Crie uma função que receba um número como parâmetro e calcule seu fatorial

def factor(number):
    total = 1
    # while number > 0:
    #     total *= number
    #     number -= 1

    for v in range(number, 1, -1):
        total *= v
    
    return total

print(factor(10))