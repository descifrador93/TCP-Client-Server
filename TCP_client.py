import socket

target_host = socket.gethostname() # You can change it
target_port = 80 # This can be changed 

# Creating a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((socket.gethostname(),target_port))

# Send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") # You can send messages in bytes

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()