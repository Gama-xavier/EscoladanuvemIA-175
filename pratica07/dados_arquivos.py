import json
import statistics

def ler_log_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo_json:
            dados = json.load(arquivo_json)
            return dados
    except FileNotFoundError:
        print("❌ Arquivo não encontrado.")
        return None
    except json.JSONDecodeError:
        print("❌ O arquivo não está no formato JSON válido.")
        return None

def calcular_metricas(tempos):
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0
    return media, desvio

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo de log JSON: ").strip()
    dados = ler_log_json(nome_arquivo)

    if dados and "tempos_execucao" in dados:
        tempos = dados["tempos_execucao"]
        media, desvio = calcular_metricas(tempos)
        print(f"\n📊 Resultados:")
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio:.2f} segundos")
    else:
        print("⚠ O arquivo não contém a chave 'tempos_execucao'.")
