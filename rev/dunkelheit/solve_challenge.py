#!/usr/bin/env python3

def fnv1_32_hash(data: bytes) -> int:
    FNV_PRIME = 16777619
    FNV_OFFSET = 2166136261
    hash_value = FNV_OFFSET
    for byte in data:
        hash_value = (hash_value * FNV_PRIME) & 0xFFFFFFFF
        hash_value ^= byte
    return hash_value

def xor_decode(encoded: list, key: int) -> str:
    return ''.join(chr(b ^ key) for b in encoded)

def verify_flag(flag: str, expected_hash: int = 0x28663c47) -> bool:
    computed_hash = fnv1_32_hash(flag.encode())
    return computed_hash == expected_hash

def solve():
    XOR_KEY = 0x77

    pieces = {
        1: [0x32, 0x3b, 0x3e, 0x23, 0x32, 0x24, 0x32, 0x34, 0x0c],
        2: [0x35, 0x1b, 0x43, 0x14, 0x1c, 0x28, 0x1a, 0x44, 0x40, 0x43, 0x1b, 0x28],
        3: [0x3e, 0x04, 0x40, 0x28, 0x3c, 0x05, 0x1e, 0x44, 0x10, 0x28],
        4: [0x43, 0x19, 0x13, 0x28, 0x21, 0x43, 0x05, 0x10, 0x28],
        5: [0x43, 0x07, 0x07, 0x05, 0x47, 0x01, 0x44],
        6: [0x04, 0x28, 0x40, 0x1f, 0x1e, 0x04, 0x28, 0x56, 0x56, 0x0a],
    }

    decoded_pieces = [xor_decode(encoded, XOR_KEY) for encoded in pieces.values()]
    flag = ''.join(decoded_pieces)

    if verify_flag(flag):
        print(flag)
        return flag
    else:
        print("Failed")
        return None

if __name__ == "__main__":
    solve()
