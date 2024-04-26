# Capture dois números do usuário
# Faça as operações (+, -, *, /) e atribua variáveis semanticas
# Imprima na tela o valor das variáveis com suas operações

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))

operation = input("Qual operação deseja realizar?(+, -, *, /) ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print("O resultado é:", result)
