import hashlib
# Implementar um mecanismo de bloqueio de contas após um número específico de tentativas de login malsucedidas.
# Por exemplo, após 3 tentativas falhas, bloquear a conta por 5 minutos.
# Isso pode ser feito adicionando uma contagem de tentativas malsucedidas de login ao arquivo de usuários e verificando se excedeu um limite antes de permitir o login.
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = self.hash_senha(senha)
    
    def hash_senha(self, senha):
        return hashlib.md5(senha.encode()).hexdigest()

class UsuarioBloqueado(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self.tentativas_falhas = 0
        self.bloqueado = False
    
    def aumentar_tentativas_falhas(self):
        self.tentativas_falhas += 1
        if self.tentativas_falhas >= 3:
            self.bloquear_conta()
    
    def resetar_tentativas_falhas(self):
        self.tentativas_falhas = 0
    
    def bloquear_conta(self):
        self.bloqueado = True

def autenticar_usuario(email, senha):
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    with open('usuarios.txt', 'r+') as file:
        linhas = file.readlines()
        file.seek(0)
        for line in linhas:
            nome, email_armazenado, senha_armazenada, tentativas_falhas, bloqueado = line.strip().split(',')
            if email == email_armazenado:
                if bloqueado == 'True':
                    print("Conta bloqueada. Aguarde alguns minutos e tente novamente.")
                    return False
                elif senha_hash == senha_armazenada:
                    usuario = UsuarioBloqueado(nome, email, senha)
                    usuario.resetar_tentativas_falhas()
                    file.write(f"{usuario.nome},{usuario.email},{usuario.senha},{usuario.tentativas_falhas},{usuario.bloqueado}\n")
                    return True
                else:
                    usuario = UsuarioBloqueado(nome, email, senha)
                    usuario.aumentar_tentativas_falhas()
                    file.write(f"{usuario.nome},{usuario.email},{usuario.senha},{usuario.tentativas_falhas},{usuario.bloqueado}\n")
                    print("Senha incorreta. Tente novamente.")
                    return False
            else:
                file.write(line)
        print("Usuário não encontrado.")
        return False

# Exemplo de uso
print(autenticar_usuario("joao@email.com", "1234"))  # Deve retornar True
print(autenticar_usuario("joao@email.com", "4321"))  # Deve retornar False
print(autenticar_usuario("joao@email.com", "4321"))  # Deve retornar False e bloquear a conta
