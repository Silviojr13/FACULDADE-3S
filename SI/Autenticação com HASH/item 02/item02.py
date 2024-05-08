import hashlib
import itertools
import time

def quebrar_hash(hash_alvo):
    caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789'
    tamanho_max_senha = 4

    start_time = time.time()

    for tamanho in range(1, tamanho_max_senha + 1):
        for tentativa in itertools.product(caracteres, repeat=tamanho):
            senha = ''.join(tentativa)
            if hashlib.md5(senha.encode()).hexdigest() == hash_alvo:
                end_time = time.time()
                tempo_total = end_time - start_time
                return senha, tempo_total
    
    return None, None

hashes_alvo = ['81dc9bdb52d04dc20036dbd8313ed055', '098f6bcd4621d373cade4e832627b4f6', '5f4dcc3b5aa765d61d8327deb882cf99', 'e99a18c428cb38d5f260853678922e03']
for hash_alvo in hashes_alvo:
    senha_quebrada, tempo_total = quebrar_hash(hash_alvo)
    if senha_quebrada is not None:
        print(f"Hash: {hash_alvo}, Senha: {senha_quebrada}, Tempo: {tempo_total} segundos")
    else:
        print(f"Hash: {hash_alvo}, Senha não encontrada.")
