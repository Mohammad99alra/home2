import socket
import threading
accounts = {
    '1999': {'pin': '999', 'balance': 5000},
    '1998': {'pin': '998', 'balance': 3000},
    '1997': {'pin': '997', 'balance': 7000}
}

def handle_client(client_socket):
    try:
        # Authenticate the client
        client_socket.send(b'Enter account number: ')
        account_number = client_socket.recv(1024).decode().strip()
        client_socket.send(b'Enter PIN: ')
        pin = client_socket.recv(1024).decode().strip()

        if account_number in accounts and accounts[account_number]['pin'] == pin:
            client_socket.send(b'Authentication successful.\n')
        else:
            client_socket.send(b'Authentication failed.\n')
            client_socket.close()
            return

        while True:
            client_socket.send(b'\nOptions:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\nChoose an option: ')
            option = client_socket.recv(1024).decode().strip()

            if option == '1':
                balance = accounts[account_number]['balance']
                client_socket.send(f'Your balance is: ${balance}\n'.encode())

            elif option == '2':
                client_socket.send(b'Enter amount to deposit: ')
                amount = float(client_socket.recv(1024).decode().strip())
                accounts[account_number]['balance'] += amount
                client_socket.send(b'Deposit successful.\n')

            elif option == '3':
                client_socket.send(b'Enter amount to withdraw: ')
                amount = float(client_socket.recv(1024).decode().strip())
                if amount <= accounts[account_number]['balance']:
                    accounts[account_number]['balance'] -= amount
                    client_socket.send(b'Withdrawal successful.\n')
                else:
                    client_socket.send(b'Insufficient funds.\n')

            elif option == '4':
                final_balance = accounts[account_number]['balance']
                client_socket.send(f'Your final balance is: ${final_balance}\n'.encode())
                client_socket.close()
                break

            else:
                client_socket.send(b'Invalid option. Try again.\n')
    except Exception as e:
        print(f'Error: {e}')
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print('Server started on port 9999.')

    while True:
        client_socket, addr = server.accept()
        print(f'Accepted connection from {addr}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
    