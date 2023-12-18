def calculate_checksum(data, max_val):
    total = 0
    for char in data: 
        total += ord(char)
    checksum = total % (max_val + 1)
    return checksum

def gamming_hash(data, a, b, c, t0):
    t = t0
    total = 0
    for char in data:
        t = (a * t + b) % c
        total += (ord(char) ^ t)
    return total % c

def main():
    a = 23
    b = 19
    max_val = 255
    t0 = 235
    
    # a) P = '0000123456'
    data_a = '0000123456'
    checksum_a = calculate_checksum(data_a, max_val)
    gamming_hash_a = gamming_hash(data_a, a, b, max_val + 1, t0)
    
    # b) P = '6543210000'
    data_b = '6543210000'
    checksum_b = calculate_checksum(data_b, max_val)
    gamming_hash_b = gamming_hash(data_b, a, b, max_val + 1, t0)
    
    # в) P = '10000001'
    data_c = '10000001'
    checksum_c = calculate_checksum(data_c, max_val)
    gamming_hash_c = gamming_hash(data_c, a, b, max_val + 1, t0)
    
    # г) P = '11000000'
    data_d = '11000000'
    checksum_d = calculate_checksum(data_d, max_val)
    gamming_hash_d = gamming_hash(data_d, a, b, max_val + 1, t0)
    
    print(f'a) Контрольная сумма: {checksum_a}, Сумма с гаммированием:{gamming_hash_a}')
    print(f'б) Контрольная сумма: {checksum_b}, Сумма с гаммированием:{gamming_hash_b}')
    print(f'в) Контрольная сумма: {checksum_c}, Сумма с гаммированием:{gamming_hash_c}')
    print(f'г) Контрольная сумма: {checksum_d}, Сумма с гаммированием:{gamming_hash_d}')
    
if __name__ == "__main__":
    main()