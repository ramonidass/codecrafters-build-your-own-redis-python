import socket


def main():
    print("Logs:!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, _ = server_socket.accept()
    connection.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
