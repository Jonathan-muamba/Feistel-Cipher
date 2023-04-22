import math

def feistel_encrypt(plaintext, key, rounds):
    # Divisez le texte en deux moitiés
    left, right = plaintext[:len(plaintext)//2], plaintext[len(plaintext)//2:]
    
    # Effectuez le chiffrement Feistel pour chaque tour
    for i in range(rounds):
        # Calculez la fonction de Feistel
        function_output = feistel_function(right, key[i])
        
        # XOR la sortie de la fonction de Feistel avec la moitié gauche
        new_right = xor(left, function_output)
        
        # La moitié droite devient la nouvelle moitié gauche
        left = right
        
        # La sortie de la fonction de Feistel devient la nouvelle moitié droite
        right = new_right
        
    # Concaténez les deux moitiés et retournez le texte chiffré
    ciphertext = left + right
    return ciphertext

def feistel_decrypt(ciphertext, key, rounds):
    # Divisez le texte chiffré en deux moitiés
    left, right = ciphertext[:len(ciphertext)//2], ciphertext[len(ciphertext)//2:]
    
    # Effectuez le déchiffrement Feistel pour chaque tour dans l'ordre inverse
    for i in reversed(range(rounds)):
        # Calculez la fonction de Feistel avec la clé correspondante
        function_output = feistel_function(left, key[i])
        
        # XOR la sortie de la fonction de Feistel avec la moitié droite
        new_left = xor(right, function_output)
        
        # La moitié gauche devient la nouvelle moitié droite
        right = left
        
        # La sortie de la fonction de Feistel devient la nouvelle moitié gauche
        left = new_left
        
    # Concaténez les deux moitiés et retournez le texte déchiffré
    plaintext = left + right
    return plaintext

def feistel_function(data, key):
    # Calculez la valeur de hachage MD5 de la donnée concaténée avec la clé
    md5_hash = hashlib.md5(data + key).hexdigest()
    
    # Convertissez le hachage en un entier décimal
    decimal_hash = int(md5_hash, 16)
    
    # Retournez le reste de la division par 2^32
    return decimal_hash % 2**32

def xor(a, b):
    # Convertissez les chaînes en listes d'octets
    a_bytes = bytearray(a, 'utf-8')
    b_bytes = bytearray(b, 'utf-8')
    
    # Effectuez XOR sur chaque octet correspondant
    result_bytes = bytearray()
    for i in range(min(len(a_bytes), len(b_bytes))):
        result_bytes.append(a_bytes[i] ^ b_bytes[i])
    
    # Convertissez le résultat en une chaîne hexadécimale
    result_hex = result_bytes.hex()
    
    # Convertissez la chaîne hexadécimale en une chaîne ASCII
    result_ascii = bytes.fromhex(result_hex).decode('ascii')
    
    # Retournez la chaîne ASCII résultante
    return result_ascii


Pour utiliser ce script, vous devez appeler les fonctions feistel_encrypt et feistel_decrypt avec les paramètres appropriés. Par exemple, voici comment vous pouvez chiffrer et déchiffrer un texte avec une clé de 128 bits et 16 tours :

import hashlib

plaintext = "Bonjour, comment vas-tu ?"
key = "0123456789abcdef0123456789abcdef"
rounds = 16

ciphertext = feistel_encrypt(plaintext, key, rounds)

print("Texte chiffré :", ciphertext)

decrypted_text = feistel_decrypt(ciphertext, key, rounds)
print("Texte déchiffré :", decrypted_text)