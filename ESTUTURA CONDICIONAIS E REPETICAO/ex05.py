opcao = int(input("Informe uma opção: [1] Sacar\n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para sacar: "))
elif opcao == 2:
    print("Exibindo extrato ")
else:
    
    SystemExit.exit("Opcão Inválida ")