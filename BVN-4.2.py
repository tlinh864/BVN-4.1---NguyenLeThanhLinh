def char_to_num(ch):
# Chuyển ký tự sang số (A=0,...,Z=25 / a=0,...,z=25).
    if ch.isupper():
        return ord(ch) - ord('A')
    elif ch.islower():
        return ord(ch) - ord('a')
    else:
        return None  # không xử lý ký tự đặc biệt

def num_to_char(n, is_upper):
# Chuyển số 0-25 về ký tự, giữ nguyên hoa/thường.
    if is_upper:
        return chr(n + ord('A'))
    else:
        return chr(n + ord('a'))

def caesar_encrypt_table(plaintext, k):
    print(f"{'Ký tự':<6} {'P':<4} {'P+k':<6} {'(P+k) mod 26':<15} {'C':<6}")
    print("-"*45)
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            P = char_to_num(ch)
            C_num = (P + k) % 26
            C = num_to_char(C_num, ch.isupper())
            print(f"{ch:<6} {P:<4} {P+k:<6} {C_num:<15} {C:<6}")
            ciphertext += C
        else:
            ciphertext += ch
    return ciphertext

def caesar_decrypt_table(ciphertext, k):
    print(f"{'Ký tự':<6} {'C':<4} {'C-k':<6} {'(C-k) mod 26':<15} {'P':<6}")
    print("-"*45)
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            C = char_to_num(ch)
            P_num = (C - k) % 26
            P = num_to_char(P_num, ch.isupper())
            print(f"{ch:<6} {C:<4} {C-k:<6} {P_num:<15} {P:<6}")
            plaintext += P
        else:
            plaintext += ch
    return plaintext

plaintext = "NguyenLeThanhLinh"
k = 10

print("\nBẢNG MÃ HÓA\n")
ciphertext = caesar_encrypt_table(plaintext, k)

print("\nPlaintext :", plaintext)
print("Ciphertext:", ciphertext)

print("\nBẢNG GIẢI MÃ\n")
decrypted = caesar_decrypt_table(ciphertext, k)

print("\nCiphertext:", ciphertext)
print("Decrypted :", decrypted)
