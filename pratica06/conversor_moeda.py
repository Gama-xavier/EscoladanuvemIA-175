import requests
from datetime import datetime

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            return "❌ Moeda não encontrada. Verifique o código e tente novamente."

        cotacao = dados[chave]
        valor_atual = float(cotacao["bid"])
        valor_max = float(cotacao["high"])
        valor_min = float(cotacao["low"])
        atualizacao = datetime.fromtimestamp(int(cotacao["timestamp"]))

        return f"""
💱 Cotação de {moeda} para BRL:
Valor atual: R$ {valor_atual:.2f}
Valor máximo: R$ {valor_max:.2f}
Valor mínimo: R$ {valor_min:.2f}
Atualizado em: {atualizacao.strftime('%d/%m/%Y %H:%M:%S')}
"""

    except requests.exceptions.RequestException as e:
        return f"Erro ao consultar a cotação: {e}"

def main():
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()

    if not moeda.isalpha() or len(moeda) != 3:
        print("❗ Código de moeda inválido. Use códigos como USD, EUR, GBP.")
        return

    resultado = consultar_cotacao(moeda)
    print(resultado)

if __name__ == "__main__":
    main()
