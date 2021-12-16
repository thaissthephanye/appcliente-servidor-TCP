import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode(input('Digite algo: ')))
data = s.recv(1024)

print('Mensagem:' , data.decode())
