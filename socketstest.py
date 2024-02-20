import socket

'''
ip=socket.gethostbyname('academy.tcm-sec.com')
print(ip)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("academy.tcm-sec.com", 80))
s.sendall(b"HEAD / HTTP/1.1\r\nHost:academy.tcm-sec.com\r\n\r\n" )
print(s.recv(1024).decode())
s.close()
'''
client = False
server = False
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if server:
    s.bind(("127.0.0.1"), port)
    s.listen()

    while True:
        connect, addr = s.accept()
        connect.send(b"u made it")
        connect.close()


if client:
    s.connect(("127.0.0.1", port))
    print(s.recv(1024))
    s.close()


for port in [22, 80, 445]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result=s.connect_ex(("127.0.0.1", port))
    if result ==0:
        print("{} open ".format(port))
    else:
        print("{} closed ".format(port))
    s.close()