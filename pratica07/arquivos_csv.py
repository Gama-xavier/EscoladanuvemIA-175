import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Nome", "Idade", "Cidade"])
            for linha in dados:
                escritor.writerow(linha)
        print(f"✅ Dados salvos com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"❌ Erro ao escrever no arquivo: {e}")

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            cabecalho = next(leitor)  # Pula o cabeçalho
            print("\n📄 Dados lidos do arquivo CSV:")
            for linha in leitor:
                print(f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}")
    except FileNotFoundError:
        print("❌ Arquivo CSV não encontrado.")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    dados = [
        ["Ana", 30, "Rio de Janeiro"],
        ["Pedro", 25, "São Paulo"],
        ["Maria", 28, "Salvador"],
        ["Luiz", 35, "Belo Horizonte"]
    ]

    nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ").strip()
    escrever_csv(nome_arquivo, dados)
    ler_csv(nome_arquivo)
