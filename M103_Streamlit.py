import streamlit as st

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += encrypted_char.upper() if is_upper else encrypted_char
        else:
            result += char
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_cipher_E(text, shift1, shift2):
    if gcd(shift1, 26) != 1:
        st.error("A must be coprime to 26.")
        return ""
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((shift1 * ((ord(char) - ord('a')) - shift2)) % 26) + ord('a'))
            result += encrypted_char.upper() if is_upper else encrypted_char
        else:
            result += char
    return result

def affine_cipher_D(text, shift1, shift2):
    if gcd(shift1, 26) != 1:
        st.error("A must be coprime to 26.")
        return ""
    shift_inv = mod_inverse(shift1, 26)
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((shift_inv * ((ord(char) - ord('a')) - shift2)) % 26) + ord('a'))
            result += decrypted_char.upper() if is_upper else decrypted_char
        else:
            result += char
    return result

def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key = key.lower()
    key_length = len(key)
    key_indices = [ord(char) - ord('a') for char in key]
    
    for i, char in enumerate(text):
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            char_index = ord(char) - offset
            key_index = key_indices[i % key_length]
            
            if mode == 'encrypt':
                new_index = (char_index + key_index) % 26
            elif mode == 'decrypt':
                new_index = (char_index - key_index) % 26
            
            result.append(chr(new_index + offset))
        else:
            result.append(char)
    
    return ''.join(result)

st.title("M103 Project: Ciphers")
st.subheader("This program serves as a playground to experiment with the three listed encryption techniques.")

cipher = st.selectbox("Select Cipher", ["Caesar", "Affine", "Vigenère"])
text = st.text_input("Enter Text")
action = st.radio("Action", ["Encrypt", "Decrypt"])

valid_a_values = [x for x in range (1,26) if gcd(x,26) == 1]

if cipher == "Caesar":
    shift = st.number_input("Enter shift (integer)", value=0, step=1)
    if st.button("Process"):
        shift = int(shift)
        result = caesar_cipher(text, shift) if action == "Encrypt" else caesar_cipher(text, -shift)
        st.write("Result:", result)

elif cipher == "Affine":
    shift1 = st.selectbox("Select A (integer)", valid_a_values)
    shift2 = st.number_input("Enter B (integer)", value=0, step=1)
    st.text("Note that A can only be a coprime of 26.")
    if st.button("Process"):
        shift1, shift2 = int(shift1), int(shift2)
        if action == "Encrypt":
            result = affine_cipher_E(text, shift1, shift2)
        else:
            result = affine_cipher_D(text, shift1, shift2)
        st.write("Result:", result)

elif cipher == "Vigenère":
    key = st.text_input("Enter key (string)")
    if st.button("Process"):
        result = vigenere_cipher(text, key, mode="encrypt" if action == "Encrypt" else "decrypt")
        st.write("Result:", result)