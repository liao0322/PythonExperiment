import socket

s = socket.socket()

HOST = socket.gethostname()
PORT = 1234
s.connect((HOST, PORT))

while True:
    input_str = input('>>> ')
    s.sendall(bytes(input_str, 'utf8'))
    if input_str == 'q':
        break
    response = s.recv(1024)
    print('response: ', response)

s.close()
