import socket
import string
import getpass

def encrypt(plaintext):
	key = [ ['l', 'b', 'v', 'r', 'h'], ['y', 'a', 't', 'w', 'g'], ['j', 'o', 'f', 'p', 'e'], ['u', 'd', 'n', 'c', 'q'], ['k', 'x', 'm', 's', 'i'] ]
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
	#print(ciphertext)	
	return ciphertext

s = socket.socket()
port = 50000
s.connect(('127.0.0.1', port))

print("Enter username")
username = input()
udata = encrypt(username)
s.send(udata.encode())
print("Enter password")
password = getpass.getpass()
#data = "username=" + username + "&password=" + password
#print("password is   "  + password)
data = encrypt(password)
#print("data is   " + data)
s.send(data.encode())
r = s.recv(1024)
print(r.decode())
#print("Data to be sent to server after encryption is : ")
#print(data)
s.send(data.encode())
r = s.recv(1024)
print(r.decode())
