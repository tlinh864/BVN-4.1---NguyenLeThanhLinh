def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return g, x, y

def mod_inverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception("Không tồn tại nghịch đảo modular")
    return x % phi

def char_to_num(ch):
    if ch.isalpha():
        return ord(ch.upper()) - ord('A')
    return None

def num_to_char(num, orig_char):
    ch = chr(num + ord('A'))
    return ch if orig_char.isupper() else ch.lower()

# --- Thông số RSA ---
p, q, e = 17, 23, 5
n = p * q
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)

print("n =", n, "phi =", phi, "d =", d)

plaintext = "NguyenLeThanhLinh"

# Mã hóa
cipher_nums = []
for ch in plaintext:
    if ch.isalpha():
        M = char_to_num(ch)
        C = pow(M, e, n)
        cipher_nums.append(C)
    else:
        cipher_nums.append(ch)

print("\nCipher (số):", cipher_nums)

# Giải mã
decrypted = ""
for i, val in enumerate(cipher_nums):
    if isinstance(val, int):  # số đã mã hóa
        M = pow(val, d, n)
        decrypted += num_to_char(M, plaintext[i])
    else:
        decrypted += val

print("Plaintext gốc :", plaintext)
print("Sau giải mã   :", decrypted)
