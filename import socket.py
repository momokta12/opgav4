import socket
import threading
import random  # Importer nødvendig for at bruge random.randint

serverHOST = '127.0.0.1'
serverPORT = 17829

# Opret en TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket til port
server.bind((serverHOST, serverPORT))

# Lyt for indkommende forbindelser
server.listen(5) 

def handle_client(conn, addr):
    """Håndterer en enkelt klientforbindelse"""
    print(f"Connected by {addr}")

    # Modtag kommando fra klient
    command = conn.recv(1024).decode()

    # Send 'Input numbers' besked til klient baseret på kommandoen
    conn.sendall(b'Input numbers')
    numbers = conn.recv(1024).decode().split()
    tal1, tal2 = int(numbers[0]), int(numbers[1])

    # Udfør operation baseret på kommandoen
    if command == 'Random':
        result = random.randint(tal1, tal2)
    elif command == 'Add':
        result = tal1 + tal2
    elif command == 'Subtract':
        result = tal1 - tal2

    # Send resultatet tilbage til klienten
    conn.sendall(str(result).encode())

    # Luk forbindelsen til klienten
    conn.close()

# Hovedløkke for at acceptere forbindelser
while True:
    conn, addr = server.accept()  # Accepter en ny forbindelse
    thread = threading.Thread(target=handle_client, args=(conn, addr))  # Opret en ny tråd for hver klient
    thread.start()  # Start tråden
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")  # Vis antal aktive forbindelser
