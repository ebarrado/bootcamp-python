conta_normal = False
conta_universitaria = False
conta_especial = False

#if aninhado

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso ")
    elif saque <= (saldo + cheque_especial):
        print("Saque realiado com uso do cheque especial ")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso ")
    else: print("Saldo insuficiente")
elif conta_especial:
    print("Conta especial selecionada")
else:
    print("Sistema não reconhece seu tipo de conta, entre em contato com o gerente")