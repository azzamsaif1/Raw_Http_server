import socket

HOST = '127.0.0.1'
PORT = 8080

# إنشاء الخادم
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Server Running] Visit: http://{HOST}:{PORT}")

while True:
    client_conn, client_addr = server_socket.accept()
    request = client_conn.recv(1024).decode()

    print("[Request Received]:")
    print(request)

    html = """
    <html>
        <head><title>Azzam HTTP Server</title></head>
        <body style="font-family:sans-serif;">
            <h1>Hello from Azzam's raw HTTP server!</h1>
            <p>This page was served manually using Python + socket.</p>
        </body>
    </html>
    """

    response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html)}

{html}
"""

    client_conn.sendall(response.encode())
    client_conn.close()
