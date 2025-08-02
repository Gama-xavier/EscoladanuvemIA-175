import requests
import random
import string

# Gera uma senha aleatória segura
def gerar_senha(tamanho):
    if tamanho < 4:
        return "A senha deve ter pelo menos 4 caracteres."

    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    especiais = string.punctuation

    todos = letras_maiusculas + letras_minusculas + numeros + especiais

    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(especiais)
    ]

    senha += random.choices(todos, k=tamanho - 4)
    random.shuffle(senha)

    return ''.join(senha)

# Consulta a API Random User
def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]

        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        
        return nome, email, pais

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None, None, None

# Função principal
def main():
    try:
        tamanho = int(input("Informe o tamanho da senha que deseja gerar: "))
        nome, email, pais = obter_usuario_aleatorio()

        if nome:
            senha = gerar_senha(tamanho)
            print("\nUsuário gerado aleatoriamente:")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"País: {pais}")
            print(f"Senha gerada: {senha}")
        else:
            print("Não foi possível gerar o usuário.")

    except ValueError:
        print("Por favor, insira um número inteiro válido para o tamanho da senha.")

if __name__ == "__main__":
    main()

