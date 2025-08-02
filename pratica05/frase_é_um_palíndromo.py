import unicodedata

def remover_acentos(texto: str) -> str:
    """
    Remove acentos do texto, normalizando os caracteres para sua forma base.
    """
    texto_normalizado = unicodedata.normalize('NFD', texto)
    return ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')

def limpar_texto(texto: str) -> str:
    """
    Remove acentos, espaços, pontuação e converte para minúsculas.
    """
    texto = remover_acentos(texto)
    texto_limpo = ''.join(
        char.lower() for char in texto
        if char.isalnum()
    )
    return texto_limpo

def verificar_palindromo(frase: str) -> str:
    """
    Verifica se a frase é um palíndromo e retorna "Sim" ou "Não".
    """
    texto_formatado = limpar_texto(frase)
    if texto_formatado == texto_formatado[::-1]:
        return "Sim"
    else:
        return "Não"


def iniciar_verificacao():
    """
    Função principal que interage com o usuário para verificar palíndromos.
    """
    print("🔁 Verificador de Palíndromos 🔁")
    print("Digite palavras ou frases para verificar se são palíndromos.")
    print("A verificação ignora acentos, espaços e pontuação.")
    print("Digite 'sair' para encerrar.\n")

    historico = []  # Armazena frases e resultados

    while True:
        entrada = input("Digite uma palavra ou frase: ").strip()
        
        if entrada.lower() == "sair":
            break

        resultado = verificar_palindromo(entrada)
        print(f"✅ Resultado: {resultado} - \"{entrada}\"\n")
        
        historico.append((entrada, resultado))

    print("\n📋 RELATÓRIO FINAL")
    print("-" * 30)
    if historico:
        for frase, res in historico:
            print(f"{res} → \"{frase}\"")
    else:
        print("Nenhuma frase foi verificada.")

    print("\nObrigado por usar o Verificador de Palíndromos!")

# Executa o programa
iniciar_verificacao()


