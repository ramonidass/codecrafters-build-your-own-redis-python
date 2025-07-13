import logging
import socket
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# REDIS port
PORT = 6379
ADDR = ("127.0.0.1", PORT)

client_socket = socket.create_connection(ADDR)


def send_command(command):
    if not command:
        logger.error("No command provided")
        return
    content = (command + "\r\n").encode("utf-8")
    client_socket.sendall(content)


if __name__ == "__main__":
    logger.info("Connecting client...")
    if len(sys.argv) < 2:
        logger.error("Please provide a command as an argument")
        sys.exit(1)
    command = sys.argv[1]
    try:
        send_command(command)
        response = client_socket.recv(1024).decode('utf-8')
        logger.info(f"Response: {response}")
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        client_socket.close()
