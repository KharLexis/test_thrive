import socket
import threading
from .models import Message


# Socket server setup
def socket_server():
    HOST = "127.0.0.1"  # Localhost
    PORT = 65432  # Arbitrary port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Socket server running on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    Message.objects.create(content=data.decode("utf-8"))
                    print(f"Message received and stored: {data.decode('utf-8')}")


# Start socket server in a separate thread
threading.Thread(target=socket_server, daemon=True).start()
