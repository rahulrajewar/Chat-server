import socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    serveraddress = ('192.168.0.16' , 2000)
    s1.connect(serveraddress)
    while True:
        mssg = raw_input('type mssg: ')
        s1.send(mssg.encode())
        print('waiting for reply')
        rply = s1.recv(1000)
        print('Received mssg: ', repr(rply))
    s1.close()
try:
    main()
except KeyboardInterrupt as e:
        print ("Interrupted")
        s1.close()
