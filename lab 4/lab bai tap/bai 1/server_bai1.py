import socket  # Nhập thư viện socket để làm việc với mạng

def echo_server(host, port):  # Định nghĩa hàm echo_server nhận host và port là tham số

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Tạo một đối tượng socket

    
    try:  # Bắt đầu xử lý lỗi
        server_socket.bind((host, port))  # Gắn kết máy chủ với host và port
        server_socket.listen(1)  # Chỉ lắng nghe một kết nối đồng thời
        
        print(f"Server đang lắng nghe trên {host}:{port}")  # In thông báo máy chủ đang lắng nghe

        while True:  # Vòng lặp vô hạn để liên tục lắng nghe kết nối
            client_socket, client_address = server_socket.accept()  # Chấp nhận kết nối từ client
            print(f"Đã kết nối từ {client_address}")  # In thông báo kết nối thành công

            data = client_socket.recv(1024).decode("utf-8")  # Nhận và giải mã dữ liệu từ client
            print(f"Nhận từ client: {data}")  # In dữ liệu nhận được từ client

            client_socket.sendall(data.encode("utf-8"))  # Gửi lại chuỗi cho client
            
            client_socket.close()  # Đóng kết nối với client
    
    except KeyboardInterrupt:  # Xử lý lỗi khi ngừng chương trình bằng Ctrl+C
        print("Server đã ngừng hoạt động.")
    finally:  # Luôn được thực thi sau khi thực hiện try hoặc except
        server_socket.close()  # Đóng socket của máy chủ

if __name__ == "__main__":  # Kiểm tra xem chương trình có được chạy trực tiếp hay không
    host = socket.gethostname()  # Lấy tên máy chủ hiện tại
    port = 12345  # Gán giá trị cổng 12345 (sinh viên có thể chọn cổng khác)
    echo_server(host, port)  # Gọi hàm echo_server với host và port đã được định nghĩa
