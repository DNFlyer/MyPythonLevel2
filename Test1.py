import time

# Odd-Even Swap Code -

def Swap_EvenOdd (Given_Sentence) :
    chars = list(Given_Sentence)
    for i in range (0 , len (chars) - 1 , 2) :
        chars[i] , chars[i+1] = chars[i+1] , chars[i]
    return ''.join (chars)

# Odd-Even Swap Execution -

Pre_Text = "Welcome to Earth"
Pre_Result = Swap_EvenOdd (Pre_Text)
print ("\n--- Odd-Even Swap ---")
print( "Original:" , Pre_Text)
print ("Swapped :" , Pre_Result)

time.sleep (2)


# Reverse String Code -

def String_Reverse (s) :
    return s [::-1]

# String Reversal Execution -

Pre_Text = "Welcome to Earth"
Pre_Result = String_Reverse (Pre_Text)
print ("\n--- Reverse String ---")
print ("Original:" , Pre_Text)
print ("Reversed:" , Pre_Result)

time.sleep (2)


# Reverse String Word-by-Word Code -

def Words_Reverse (sentence) :
    Words = sentence.split()
    Reversed_Words = Words[::-1]
    return ' '.join (Reversed_Words)

# Reverse String Word-by-Word Execution -

Pre_Text = "Welcome to Earth"
Pre_Result = Words_Reverse (Pre_Text)
print ("\n--- Reverse Word-by-Word ---")
print ("Original:" , Pre_Text)
print ("Word-by-word reversed:" , Pre_Result)

time.sleep (2)


# Slicing Code -

def Split_Reverse (sentence) :
    Middle = len(sentence) // 2
    First_Half = sentence[:Middle]
    Second_Half = sentence[Middle:]
    return Second_Half + First_Half

# Slicing Execution -
Pre_Text = "Welcome to Earth"
Pre_Result = Split_Reverse (Pre_Text)
print ("\n--- Swap Halves ---")
print ("Original:" , Pre_Text)
print ("Swapped halves:" , Pre_Result)

print ()

time.sleep (4)

#BONUS!!

#User Input Code -

#Pre-Defined Functions -
def My_Swap(Sentence) :
    chars = list (Sentence)
    for i in range (0 , len(chars) - 1, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]
    return ''.join(chars)

def String_Reverse (s):
    return s [::-1]

def Words_Reverse (Sentence):
    Words = Sentence.split()
    return ' '.join (Words[::-1])

def Words_Reverse_Each (Sentence):
    Words = Sentence.split()
    return ' '.join (Words[::-1] for Words in Words)

def swap_halves (Sentence):
    Middle = len(Sentence) // 2
    return Sentence[Middle:] + Sentence[:Middle]

    #(Polybius Square) -
Matrix = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I/J", "K"],
    ["L", "M", "N", "O", "P"],
    ["Q", "R", "S", "T", "U"],
    ["V", "W", "X", "Y", "Z"]
]

Encode = {}
Decode = {}

for row in range(5):
    for col in range(5):
        letter = Matrix[row][col]
        if letter == "I/J":
            Encode["I"] = str(row+1) + str(col+1)
            Encode["J"] = str(row+1) + str(col+1)
            Decode[str(row+1) + str(col+1)] = "I/J"
        else:
            Encode[letter] = str(row+1) + str(col+1)
            Decode[str(row+1) + str(col+1)] = letter

def encode_matrix(message):
    message = message.upper().replace(" ", "")
    return ' '.join(Encode[ch] for ch in message if ch in Encode)

def decode_matrix(encoded):
    codes = encoded.split()
    return ''.join(Decode[code] for code in codes)

# --- Main Program ---
print("Choose an encoding method:")
print("1. Odd-Even Swap")
print("2. Reverse String (character-by-character)")
print("3. Reverse String Word-by-Word")
print("4. Reverse Each Word (same order)")
print("5. Swap Halves")
print("6. 5x5 Matrix (Polybius Square)")

choice = input("Enter your choice (1-6): ")
message = input("Enter the message to encode: ")

print("\n--- Encoding Result ---")

if choice == "1":
    result = My_Swap(message)
    print("Odd-Even Swap:", result)

elif choice == "2":
    result = String_Reverse(message)
    print("Reversed String:", result)

elif choice == "3":
    result = Words_Reverse(message)
    print("Word-by-Word Reversed:", result)

elif choice == "4":
    result = Words_Reverse_Each(message)
    print("Each Word Reversed:", result)

elif choice == "5":
    result = swap_halves(message)
    print("Halves Swapped:", result)

elif choice == "6":
    result = encode_matrix(message)
    print("Matrix Encoded:", result)
    time.sleep(2)
    decoded = decode_matrix(result)
    print("\nDecoded back:", decoded)

else:
    print("Invalid Number Selected!")

time.sleep(2)

print("\n--- End of Program ---")