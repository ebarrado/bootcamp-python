from datetime import datetime, timedelta

tipo_carro = 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
#data_atual = today();
data_atual = datetime.now() #timezone utcnow() - 

#Calculando média para lavar carro


if tipo_carro == 'P':
    data_estimativa = data_atual + tempo_pequeno
    print(data_atual)
elif tipo_carro == 'M':
    data_estimativa = data_atual + tempo_medio
    print(data_atual)
else: 
    data_estimativa = data_atual + tempo_grande
    print(data_atual)