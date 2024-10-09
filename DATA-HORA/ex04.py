#Manipulação de Dadtas e horas

import datetime

d = datetime.datetime(2024,10,9, 13, 22, 40)
print(d)

#adicionando uma semana 7 dias
d = d + datetime.timedelta(weeks=1)
print(d) #2024-10-16 13:22:40

