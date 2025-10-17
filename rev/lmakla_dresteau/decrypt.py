#!/usr/bin/env python3
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def positive_modulo(a, n):
    return (a % n + n) % n

def modular_inverse(a, modulo):
    _, _, inv = extended_gcd(modulo, a)
    return positive_modulo(inv, modulo)

def decrypt_affine(encrypted_array, A, B, modulo=127):
    inv_A = modular_inverse(A, modulo)
    result = ""
    for c in encrypted_array:
        char_code = positive_modulo(inv_A * (c - B), modulo)
        result += chr(char_code)

    return result

def bruteforce_decrypt(encrypted_array, modulo=127):
    PRIME_NUMBERS = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103,
        107, 109, 113
    ]

    candidates = []
    for A in PRIME_NUMBERS:
        for B in range(127):
            try:
                decrypted = decrypt_affine(encrypted_array, A, B, modulo)
                if all(32 <= ord(c) <= 126 or c in '\n\r\t' for c in decrypted):
                    candidates.append((A, B, decrypted))
            except:
                continue

    return candidates

def interactive_mode():
    print("=" * 60)
    print("=" * 60)
    print()
    print("Enter the encrypted array")
    print("Format: comma-separated integers")
    print("Example: 115,76,73,84,69,83,69,67")
    print()
    encrypted_str = input("Encrypted array: ").strip()
    try:
        encrypted_array = [int(x.strip()) for x in encrypted_str.split(',')]
        print(f"\n[+] Parsed {len(encrypted_array)} encrypted values")
    except:
        print("[-] Error parsing encrypted array")
        return

    candidates = bruteforce_decrypt(encrypted_array)

    if not candidates:
        print("[-] No valid decryptions found")
        return

    print(f"[+] Found {len(candidates)} possible decryptions\n")
    print("-" * 60)

    for i, (A, B, decrypted) in enumerate(candidates, 1):
        print(f"#{i} A={A}, B={B}")
        print(f"    {decrypted}")
        print()

def main():
    interactive_mode()

if __name__ == "__main__":
    main()
