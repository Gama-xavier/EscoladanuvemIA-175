import requests


# Obter um usuário aleatório da API "Random User Generator"
def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api/'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Corrigido o nome da variável
        dados = response.json()["results"][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}, Email: {email}, País: {pais}"

    except requests.exceptions.RequestException as e:
        return f"Erro ao obter usuário: {e}"

def main():
    print("Gerando um usuário aleatório...")
    usuario = obter_usuario_aleatorio()
    print(usuario)

if __name__ == "__main__":
    main()