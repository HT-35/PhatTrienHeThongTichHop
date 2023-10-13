import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))

    print("Connected to the server.")

    try:
        while True:
            print("Menu:")
            print("1. Tính tổng")
            print("2. Tính tích")
            choice = input("Nhập lựa chọn của bạn: ")

            if choice not in ['1', '2']:
                print("Lựa chọn không hợp lệ. Vui lòng chọn 1 để tính tổng hoặc 2 để tính tích.")
                continue

            client_socket.send(choice.encode())
            result = client_socket.recv(1024).decode()

            if result == "exit":
                print("Kết thúc kết nối.")
                break

            print(f"Kết quả: {result}")
    except ConnectionAbortedError as e:
        print(f"Lỗi kết nối: {e}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    main()
