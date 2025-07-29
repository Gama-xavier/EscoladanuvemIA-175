nome = input()
salario_fixo = float(input())
total_vendas = float(input())

if salario_fixo >= 0 and total_vendas >= 0:
    comissao = total_vendas * 0.15
    total_receber = salario_fixo + comissao
else:
    # Se valor inválido, define total_receber como salário fixo para não travar o código
    total_receber = salario_fixo

print(f"TOTAL = R$ {total_receber:.2f}")

