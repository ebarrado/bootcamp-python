opcao = -1

while opcao != 0:
    opcao = int(input("Informe uma opção: [1] Sacar\n [2] Extrato: "))
    
    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo o extrato ...")
        
else:
    print("Obrigado por usar nosso sistema bancário, ate logo ")
        
        