import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))

    try:
        while True:
            response = client.recv(4096).decode()
            print(response, end='')

            if 'Choose an option' in response:
                option = input()
                client.send(option.encode())

                if option == '4':
                    break
            else:
                data = input()
                client.send(data.encode())
    except Exception as e:
        print(f'Error: {e}')
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
    