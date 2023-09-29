import socket

def echo_client(host, port):
    # Lấy tên máy chủ hiện tại và cổng
    host = socket.gethostname()
    port = 12351
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        
        message = input("Nhập chuỗi cần gửi cho server: ")
        client_socket.sendall(message.encode("utf-8"))
        
        data = client_socket.recv(1024).decode("utf-8")
        print(f"Nhận từ server: {data}")
    
    except ConnectionRefusedError:
        print("Không thể kết nối đến server. Đảm bảo server đã được khởi chạy.")
    except KeyboardInterrupt:
        print("Client đã ngừng hoạt động.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    host = socket.gethostname()
    port = 12345  # Sinh viên phải sử dụng cùng cổng với server
    echo_client(host, port)
