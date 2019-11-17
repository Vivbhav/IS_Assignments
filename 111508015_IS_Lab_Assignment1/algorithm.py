def encrypt():
	key = [ ['l', 'b', 'v', 'r', 'h'], ['y', 'a', 't', 'w', 'g'], ['j', 'o', 'f', 'p', 'e'], ['u', 'd', 'n', 'c', ''], ['k', 'x', 'm', 's', 'i'] ]
	plaintext = input("Enter text to encrypt.\t\t")
	ciphertext = ""
	text1 = ""
	text2 = ""
	length = len(plaintext)
	for i in range(length):
		if plaintext[i] == 'z':
			row = 1
			col = 0
		else:
			for j in range(5):
				for k in range(5):
					#print("key is   " + key[j][k] + "     plaintext is   " + plaintext[i])
					if key[j][k] == plaintext[i]:
						row = j
						col = k
						break
		if(i % 5 == 0):
			text1 += chr(ord('a') + row)
			text2 += chr(ord('a') + col)
		elif(i % 5 == 1):
			text1 += chr(ord('f') + row)
			text2 += chr(ord('f') + col)
		elif(i % 5 == 2):
			text1 += chr(ord('k') + row)
			text2 += chr(ord('k') + col)
		elif(i % 5 == 3):
			text1 += chr(ord('p') + row)
			text2 += chr(ord('p') + col)
		else:
			text1 += chr(ord('u') + row)
			text2 += chr(ord('u') + col)
	text2 = text2[::-1]
	ciphertext += text1
	ciphertext += text2
	print(ciphertext)	
#encrypt()

def decrypt():
	ciphertext = input("Enter text to decrypt\t\t")
	length = len(ciphertext)
	text1 = ciphertext[0:length // 2:1]
	text2 = ciphertext[length // 2 : length : 1]
	text2 = text2[::-1]
	plaintext = ""
	key = [ ['l', 'b', 'v', 'r', 'h'], ['y', 'a', 't', 'w', 'g'], ['j', 'o', 'f', 'p', 'e'], ['u', 'd', 'n', 'c', ''], ['k', 'x', 'm', 's', 'i'] ]
	for i in range(len(text1)):
		ch1 = text1[i]
		ch2 = text2[i]
		if i % 5 == 0:
			row = ord(text1[i]) - ord('a')
			col = ord(text2[i]) - ord('a')
		elif i % 5 == 1:
			row = ord(text1[i]) - ord('f')
			col = ord(text2[i]) - ord('f')
		elif i % 5 == 2:
			row = ord(text1[i]) - ord('k')
			col = ord(text2[i]) - ord('k')
		elif i % 5 == 3:
			row = ord(text1[i]) - ord('p')
			col = ord(text2[i]) - ord('p')
		else:
			row = ord(text1[i]) - ord('u')
			col = ord(text2[i]) - ord('u')
		plaintext += key[row][col]
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
			print("\n\n")
		elif option == 2:
			decrypt()
			print("\n\n")
		else:
			exit()

if __name__ == "__main__":
	main()

