saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    saldo = saldo - saque
    print("Realizando saque")
    print("Novo saldo: ", saldo)
else:
    print("Saldo insuficiente!")