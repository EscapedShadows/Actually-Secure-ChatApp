import secrets
import hashlib

def get_user_input():
    user_input = ""
    for i in range(10):
        value = input(f"Enter random letters or numbers ({i+1}/10): ")
        user_input += value
    return user_input

def generate_1024bit_key(user_input):
    key = secrets.token_bytes(128)
    
    salt = secrets.token_bytes(32)
    
    hashed_input = hashlib.sha256(user_input.encode()).digest()
    
    salted_input = hashlib.sha512(salt + hashed_input).digest()
    
    combined_key = hashlib.sha512(key + salted_input).digest()
    
    return combined_key.hex()

user_input = get_user_input()

key = generate_1024bit_key(user_input)
print(f"Your 1024-bit key: {key}")