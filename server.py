import socket
sock = socket.socket()
sock.bind(('',1337))
sock.listen(1)
conn, addr = sock.accept()
print ('connected:', addr)
f = open('1.txt', 'r')
while True:
    buff = f.read(1024)
    if len(buff)==0:
        break
    conn.send(buff.encode())
    
conn.close()
