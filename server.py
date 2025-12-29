import socket
import json  # Importe o módulo json para serialização
from routes_json import name_routes, routes

# Definindo o endereço e a porta do servidor
host = '127.0.0.1'
port = 8080

# Criando o socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Servidor HTTP rodando em http://{host}:{port}")

while True:
    # Aceitando uma conexão
    client_socket, client_address = server_socket.accept()
    print(f"Conexão de {client_address}")

    # Recebendo a requisição HTTP
    request = client_socket.recv(1024).decode('utf-8')
    print("Requisição recebida:")
    print(request)

    def verificar_request():
        response_route = ""
        request_return = request.split('\r\n')[0]
        
        if request_return in name_routes():
            response_route = routes()[request_return],200
        else:
            response_route = "Página não encontrada",404

        return response_route

    cod_request = verificar_request()[1]

    # Serializa o objeto para JSON
    json_response = json.dumps(verificar_request()[0])

    # Cabeçalhos HTTP necessários
    response_headers = (
        f"HTTP/1.1 {cod_request} OK\r\n"
        "Content-Type: application/json; charset=UTF-8\r\n"
        "Access-Control-Allow-Origin: *\r\n"  # Permite qualquer origem
        f"Content-Length: {len(json_response)}\r\n"
        "\r\n"
    )

    # Junta cabeçalhos + corpo da resposta
    response = response_headers+json_response

    # Envia a resposta
    client_socket.sendall(response.encode('utf-8'))

    # Fecha a conexão
    client_socket.close()