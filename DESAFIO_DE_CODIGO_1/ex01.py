def analise_vendas(vendas):
    # Calcule o total de vendas e a média mensal
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    #importante no desafio os inputs devem ir sem texto
    entrada = input("Digite uma lista com 12 números inteiros, cada um representando o número de vendas realizadas em um mês do ano, separados por vírgula: ")
    # Divide a entrada em elementos separados por vírgula e converte para inteiros
    vendas = list(map(int, entrada.split(',')))
    return vendas

# Solicita a entrada do usuário
vendas = obter_entrada_vendas()
# Exibe o total de vendas e a média mensal
print(analise_vendas(vendas))
