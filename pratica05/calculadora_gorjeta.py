def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta a ser deixada em um restaurante.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%).

    Retorna:
        float: O valor da gorjeta calculada, arredondado para 2 casas decimais.
    """
    if valor_conta < 0:
        raise ValueError("O valor da conta não pode ser negativo.")
    if porcentagem_gorjeta < 0:
        raise ValueError("A porcentagem da gorjeta não pode ser negativa.")
    
    gorjeta = (valor_conta * porcentagem_gorjeta) / 100
    return round(gorjeta, 2)


# Parte interativa com o usuário
try:
    valor_conta = float(input("Digite o valor total da conta (em R$): "))
    porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta desejada (%): "))

    valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    total_com_gorjeta = round(valor_conta + valor_gorjeta, 2)

    print(f"\n--- Resultado ---")
    print(f"Valor da conta:      R$ {valor_conta:.2f}")
    print(f"Porcentagem gorjeta: {porcentagem_gorjeta:.0f}%")
    print(f"Valor da gorjeta:    R$ {valor_gorjeta:.2f}")
    print(f"Total a pagar:       R$ {total_com_gorjeta:.2f}")

except ValueError as erro:
    print(f"\nErro: {erro}")
except Exception as erro:
    print(f"\nOcorreu um erro inesperado: {erro}")

