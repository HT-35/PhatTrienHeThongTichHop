# Vd 1:

import socket

# Tạo một socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lấy tên máy chủ hiện tại và cổng
host = socket.gethostname()
port = 12351

# Gắn kết socket với địa chỉ và cổng
server_socket.bind((host, port))

# Bắt đầu lắng nghe kết nối từ client, tối đa 5 kết nối đồng thời
server_socket.listen(5)
print(f"Server đang lắng nghe trên {host}:{port}")

while True:
    # Chấp nhận kết nối từ client
    client_socket, client_address = server_socket.accept()
    print(f"Đã chấp nhận kết nối từ {client_address}")

    # Gửi thông điệp cho client
    message = "Cảm ơn bạn đã kết nối."
    client_socket.sendall(message.encode("utf-8"))

    # Đóng kết nối với client
    client_socket.close()


