def calcular_preco_final():
  """
  Esta função solicita ao usuário o preço original de um produto e um percentual de desconto,
  calcula e exibe o preço final com duas casas decimais.
  """
  try:
    preco_original = float(input("Digite o preço original do produto (exemplo: 250.75): R$ "))
    percentual_desconto = float(input("Digite o percentual de desconto (exemplo: 10): "))

    if preco_original < 0 or percentual_desconto < 0:
        print("Erro: O preço e o percentual de desconto não podem ser negativos.")
        return

    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto

    print("\n--- Resultado ---")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Percentual de Desconto: {percentual_desconto:.2f}%")
    print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
    print(f"Preço Final com Desconto: R$ {preco_final:.2f}")

  except ValueError:
    print("\nErro: Por favor, insira valores numéricos válidos.")

# Executa a função principal
if __name__ == "__main__":
  calcular_preco_final()