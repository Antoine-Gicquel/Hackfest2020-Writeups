import socket
 
class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = b""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)
 
    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):

        self.socket.send(data)
    
    def close(self):

        self.socket.close()
        
        

nc = Netcat("35.242.192.203", 30769)
nc.read()
nc.write(b'\n')
print(nc.read())
nc.write(b'\n')
print(nc.read())
nc.write(b'\n')
print(nc.read())
nc.write(b'\n')

## Game starts

t = nc.read()

for i in range(205):
    t = t[len(t) - 70 :]
    if b'blue' in t[:34] or b'yellow' in t[:34]:
        nc.write(b'red')
    else:
        nc.write(b'blue')
    nc.write(b'\n')
    t = nc.read()
    print(t.decode())

nc.write(b'\n')
t = nc.read()

for i in range(210):
    t = t[len(t) - 70 :]
    if b'blue' in t[:34] or b'red' in t[:34] or b'green' in t[:34]:
       nc.write(b'yellow')
    else:
        nc.write(b'blue')
    nc.write(b'\n')
    t = nc.read()
    print(t.decode())