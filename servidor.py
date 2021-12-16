import socket

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexão com o cliente...')

conx, ender = s.accept()
print('Conectado em', ender)

while True:
    data = conx.recv(1024)
    if not data:
        print('Conexão terminada')
        conx.close()
        break
    conx.sendall(data[::-1])
