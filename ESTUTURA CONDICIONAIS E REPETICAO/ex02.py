

def sacar(valor):
    #variavel
    saldo = 500

    saldo -= valor
    if saldo >= valor:
        print("valor sacado!!!", saldo)
    
    print("Obrigado por ser nosso cliente, tenha um bom dia")        #sempre vai executar faz parte do método
        
#chamar função
sacar(100)

#sacar 100 de 500 
#saida "valor sacado!!! 400"

def depositar(valor):
    saldo = 400
    
    saldo += valor
    if saldo >= valor:
        print("valor Depositado!!!", saldo)
        
depositar(200)

#500 -100 + 200
# 400 + 200
        
        
