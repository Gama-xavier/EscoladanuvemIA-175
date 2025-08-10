import pandas as pd


def processar_logs_treinamento(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    media_tempo = df['tempo_execucao'].mean()
    desvio_padrao_tempo = df['tempo_execucao'].std()
    print(f"Média do tempo de execução: {media_tempo} segundos")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo} segundos")

nome_arquivo = input("Digite o nome do arquivo de log: ")
processar_logs_treinamento(nome_arquivo)

