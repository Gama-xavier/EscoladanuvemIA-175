while True:
    # Entrada do primeiro número
    try:
        num1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    # Entrada do segundo número
    try:
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    # Escolha da operação
    operacao = input("Escolha a operação (+, -, *, /): ")
    if operacao not in ['+', '-', '*', '/']:
        print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
        continue

    # Execução da operação com tratamento de erro
    try:
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2  # Se num2 == 0, cai no except

        print(f"O resultado é: {resultado:.2f}")
        print("Operação concluída com sucesso.")
        break  # Encerra o loop após uma operação válida

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        continue  # Volta para o início do loop
