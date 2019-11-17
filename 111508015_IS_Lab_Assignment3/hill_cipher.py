import math
import numpy
def createMatrix(message, cols):
	rows = len(message) // cols
	keymatrix = [[0 for i in range(cols)] for j in range(rows)]
	index = 0
	for i in range(rows):
		for j in range(cols):
			keymatrix[i][j] = ord(message[index]) - ord('a')
			keymatrix[i][j] %= 26
			index += 1
	return keymatrix

def key_validate(key):
	length = len(key)
	root = math.sqrt(length)
	intnum = int(root)
	if root - intnum == 0.0:
		return 1
	else:
		return 0

def inverse(det, n):
	for i in range(1, n):
		if (det * i) % n == 1:
			return i
	return 1

def transpose(matrix):
	rows = len(matrix)
	for i in range(rows):
		for j in range(i):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]				
	return matrix	
			
def cofact(matrix):
	return numpy.linalg.inv(matrix).T * numpy.linalg.det(matrix)		

def multmatrix(num, matrix):
	rows = len(matrix)
	for i in range(rows):
		for j in range(rows):
			matrix[i][j] *= num
	return matrix

def multmatrices(a, b):
	rows1 = len(a)
	cols1 = len(a[0])
	rows2 = len(b)
	cols2 = len(b[0])
	c = [[0 for i in range(cols2)] for j in range(rows1)]
	for i in range(rows1):
		for j in range(cols2):
			for k in range(rows2):
				c[i][j] += a[i][k] * b[k][j]
	return c

def encrypt():
	keystr = input("Enter the key for encryption.\t\t")
	keystr = keystr.lower()
	length = len(keystr)
	if key_validate(keystr) == 0:
		print("Key length does not form a perfect square. Please check and try again\n")
		return		
	cols = math.sqrt(length)
	cols = int(cols)
	keymatrix = createMatrix(keystr, cols)
	message = input("Enter the message to encrypt\t\t")
	message = message.lower()
	messagematrix = createMatrix(message, cols)
	output = multmatrices(messagematrix, keymatrix)
	rows = len(message) // cols
	for i in range(rows):
		for j in range(cols):
			output[i][j] %= 26
	opmessage = [['a' for i in range(cols)] for j in range(rows)]
	message = ""
	for i in range(rows):
		for j in range(cols):
			opmessage[i][j] = chr(ord('a') + output[i][j])
			message += opmessage[i][j]
	print("Ciphertext is   " + message)

def decrypt():
	keystr = input("Enter the key for decryption.\t\t")
	keystr = keystr.lower()
	if key_validate(keystr) == 0:
		print("Key length does not form a perfect square. Please check and try again\n")
		return		
	length = len(keystr)
	cols = math.sqrt(length)
	cols = int(cols)
	keymatrix = createMatrix(keystr, cols)
	message = input("Enter the message to decrypt\t\t")
	message = message.lower()
	messagematrix = createMatrix(message, cols)
	rows = len(message) // cols
	determinant = numpy.linalg.det(keymatrix)
	determinant = round(determinant)
	determinant %= 26
	inv = inverse(determinant, 26)
	trans = transpose(keymatrix)	
	cofactor = cofact(trans)
	finalkey = multmatrix(inv, cofactor)
	for i in range(cols):
		for j in range(cols):
			finalkey[i][j] %= 26
	plainmatrix = multmatrices(messagematrix, finalkey)
	for i in range(rows):
		for j in range(cols):
			plainmatrix[i][j] = round(plainmatrix[i][j])
			plainmatrix[i][j] = int(plainmatrix[i][j])
			plainmatrix[i][j] %= 26
	opmessage = [['a' for i in range(cols)] for j in range(rows)]
	message = ""
	for i in range(rows):
		for j in range(cols):
			opmessage[i][j] = chr(ord('a') + plainmatrix[i][j])
			message += opmessage[i][j]
	print("Plaintext is   " + message) 

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

