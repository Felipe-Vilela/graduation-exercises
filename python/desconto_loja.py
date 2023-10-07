#Uma determinada loja está fazendo promoções de vendas. Qualquer compra que um cliente fizer até R$ 100,00 receberá 5% de desconto.
#Se a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de 20%.
#Faça um programa que leia o quanto o cliente gastou e escreva o valor da conta já com os descontos.

valorGasto = float(input("Qual o valor gasto pelo cliente? "))
valorComDesconto = None

if valorGasto <= 100.0:
    valorComDesconto = valorGasto - (valorGasto * 0.05)
    print(f"Valor final da compra R$ {valorComDesconto}")
elif valorGasto > 100.0 and valorGasto < 200.0:
    valorComDesconto = valorGasto - (valorGasto * 0.10)
    print(f"Valor final da compra R$ {valorComDesconto}")
else:
    valorComDesconto = valorGasto - (valorGasto * 0.20)
    print(f"Valor final da compra R$ {valorComDesconto}")