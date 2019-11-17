def key_validate(key):
	key_length = len(key)
	key = key.lower()
	visited = [0] * 26
	for i in range (key_length):
		if key[i] < 'a' or key[i] > 'z':
			return 0
		if visited[ord(key[i]) - ord('a')] == 0:
			visited[ord(key[i]) - ord('a')- 1] = 1
		else:
			return 0
	return 1

def convert_key(key):
	order = [0] * len(key)
	next = 0
	for i in range(len(key)):
		min = chr(ord('z') + 1)
		minpos = -1
		for j in range(len(key)):
			if key[j] < min:
				min = key[j]
				minpos = j
		order[next] = minpos
		next += 1
		templist = list(key)
		templist[minpos] = chr(ord('z') + 2)
		key = tuple(templist)
		#print(key)
	return order

def encrypt():
	key = input("Enter the keyword\t")
	key_length = len(key)
	is_valid = key_validate(key)
	if is_valid == 0:
		print("Key has possible duplicate characters or non alphabetic characters. Please check and try again.\n")
		return
	key = tuple(key)
	order = convert_key(key)
	plaintext = input("Enter the text to encrypt\t")
	rows = len(plaintext) // key_length
	if len(plaintext) % key_length:
		rows += 1
		ch = 'a'
		diff = rows * key_length - len(plaintext)
		for i in range(diff):
			plaintext += ch
			ch = chr(ord(ch) + 1)
	plainmatrix = [[0 for x in range(key_length)] for y in range(rows)]
	index = 0
	for i in range(rows):
		for j in range(key_length):
			plainmatrix[i][j] = plaintext[index]
			index += 1
	ciphertext = ""
	for i in range(key_length):
		next = order[i]
		for j in range(rows):
			ciphertext += plainmatrix[j][next]
	print(ciphertext)

def decrypt():
	key = input("Enter the keyword\t")
	key_length = len(key)
	is_valid = key_validate(key)
	if is_valid == 0:
		print("Key has possible duplicate characters or non alphabetic characters. Please check and try again.\n")
		return
	key = tuple(key)
	order = convert_key(key)
	ciphertext = input("Enter the text to decrypt\t")
	rows = len(ciphertext) // key_length
	plainmatrix = [[0 for x in range(key_length)] for y in range(rows)]
	index = 0
	for i in range(key_length):
		next = order[i]
		for j in range(rows):
			plainmatrix[j][next] = ciphertext[index]
			index += 1
	#print(plainmatrix)
	plaintext = ""
	for i in range(rows):
		for j in range(key_length):
			plaintext += plainmatrix[i][j]
	print(plaintext)

def main():
	while(1):
		try:
			option = int(input("Please enter your option-\n1. Encrypt\n2. Decrypt\n3. Exit\t\t\t\t"))
		except ValueError:
			print("Please enter a number between 1, 2 and 3 only and try again.\n")
			continue
		if option == 1:
			encrypt()
			print("\n")
		elif option == 2:
			decrypt()
			print("\n")
		else:
			exit()

if __name__ == "__main__":
	main()
