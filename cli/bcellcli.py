import socket
import re

host = "localhost"
port = 6379
RES_PATTERN =  re.compile(r"^\+(.*)[\r\n|\n]$")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    command = input(">>")
    serialized_command = b"+" + bytes(command, 'utf-8') + b"\n"
    # print(serialized_command)
    s.sendall(serialized_command)
    data = s.recv(1024)
    decoded_data = data.decode('utf-8')
    deserialized_data = RES_PATTERN.match(decoded_data).group(1)
    print(deserialized_data)
s.close()
print('Received', repr(data))