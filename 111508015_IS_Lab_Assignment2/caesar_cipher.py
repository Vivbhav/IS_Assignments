def encrypt():
	plaintext = input("Please enter the text to encrypt\t")
	try:
		key = int(input("Enter the key for Caesar Cipher\t"))
	except ValueError:
	#is_valid = key_validate(key)
	#if is_valid == 0:
		print("Entered key is not a number. Please enter a valid key and try again.\n")
		return
	key %= 26
	ciphertext = []
	for i in range (len(plaintext)):
		if ord(plaintext[i]) >= ord('A') and ord(plaintext[i]) <= ord('Z'):
			if ord(plaintext[i]) + key > ord('Z'):
				ciphertext.append(chr(ord(plaintext[i]) + key - 26))
			else:
				ciphertext.append(chr(ord(plaintext[i]) + key))
		elif ord(plaintext[i]) >= ord('a') and ord(plaintext[i]) <= ord('z'):
			if ord(plaintext[i]) + key > ord('z'):
				ciphertext.append(chr(ord(plaintext[i]) + key - 26))
			else:
				ciphertext.append(chr(ord(plaintext[i]) + key))
		else:
			ciphertext.append(plaintext[i])
	cipher = ''.join(ciphertext)
	print(cipher)

def decrypt():
	ciphertext = input("Please enter the text to decrypt\t")
	try:
		key = int(input("Enter the key for Caesar Cipher\t"))
	except ValueError:
	#is_valid = key_validate(key)
	#if is_valid == 0:
		print("Entered key is not a number. Please enter a valid key and try again.\n")
		return
	key %= 26
	plaintext = []
	print(len(ciphertext))
	for i in range (0, len(ciphertext)):
		if ord(ciphertext[i]) >= ord('A') and ord(ciphertext[i]) <= ord('Z'):
			if ord(ciphertext[i]) - key < ord('A'):
				plaintext.append(chr(ord(ciphertext[i]) - key + 26))
			else:
				plaintext.append(chr(ord(ciphertext[i]) - key))
		elif ord(ciphertext[i]) >= ord('a') and ord(ciphertext[i]) <= ord('z'):
			if ord(ciphertext[i]) - key < ord('a'):
				plaintext.append(chr(ord(ciphertext[i]) - key + 26))
			else:
				plaintext.append(chr(ord(ciphertext[i]) - key))
		else:
			plaintext.append(ciphertext[i])
	plain = ''.join(plaintext)
	print(plain)

def main():
	while(1):
		try:
			option = int(input("Please enter your option-\n1. Encrypt\n2. Decrypt\n3. Exit\t\t\t\t"))
		except ValueError:
			print("Please enter a number between 1, 2 and 3 only and try again.\n")
			continue
		if option == 1:
			encrypt()
			print("\n\n")
		elif option == 2:
			decrypt()
			print("\n\n")
		else:
			exit()

if __name__ == "__main__":
	main()
