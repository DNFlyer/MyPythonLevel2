import random

# Caesar Cipher function - works
def caesar_cipher(text, key):
    My_Result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            My_Result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            My_Result += char
    return My_Result

# Enemy message generation (random preamble + message) - fixed
Code_Preambles = ["US", "UK", "FR", "RU"]
preamble = random.choice(Code_Preambles)
message = preamble + " " + "Welcome to Earth"

# Transformation functions -works
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

# Randomly choose one transformation - works
def random_transform(msg):
    transformations = [odd_even_swap, reverse_string, reverse_word_by_word, split_message]
    chosen = random.choice(transformations)
    return chosen(msg), chosen.__name__

# Enemy encoder with random transform first, then Caesar - fixed
def enemy_encoder(msg):
    transformed, transform_name = random_transform(msg)
    key = random.randint(1, 25) #Ceasar here
    encoded_final = caesar_cipher(transformed, key)
    return transformed, encoded_final, key, transform_name

# Execution - fixed
transformed, encoded_final, secret_key, transform_name = enemy_encoder(message)
print(f"Original Message: {message}")
print(f"Enemy Transformed ({transform_name}): {transformed}")
print(f"Enemy Caesar Encoded (after transform): {encoded_final}")
print(f"(Secret Caesar Key was {secret_key})")

# Cracking Code - rewritten
print("\nCracking Caesar Cipher...")

transformations = [odd_even_swap, reverse_string, reverse_word_by_word, split_message]
cracked = False

for key in range(26):
    caesar_decoded = caesar_cipher(encoded_final, -key)
    
    for transform_func in transformations:
        fully_decoded = transform_func(caesar_decoded)
        
        has_preamble = any(fully_decoded.startswith(pre) for pre in Code_Preambles)
        has_target_phrase = fully_decoded.endswith("Welcome to Earth")
        
        if has_preamble and has_target_phrase:
            print(f"Success!")
            print(f"Key found: {key}")
            print(f"Transformation detected: {transform_func.__name__}")
            print(f"Decoded Message: {fully_decoded}")
            cracked = True
            break        
            
    if cracked:
        break

#Might encounter false positices, in which case secret code doesn't print.
#Possibility is very low, but never zero.