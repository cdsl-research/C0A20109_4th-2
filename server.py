import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.183'
port = 8267

try:
    s.connect((host, port))
    cmd = 'sensor'
    s.sendall(cmd.encode())

    response = s.recv(4096).decode()
    print(response)

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    s.close()
