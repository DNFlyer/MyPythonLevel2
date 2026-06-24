import random

#Caesar Cipher function
def caesar_cipher(text, key):
    My_Result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            My_Result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            My_Result += char
    return My_Result

# 2. Enemy message generation (random preamble + message)
Code_Preambles = ["US", "UK", "FR", "SU", "CA", "AU"]
preamble = random.choice(Code_Preambles)
message = preamble + " " + "Welcome to Earth"

# 3. Transformation functions
def odd_even_swap(msg):
    chars = list(msg)
    for i in range(0, len(chars)-1, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]
    return "".join(chars)

def reverse_string(msg):
    return msg[::-1]

def reverse_word_by_word(msg):
    return " ".join(word[::-1] for word in msg.split())

def split_message(msg):
    mid = len(msg)//2
    return msg[mid:] + msg[:mid]

# Randomly choose one transformation
def random_transform(msg):
    transformations = [odd_even_swap, reverse_string, reverse_word_by_word, split_message]
    chosen = random.choice(transformations)
    return chosen(msg), chosen.__name__

# 4. Enemy encoder with random transform first, then Caesar
def enemy_encoder(msg):
    transformed, transform_name = random_transform(msg)
    key = random.randint(1, 25)  # random Caesar key
    encoded_final = caesar_cipher(transformed, key)
    return transformed, encoded_final, key, transform_name

transformed, encoded_final, secret_key, transform_name = enemy_encoder(message)
print(f"Original Message: {message}")
print(f"Enemy Transformed ({transform_name}): {transformed}")
print(f"Enemy Caesar Encoded (after transform): {encoded_final}")
print(f"(Secret Caesar Key was {secret_key})")

# 5. Cracking Caesar Cipher with loop + break
print("\nCracking Caesar Cipher...")
for key in range(26):
    attempt = caesar_cipher(encoded_final, -key)
    if any(pre in attempt for pre in Code_Preambles):  # check against all preambles
        print(f"Key found: {key}, Decoded Message: {attempt}")
        break