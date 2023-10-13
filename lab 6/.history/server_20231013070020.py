import socket

def calculate_total(data):
    numbers = list(map(int, data.split()))
    return sum(numbers)

def calculate_product(data):
    numbers = list(map(int, data.split()))
    result = 1
    for num in numbers:
        result *= num
    return result

def main():
    with open('data5.txt', 'r') as file:
        data = file.read().splitlines()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(5)

    print("Server is listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        choice = client_socket.recv(1024).decode()

        if choice == "1":
            result = calculate_total(data[1])
        elif choice == "2":
            result = calculate_product(data[1])
        else:
            result = "Invalid choice. Please select 1 for Total or 2 for Product."

        client_socket.send(str(result).encode())
        client_socket.close()

if __name__ == '__main__':
    main()
