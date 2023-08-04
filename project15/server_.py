import socket 
from gmssl import sm2, sm4
import sys
import random
from ECC_functions import inverse, generate_element, create_pub_key, generate_elements 

# Establishing TCP Connection
HOST = ''
PORT = 50007
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print('Listening on port:', PORT)
connection, addr_info = server.accept()
print('Connected by', addr_info)

# Receiving P1
P1 = connection.recv(1024).decode('utf-8')

element2 = generate_element()
# Generating Public Key
key_pub = create_pub_key(element2, P1)
print("Generated Public Key is：", key_pub)
connection.sendall("OK".encode("utf-8"))

# Receiving Q1
Q1 = connection.recv(1024).decode('utf-8')
connection.sendall("OK".encode("utf-8"))

# Receiving 'e'
enc = connection.recv(1024)
connection.sendall("OK".encode("utf-8"))

# Generating r, s2, s3 and sending to other party
r, s2, s3 = generate_elements(element2, Q1, enc)

connection.sendall(hex(r)[2:].encode('utf-8'))
confirmation = connection.recv(1024)
assert confirmation.decode('utf-8') == "OK", "fail1"

connection.sendall(hex(s2)[2:].encode('utf-8'))
confirmation = connection.recv(1024)
assert confirmation.decode('utf-8') == "OK", "fail1"

connection.sendall(hex(s3)[2:].encode('utf-8'))
confirmation = connection.recv(1024)
assert confirmation.decode('utf-8') == "OK", "fail1"
