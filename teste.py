# main.py
# Este é um exemplo de um programa Python simples que simula uma conta bancária.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} depositado. Novo saldo é {self.balance}.")

    def withdraw(self, amount):
        # TODO: Improe withdraw
        #  This is an test of todo-to-issue
        #  ? It's will work?
        #  //or not
        if amount > self.balance:
            print("Saldo insuficiente.")
        else:
            self.balance -= amount
            print(f"{amount} retirado. Novo saldo é {self.balance}.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Conta bancária do {self.owner} com saldo: {self.balance}"

# Criar uma conta bancária para John
johns_account = BankAccount("John", 1000)

# Depositar dinheiro na conta de John
johns_account.deposit(500)

# Retirar dinheiro da conta de John
johns_account.withdraw(200)

# Imprimir o saldo
print(f"O saldo da conta de John é {johns_account.get_balance()}.")

# Imprimir os detalhes da conta bancária
print(johns_account)
