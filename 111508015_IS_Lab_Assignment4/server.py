import socket
import string
def to(x, b):
	return int(x, b)

def decrypt(ciphertext):
	print(ciphertext)
	length = len(ciphertext)
	text1 = ciphertext[0:length // 2:1]
	text2 = ciphertext[length // 2 : length : 1]
	text2 = text2[::-1]
	plaintext = ""
	key = [ ['l', 'b', 'v', 'r', 'h'], ['y', 'a', 't', 'w', 'g'], ['j', 'o', 'f', 'p', 'e'], ['u', 'd', 'n', 'c', 'q'], ['k', 'x', 'm', 's', 'i'] ]
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
		#print(plaintext)
		plaintext += key[row][col]
	return plaintext

s = socket.socket()
print("Socket created")
port = 50000
s.bind(('', port))
print("Socket binded to port " + str(port))
s.listen(5)
d = {}
d['vivek'] = 'vivbhav'
d['sumedh'] = 'pendurkar'
while True:
	c, addr = s.accept()
	c.send('Connection successful!'.encode())
	text = c.recv(1024)
	print("Data received from client is : ")
	
	#print(text.decode())
	text = decrypt(text.decode())
	#print(text)
	username = text
	text = ""
	text = c.recv(1024)
	temp = text.decode()
	#print("encrypted as received is   " + temp)
	text = decrypt(temp)
	#print("text is ")
	#print(text)		
	password = text
	if username in d:
		if d[username] == password:
			c.send('Successful Login : Credentials are valid!'.encode())
			x = username + " has logged in"
			print(x)
		else:
			c.send('Login Failed : Invalid Password!'.encode())
			print("Invalid Password")
	else:
		c.send('Login Failed : Invalid Username!'.encode())
		print("Invalid Username")
s.close()
