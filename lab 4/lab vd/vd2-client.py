import socket

# Tạo một socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lấy tên máy chủ hiện tại và cổng
host = socket.gethostname()
port = 12351  # Đảm bảo cổng này trùng với cổng máy chủ

try:
    # Kết nối đến máy chủ
    client_socket.connect((host, port))

    # Nhận và in thông điệp từ máy chủ
    data = client_socket.recv(1024)
    print(data.decode("utf-8"))

except ConnectionRefusedError:
    print("Không thể kết nối đến máy chủ. Đảm bảo máy chủ đã được khởi chạy và lắng nghe trên cổng đã chỉ định.")

finally:
    # Đóng kết nối
    client_socket.close()
