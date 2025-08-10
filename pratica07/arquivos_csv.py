import csv
def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Nome", "Idade", "Cidade"])
            for linha in dados:
                escritor.writerow(linha)
        print(f"Dados salvos com sucesso em {nome_arquivo}.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

dados = [
    ["Ana", 30, "Rio de Janeiro"],
    ["Pedro", 25, "São Paulo"],
    ["Maria", 28, "Salvador"],
    ["Luiz", 35, "Belo Horizonte"]
]

if _name_ == "_main_":
    nome_arquivo = input("Digite o nome do arquivo CSV: ")
    escrever_csv(nome_arquivo, dados)