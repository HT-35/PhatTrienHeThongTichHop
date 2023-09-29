import socket

def server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)  # Chỉ lắng nghe một kết nối đồng thời
        
        print(f"Server đang lắng nghe trên {host}:{port}")
        
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Đã kết nối từ {client_address}")
            
            data = client_socket.recv(1024).decode("utf-8")
            print(f"Nhận từ client: {data}")
            
            # Chuyển thành chữ hoa
            data = data.upper()
            
            client_socket.sendall(data.encode("utf-8"))  # Gửi lại chuỗi cho client
            
            client_socket.close()
    
    except KeyboardInterrupt:
        print("Server đã ngừng hoạt động.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    host = socket.gethostname()
    port = 12345  # Sinh viên có thể chọn cổng tuỳ ý
    server(host, port)
    