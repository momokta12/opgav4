import socket

# Serverens host og port konfiguration
serverHOST = '127.0.0.1'
serverPORT = 17829

# Opret en TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Opret forbindelse til serveren
client.connect((serverHOST, serverPORT))

while True:
    command = input("Enter command (Random, Add, Subtract) or 'exit' to quit: ")
    if command.lower() == 'exit':  # Tillader brugeren at afslutte klienten
        break

    # Send kommando til serveren
    client.sendall(command.encode())

    # Modtag og print serverens prompt
    response = client.recv(1024).decode()
    print(response)

    if response == 'Input numbers':
        numbers = input("Enter two numbers separated by space: ")
        client.sendall(numbers.encode())  # Send tal til serveren
        result = client.recv(1024).decode()  # Modtag resultatet fra serveren
        print(f"Result: {result}")

client.close()  # Luk forbindelsen til serveren
