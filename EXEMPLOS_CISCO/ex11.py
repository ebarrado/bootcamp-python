income = float(input("Entre com os rendimentos "))

if income < 85528:
tax = income * 0.18 - 556
# Escrever o resto do código aqui.
tax = round(tax, 0)

print(
 "A taxa é:", tax, "thalers")

