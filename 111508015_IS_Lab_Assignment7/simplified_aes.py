sbox = [9, 4, 10, 11, 13, 1, 8, 5, 6, 2, 0, 3, 12, 14, 15, 7]
def Convert_Num_To_Ascii_Bit(x):
	y = ""
	for i in range(len(x)):
		val = ord(x[i])
		j = 7
		ans = ""
		while j >= 0:
			w = val // (pow(2, j))
			ans += str(w)
			val = val % (pow(2, j))
			j -= 1
		y += ans
	return y
def Convert_ASCII_To_Char(x):
	y = ""
	for i in range(0, len(x), 8):
		ans = 0
		for j in range(8):
			ans += int(x[i + j]) * pow(2, 7 - j)
		if i == len(x) - 8:
			if chr(ans) != '#':
				y += chr(ans)
		else:
			y += chr(ans)
	return y

def Key_Expansion(key):
	x = [key[:4], key[4:8], key[8:12], key[12:16]]
	for i in range(4):
		x[i] = list(map(int, x[i]))
		x[i] = x[i][0] * 8 + x[i][1] * 4 + x[i][2] * 2 + x[i][3]
	keylist = [x[0], x[1], x[2], x[3]]
	for i in range(2):
		w2 = [0, 0, 0, 0]
		if i == 0:
			val = 8
		else:
			val = 3
		w2[0] = keylist[4 * i] ^ val ^ (sbox[keylist[4 * i + 3]])
		w2[1] = keylist[4 * i + 1] ^ 0 ^ (sbox[keylist[4 * i + 2]])
		w2[2] = w2[0] ^ keylist[4 * i + 2]
		w2[3] = w2[1] ^ keylist[4 * i + 3]
		keylist.append(w2[0])
		keylist.append(w2[1])
		keylist.append(w2[2])
		keylist.append(w2[3])
	return keylist
def Get_Byte_From_Bit(x):
	y = []
	i = 0
	while i < (len(x)):
		y.append(8 * x[i] + 4 * x[i + 1] + 2 * x[i + 2] + x[i + 3])
		i += 4
	return y
def Mix_Columns(y):
	w = []
	for i in range(len(y)):
		val = y[i] * 4
		if val >= 32:
			val ^= 38
		if val >= 16:
			val ^= 19
		w.append(val)
	ans = [0, 0, 0, 0]
	ans[0] = y[0] ^ w[1]
	ans[1] = y[1] ^ w[0]
	ans[2] = y[2] ^ w[3]
	ans[3] = y[3] ^ w[2]
	return ans
def Convert_Byte_To_Bit(y):
	cipher = []
	for i in range(len(y)):
		val = y[i]
		val1 = val // 8
		cipher.append(val1)
		val = val % 8
		val1 = val // 4
		cipher.append(val1)
		val = val % 4
		val1 = val // 2
		cipher.append(val1)
		val1 = val % 2
		cipher.append(val1)
	cipher = list(map(str, cipher))
	return "".join(cipher)
def mult(x, y):
	val = x * y
	if y == 2:
		if val >= 32:
			val ^= 38
		if val >= 16:
			val ^= 19
	else:
		val = x * 8
		if val >= 64:
			val ^= 76
		if val >= 32:
			val ^= 38
		if val >= 16:
			val ^= 19
		val ^= x
	return val
def Inverse_Mix_Columns(y):
	w = [0, 0, 0, 0]
	w[0] = mult(y[0], 9) ^ mult(y[1], 2)
	w[1] = mult(y[1], 9) ^ mult(y[0], 2)
	w[2] = mult(y[2], 9) ^ mult(y[3], 2)
	w[3] = mult(y[3], 9) ^ mult(y[2], 2)
	return w
def AES_Decrypt(y, keylist):
	j = 2
	for i in range(len(y)):
		y[i] ^= keylist[4 * j + i]
	j = 1
	while j >= 0:
		y[1], y[3] = y[3], y[1]
		for i in range(len(y)):
			y[i] = sbox.index(y[i])
		for i in range(len(y)):
			y[i] ^= keylist[4 * j + i]
		if j != 0:
			y = Inverse_Mix_Columns(y)
		j -= 1
	return Convert_Byte_To_Bit(y)
def AES_Encrypt(y, keylist):
	for i in range(len(y)):
		y[i] ^= keylist[i % 4]
	for i in range(1, 3):
		for j in range(len(y)):
			y[j] = sbox[y[j]]
		y[1], y[3] = y[3], y[1]
		if i != 2:
			y = Mix_Columns(y)
		for j in range(len(y)):
			y[j] = y[j] ^ keylist[4 * i + j]
	return Convert_Byte_To_Bit(y)

def main():
	while(1):
		option = int(input("Choose an option - 1. Encrypt\t2. Decrypt\t3. Exit\t\t"))
		if option == 1:
			x = input("Enter some text to encrypt\t\t")
			key = input("Enter a 2 character (16 bit) key\t\t")
			if len(key) != 2:
				print("Length of key is not 16 bits. Please enter 2 character only and try again.")
				exit(0)
			key = Convert_Num_To_Ascii_Bit(key)
			keylist = Key_Expansion(key)
			if len(x) % 2 != 0:
				x += '#'		
			x = Convert_Num_To_Ascii_Bit(x)
			x = list(map(int, x))
			i = 0
			cipher = ""
			while i < len(x) - 1:
				y = Get_Byte_From_Bit(x[i:i + 16])
				cipher += AES_Encrypt(y, keylist)
				i += 16		
			print("Bit wise encrypted cipher text is : " + str(cipher))
			#print(cipher)
			print("Cipher text in character format is  " + str(Convert_ASCII_To_Char(cipher)) + "\n\n")
		elif option == 2:
			x = list(map(int, cipher))
			i = 0
			plaintext = ""
			while i < len(x) - 1:
				y = Get_Byte_From_Bit(x[i:i + 16])
				plaintext += AES_Decrypt(y, keylist)
				i += 16
			print("Bit wise decrypted plain text is : " + str(plaintext))
			print("Plaintext in character format is  " + Convert_ASCII_To_Char(plaintext) + "\n\n")		
		else:
			exit()

if __name__ == "__main__":
	main()
