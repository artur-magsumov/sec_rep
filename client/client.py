import socket

s = socket.socket()
s.connect(('127.0.0.1', 9099))
while True:
    filename = input('Input file name which you want to send for server:\n')
    try:
        with open(filename, 'rb') as fn:
            data = fn.read()
            break
    except FileNotFoundError:
        print('File not found. Try input file name again.')
s.send(data)
with open(filename, 'w') as f:
    f.write('')

while True:
    rec_data = s.recv(1024)
    if not rec_data:
        break
    with open(filename, 'a') as file:
        file.write(rec_data.decode("utf8"))
s.close()
