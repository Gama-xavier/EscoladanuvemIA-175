def senha_forte(senha):
    if (len(senha) < 8 or
        not any(c.isdigit() for c in senha) or
        not any(c.isupper() for c in senha) or
        not any(c.islower() for c in senha) or
        not any(c in "!@#$%^&*()-+" for c in senha)):
        return False
    return True
#verifica se a senha é forte
while True:
    senha = input("Digite uma senha: ")
    if senha_forte(senha):
        print("Senha forte.")
        break
    else:
        print("Senha fraca. A senha deve ter pelo menos 8 caracteres, "
              "incluir letras maiúsculas e minúsculas, números e símbolos.")    
        