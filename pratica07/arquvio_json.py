import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo_json:
            dados = json.load(arquivo_json)
            print("\n📄 Dados lidos do arquivo JSON:")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
    except FileNotFoundError:
        print("❌ Arquivo não encontrado.")
    except json.JSONDecodeError:
        print("❌ O arquivo não está no formato JSON válido.")

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
        print(f"✅ Dados salvos em '{nome_arquivo}'.")        
    except Exception as e:
        print(f"❌ Erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    # Dados da pessoa
    dados = {
        "nome": "Joice",
        "idade": 29,
        "cidade": "Curitiba"
    }

    nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ").strip()
    escrever_json(nome_arquivo, dados)
    ler_json(nome_arquivo)
