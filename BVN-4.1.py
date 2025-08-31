# Hàm mã hóa
def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Kiểm tra ký tự là chữ
            # Xác định ký tự viết hoa hay thường
            base = ord('A') if char.isupper() else ord('a')
            # Mã hóa ký tự
            encrypted_char = chr((ord(char) - base + k) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += char  # Giữ nguyên nếu không phải chữ cái
    return ciphertext

# Hàm giải mã
def caesar_decrypt(ciphertext, k):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - k) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Hàm chạy
def main():    
    # Nhập dữ liệu từ người dùng
    plaintext = input("Nhập Plaintext: ")
    k = int(input("Nhập k: "))
    
    # Mã hóa
    ciphertext = caesar_encrypt(plaintext, k)
    print("\nKết quả Mã hóa")
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)
    
    # Giải mã
    decrypted_text = caesar_decrypt(ciphertext, k)
    print("\nKiểm tra Giải mã")
    print("Decrypted :", decrypted_text)
    
    # Kiểm tra đúng/sai
    if decrypted_text == plaintext:
        print("Giải mã chính xác!")
    else:
        print("Mã hóa or giải mã lỗi")

if __name__ == "__main__":
    main()

# Chạy thử dữ liệu của mình
plaintext = "NguyenLeThanhLinh"
k = 10

# Mã hóa
ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)

# Giải mã để kiểm tra
decrypted_text = caesar_decrypt(ciphertext, k)
print("Decrypted :", decrypted_text)
