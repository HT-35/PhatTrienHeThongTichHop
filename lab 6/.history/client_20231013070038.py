import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1235))

    print("Connected to the server.")

    while True:
        print("Menu:")
        print("1. Total")
        print("2. Product")
        choice = input("Enter your choice: ")

        if choice not in ['1', '2']:
            print("Invalid choice. Please select 1 for Total or 2 for Product.")
            continue

        try:
            client_socket.send(choice.encode())
            result = client_socket.recv(1024).decode()
            print(f"Result: {result}")
        except ConnectionAbortedError as e:
            print(f"Connection aborted: {e}")
            break

    client_socket.close()

if __name__ == '__main__':
    main()
