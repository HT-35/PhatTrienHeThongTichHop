import socket  # Nhập thư viện socket để làm việc với mạng

def echo_client(host, port):  # Định nghĩa hàm echo_client nhận host và port là tham số
    host = socket.gethostname()  # Lấy tên máy chủ hiện tại (đã được truyền qua tham số, gây hiểu nhầm)
    port = 12352  # Gán giá trị cổng 12352 (không được sử dụng trong hàm)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Tạo một đối tượng socket

    try:  # Bắt đầu xử lý lỗi
        client_socket.connect((host, port))  # Kết nối đến máy chủ qua host và port

        message = input("Nhập chuỗi cần gửi cho server: ")  # Nhập chuỗi từ người dùng
        client_socket.sendall(message.encode("utf-8"))  # Gửi chuỗi đến máy chủ

        data = client_socket.recv(1024).decode("utf-8")  # Nhận và giải mã dữ liệu từ máy chủ
        print(f"Nhận từ server: {data}")  # In dữ liệu nhận được từ máy chủ

    except ConnectionRefusedError:  # Xử lý lỗi khi không kết nối được đến máy chủ
        print("Không thể kết nối đến server. Đảm bảo server đã được khởi chạy.")
    except KeyboardInterrupt:  # Xử lý lỗi khi ngừng chương trình bằng Ctrl+C
        print("Client đã ngừng hoạt động.")
    finally:  # Luôn được thực thi sau khi thực hiện try hoặc except
        client_socket.close()  # Đóng kết nối với máy chủ

if __name__ == "__main__":  # Kiểm tra xem chương trình có được chạy trực tiếp hay không
    host = socket.gethostname()  # Lấy tên máy chủ hiện tại
    port = 12345  # Gán giá trị cổng 12345
    echo_client(host, port)  # Gọi hàm echo_client với host và port đã được định nghĩa
