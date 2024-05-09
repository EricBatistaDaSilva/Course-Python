class Bank_account:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.__file = "project/files/transactions.txt"

    def deposit(self, amount):
        self.__balance += amount

        try:
            with open(self.__file, "a") as file:
                file.write(f"depositou (+), {amount}\n")
        except:
            print("Algo deu errado!")
            pass
    
        print(f"Deposito de R${amount} realizado!")

account = Bank_account()
waiting_menu = False # flag
while True:
    if waiting_menu == True:
        input("\nPressione Enter para continuar...")

    # print("\033[H\033[J") # terminal clear
    print("\033c", end="") # terminal clear
    waiting_menu = True

    print('''
=== Automated Teller Machine ===
    [1] Ver extrato
    [2] Depósitar
    [3] Fazer saque
    [4] Sair
================================
''')

    option = input("\bEscolha uma opção: ")
    print("")

    if option == "1":
        print("Extrato")
    elif option == "2":
        amount = float(input("Digite o valor do depósito: "))
        account.deposit(amount)
    elif option == "3":
        print("Saque")
    elif option == "4":
        print("Programa encerrado\n")
        break
    else:
        print("Opção inválida!")