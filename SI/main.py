import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_RSA_keypair(bits):
    key = RSA.generate(bits)
    return key

def encrypt_RSA(text, key):
    cipher_rsa = key.encrypt(text.encode(), None)
    return cipher_rsa

def encrypt_AES(text, key):
    cipher_aes = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(text.encode())
    return ciphertext

def main():
    text = "RSA: algoritmo dos professores do MIT: Rivest, Shamir e Adleman"
    iterations = 5

    rsa_key_sizes = [1024, 2048, 4096, 8192]
    aes_key_sizes = [128, 256]

    results = {}

    for rsa_size in rsa_key_sizes:
        rsa_times = []
        for _ in range(iterations):
            start_time = time.time()
            rsa_keypair = generate_RSA_keypair(rsa_size)
            encrypted_text = encrypt_RSA(text, rsa_keypair[0])
            rsa_times.append(time.time() - start_time)
            print(f"RSA {rsa_size} bits encryption time: {rsa_times[-1]} seconds")
        results[f"RSA_{rsa_size}_bits"] = rsa_times

    for aes_size in aes_key_sizes:
        aes_times = []
        for _ in range(iterations):
            start_time = time.time()
            aes_key = get_random_bytes(aes_size // 8)
            encrypted_text = encrypt_AES(text, aes_key)
            aes_times.append(time.time() - start_time)
            print(f"AES {aes_size} bits encryption time: {aes_times[-1]} seconds")
        results[f"AES_{aes_size}_bits"] = aes_times

    # Save results to a spreadsheet (you can use libraries like pandas to do this)
    # Also, print system configuration
    
if __name__ == "__main__":
    main()
