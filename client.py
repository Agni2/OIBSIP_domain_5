import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nickname = input("Choose a nickname: ")

def receive():
    """Receive messages from server"""
    while True:
        try:

            message = client.recv(1024).decode('utf-8')
            
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:

            print("Disconnected from server!")
            client.close()
            break

def write():
    """Send messages to server"""
    while True:
        message = input('')
        if message.lower() == '/quit':
            client.close()
            break

        client.send(f"{nickname}: {message}".encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
