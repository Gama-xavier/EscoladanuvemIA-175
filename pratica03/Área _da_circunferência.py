# Definindo o valor de pi
pi = 3.14159265

# Solicitando o valor do raio ao usuário
raio = float(input("Favor insira o valor do raio: "))

# Cálculo da área da circunferência
area = pi * (raio ** 2)

# Exibindo os valores para o usuário com 4 casas decimais
print(f"A = {area:.4f} cm²")
