import hashlib

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = self.hash_senha(senha)
    
    def hash_senha(self, senha):
        return hashlib.md5(senha.encode()).hexdigest()

def cadastrar_usuario(nome, email, senha):
    novo_usuario = Usuario(nome, email, senha)
    with open('usuarios.txt', 'a') as file:
        file.write(f"{novo_usuario.nome},{novo_usuario.email},{novo_usuario.senha}\n")

def autenticar_usuario(email, senha):
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    with open('usuarios.txt', 'r') as file:
        for line in file:
            nome, email_armazenado, senha_armazenada = line.strip().split(',')
            if email == email_armazenado and senha_hash == senha_armazenada:
                return True
    return False

# Exemplo de uso
cadastrar_usuario("Joao", "joao@email.com", "1234")
print(autenticar_usuario("joao@email.com", "1234"))  # Deve retornar True
print(autenticar_usuario("joao@email.com", "4321"))  # Deve retornar False
