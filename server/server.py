import socket
from mysql import *

sock = socket.socket()
sock.bind(('127.0.0.1', 9099))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    with open('received_file.csv', 'ab') as rf:
        data = conn.recv(1024)
        rf.write(data)

    csvfilename = 'received_file.csv'
    get_pattern_and_acc_num_from_database()
    open_csv(csvfilename)
    appending_values_to_acc_num()
    write_new_data_to_csv(csvfilename)

    with open('received_file.csv', 'rb') as sf:
        send_data = sf.read()
    conn.send(send_data)
    conn.close()
