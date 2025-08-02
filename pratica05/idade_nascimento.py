from datetime import date

def calcular_idade_em_dias(data_nascimento: date) -> int:
  """
  Calcula a idade exata de uma pessoa em dias.

  Esta função subtrai a data de nascimento da data atual para obter
  o número exato de dias vividos, considerando todos os anos bissextos.

  Args:
    data_nascimento: Um objeto 'date' com a data de nascimento completa.

  Returns:
    O número total de dias vividos.
  """
  hoje = date.today()
  
  if data_nascimento > hoje:
    # Esta verificação é uma segurança extra, embora o loop principal já trate disso.
    return 0
    
  diferenca = hoje - data_nascimento
  return diferenca.days

# --- Parte Interativa do Programa ---
if __name__ == "__main__":
  print("--- Calculadora de Idade em Dias ---")
  
  while True:
    try:
      # Pede ao usuário para inserir os dados
      ano_str = input("Digite o ano de nascimento (ex: 1995): ")
      mes_str = input("Digite o mês de nascimento (ex: 7): ")
      dia_str = input("Digite o dia de nascimento (ex: 15): ")

      # Converte os dados para números inteiros
      ano = int(ano_str)
      mes = int(mes_str)
      dia = int(dia_str)

      # Tenta criar um objeto de data com os dados fornecidos
      data_nasc_usuario = date(ano, mes, dia)

      # Verifica se a data de nascimento não está no futuro
      if data_nasc_usuario > date.today():
        print("\nErro: A data de nascimento não pode ser uma data futura. Tente novamente.\n")
        continue # Volta para o início do loop

      # Se tudo deu certo, sai do loop
      break

    except ValueError:
      # Este bloco é executado se o usuário digitar algo que não seja um número,
      # ou se a data for inválida (ex: dia 32 ou mês 13).
      print("\nErro: Data inválida ou valor não numérico. Por favor, insira os dados corretamente.\n")
    except Exception as e:
      # Pega qualquer outro erro inesperado
      print(f"\nOcorreu um erro inesperado: {e}. Tente novamente.\n")

  # Chama a função com a data válida e armazena o resultado
  total_dias_vividos = calcular_idade_em_dias(data_nasc_usuario)

  # Exibe o resultado final de forma clara
  print("\n--- Resultado ---")
  print(f"Desde a data {data_nasc_usuario.strftime('%d/%m/%Y')} até hoje, você viveu:")
  print(f"-> {total_dias_vividos} dias.")