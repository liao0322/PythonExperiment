import socket

s = socket.socket()

HOST = socket.gethostname()
PORT = 1234
s.connect((HOST, PORT))

while True:
    input_str = input('>>> ')
    if input_str == 'q':
        break
    s.sendall(bytes(input_str, 'utf8'))

    response = s.recv(1024)
    print('response: ', str(response, 'utf8'))

s.close()
