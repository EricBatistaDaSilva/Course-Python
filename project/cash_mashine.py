class Bank_account:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.__file = "project/files/transactions.txt"
        self.__transactions = []
        self.__load_transactions()

    def check_statement(self):
        print("===== Extrato =====")

        for transactions in self.__transactions:
            print(f"{transactions[0]}, {transactions[1]}")

        print("===================")
        print(f"Saldo (=): {self.__balance}")
        print("===================")

    def __load_transactions(self):
        try:
            with open(self.__file, "r") as file:
                for line in file:
                    transaction, amount = line.strip().split(", ")
                    amount = float(amount)

                    self.__transactions.append((transaction, amount))

                    if transaction == "depositou (+)":
                        self.__balance += amount
                    elif transaction == "sacou (-)":
                        self.__balance -+ amount
        
        except:
            print("Algo deu errado na leitura do arquivo!")


    def deposit(self, amount):
        self.__balance += amount

        try:
            with open(self.__file, "a") as file:
                file.write(f"depositou (+), {amount}\n")
                self.__transactions.append(("depositou (+)", amount))
        except:
            print("Algo deu errado!")
            pass
    
        print(f"Deposito de R${amount} realizado!")

    def withdraw(self, amount):
            if amount == 0:
                return print("Valor deve ser maior que zero")
            
            if amount <= self.__balance:
                self.__balance -= amount

                try:
                    with open(self.__file, "a") as file:
                        file.write(f"sacou (-), {amount}\n")
                        self.__transactions.append(("sacou (-)", amount))
                except:
                    print("Algo deu errado!")
                    pass
            
                print(f"Saque de R${amount} realizado!")
            else:
                print("Saldo insuficiente!")

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
        account.check_statement()
    elif option == "2":
        amount = float(input("Digite o valor do depósito: "))
        account.deposit(amount)
    elif option == "3":
        amount = float(input("Digite o valor para sacar: "))
        account.withdraw(amount)
    elif option == "4":
        print("Programa encerrado\n")
        break
    else:
        print("Opção inválida!")