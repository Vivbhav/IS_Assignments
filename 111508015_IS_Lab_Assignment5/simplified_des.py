import string
import sys

rounds = 2
alphabet = string.ascii_uppercase
def bin_to_ascii_4bit(bin_string):
    h1, h2 = split_half(bin_string)
    return alphabet[bin_to_int(h1)] + alphabet[bin_to_int(h2)]

def P10(data):
    box = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    return "".join(list(map(lambda x: data[x - 1], box)))

def P8(data):
    box = [6, 3, 7, 4, 8, 5, 10, 9]
    return "".join(list(map(lambda x: data[x - 1], box)))

def P4(data):
    box = [2, 4, 3, 1]
    return "".join(list(map(lambda x: data[x - 1], box)))

def S0(data):
    row = bin_to_int(data[0] + data[3])
    col = bin_to_int(data[1] + data[2])
    box = [ ["01", "00" ,"11", "10"],
            ["11", "10", "01", "00"],
            ["00", "10", "01", "11"],
            ["11", "01", "11", "10"]
            ]

    return box[row][col]

def S1(data):
    row = bin_to_int(data[0] + data[3])
    col = bin_to_int(data[1] + data[2])
    box = [ ["00", "01", "10", "11"],
            ["10", "00", "01", "11"],
            ["11", "00", "01", "00"],
            ["10", "01", "00", "11"]
            ]
            
    return box[row][col]

def IP(data):
    box = [2, 6, 3, 1, 4, 8, 5, 7]
    return "".join(list(map(lambda x: data[x - 1], box)))

def IP_1(data):
    box = [4, 1, 3, 5, 7, 2, 8, 6]
    return "".join(list(map(lambda x: data[x - 1], box)))

def E_P(data):
    box = [4, 1, 2, 3, 2, 3, 4, 1]
    return "".join(list(map(lambda x: data[x - 1], box)))

def XOR(data, key):
    return "".join(list(map(lambda x, y: str(int(x) ^ int(y)), data, key)))

def LS(data, amount):
    return data[amount:] + data[:amount]

def SW(data):
    data1, data2 = split_half(data)
    return data2 + data1

def split_half(data):
    return data[:int(len(data) / 2)], data[int(len(data) / 2):]

def int_to_bin(data):
    return "{0:b}".format(data)

def bin_to_int(data):
    return int(data, 2)

def generate_round_keys(key, rounds):
    round_keys = []
    k_h1, k_h2 = split_half(P10(key))
    s = 0
    for i in range(1, rounds + 1):
        s += i
        h1, h2 = LS(k_h1, s), LS(k_h2, s)
        round_keys.append(P8(h1 + h2))
    return round_keys

def encrypt(data, key):
    round_keys = generate_round_keys(key, rounds)
    ip1, ip2 = split_half(IP(data))

    for i, r_key in enumerate(round_keys):
        data = E_P(ip2)
        data = XOR(data, r_key)
        d1, d2 = split_half(data)
        d1 = S0(d1)
        d2 = S1(d2)
        data = XOR(ip1, P4(d1 + d2)) + ip2

        if i != len(round_keys) - 1:
            ip1, ip2 = split_half(SW(data))
        else:
            ciphertext = IP_1(data)

    return ciphertext

def decrypt(data, key):
    round_keys = list(reversed(generate_round_keys(key, rounds)))
    ip1, ip2 = split_half(IP(data))

    for i, r_key in enumerate(round_keys):
        data = E_P(ip2)
        data = XOR(data, r_key)
        d1, d2 = split_half(data)
        d1 = S0(d1)
        d2 = S1(d2)
        data = XOR(ip1, P4(d1 + d2)) + ip2
        if i != len(round_keys) - 1:
            ip1, ip2 = split_half(SW(data))
        else:
            plaintext = IP_1(data)
    return plaintext

def main():
	while(1):
		option = int(input("Choose an option\t1. Encrypt\t2. Decrypt\t3. Exit\n"))
		if option == 1:
			plaintext = input("Enter 8 bit plaintext input\t")
			key = input("Enter a 10 bit key\t")
			ciphertext = encrypt(plaintext, key)
			print("Ciphertext generated from the key is\t".format(ciphertext))
		elif option == 2:
			ciphertext = input("Enter 8 bit ciphertext input\t")
			key = input("Enter a 10 bit key\t")
			print("Plaintext post decryption of ciphertext is\t".format(decrypt(ciphertext, key)))
		else:
			exit()

if __name__ == "__main__":
	main()
