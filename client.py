
import socket
sock = socket . socket ()
sock . connect (( 'localhost', 1337))
while True:
    data = sock.recv (1024)
    print(data)
    if not data:
        break
sock . close ()
