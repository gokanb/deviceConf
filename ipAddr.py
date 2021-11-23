#Create a script that reads your ip address and write it to a file!. 

import socket    

print(socket.gethostbyname(socket.gethostname()))

file = open ("ip_address.txt", "w")
file.write(f'Ip address is: {(socket.gethostbyname(socket.gethostname()))}')
file.close()

