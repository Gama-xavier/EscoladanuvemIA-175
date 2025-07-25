"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

"""

# Leitura dos valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
# Cálculo da diferença
diferenca = (A * B) - (C * D)
print(f"A fórmula utilizada para a diferença é = (A * B - C * D)")
# Exibição da fórmula utilizada
print(f"Subistituindo os valores fornecidos: ({A} * {B} - {C} * {D})")
# Exibição do resultado
print(f"O resultado da DIFERENCA = {diferenca}")