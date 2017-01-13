#server.py
#Modifications made 
import socket
#let's create a socket first
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def main():
    hostname = socket.gethostname() 
    '''this will assign a string to hostname variable which will contain the hostname of 
    the machine where python interpretor is currently executing.'''
    serveraddress = (hostname, 2000)
    s1.bind(serveraddress)
    print('socket created at', serveraddress)
    s1.listen(1)
    print('server listening')
    connection, address = s1.accept()
    print('connecting with: ', address)
    while True:
        data = connection.recv(1024)
        print (data)
        if not data:
            break
        reply = raw_input('Reply: ')
        connection.sendall(reply.encode())
    connection.close()
try:
    main()
except KeyboardInterrupt as e:
        print ("Interrupted")
        s1.close()
