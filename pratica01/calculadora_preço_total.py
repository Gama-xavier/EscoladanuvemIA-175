"""
Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 

"""
# Calculo do preço total da compra
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40  # em reais
quantidade = 3 # quantidade de produtos
preco_total = preco_unitario * quantidade
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {preco_total:.2f}")