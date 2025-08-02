import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            return "❌ CEP não encontrado. Verifique e tente novamente."

        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        return f"""
📍 Resultado da consulta:
Logradouro: {logradouro}
Bairro: {bairro}
Cidade: {cidade}
Estado: {estado}
"""

    except requests.exceptions.RequestException as e:
        return f"Erro ao consultar o CEP: {e}"

def main():
    cep = input("Digite o CEP (apenas números): ").strip()

    # Valida o CEP (deve ter 8 dígitos)
    if not cep.isdigit() or len(cep) != 8:
        print("❗ CEP inválido. Deve conter exatamente 8 dígitos numéricos.")
        return

    resultado = consultar_cep(cep)
    print(resultado)

if __name__ == "__main__":
    main()
