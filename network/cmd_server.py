import socket

s = socket.socket()
HOST = socket.gethostname()
PORT = 1234
s.bind((HOST, PORT))
s.listen(2)

print('等待连接...')

conn, addr = s.accept()
print('已连接：', conn)


while True:
    request = conn.recv(1024)
    request = str(request, 'utf-8')
    print('request', request)

    if request == 'q':
        break
    input_str = input('>>> ')
    conn.sendall(bytes(input_str, 'utf8'))

conn.close()
