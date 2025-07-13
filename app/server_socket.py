import logging
import socket
import threading

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
'''without socket.create_server
PORT = 6379
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
server = socket.socket(socker.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
'''

# REDIS port
PORT = 6379
# TCP stream socket for localhost
server_socket = socket.create_server(("127.0.0.1", PORT), reuse_port=True)


def handle_client(conn, addr):

    logger.info(f'New connection {addr} connected')
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(b"+PONG\r\n")


def start_server():

    logger.info("Server is listening...")
    server_socket.listen()
    try:
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            logger.info(f'Active connections {threading.active_count() - 1}')
    except Exception as e:
        logger.error(f"Error accepting connection: {e}")


if __name__ == "__main__":
    logger.info("Server is starting...")
    start_server()
