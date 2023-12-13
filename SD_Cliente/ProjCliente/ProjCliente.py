# -*- coding: latin-1 -*-

import socket
host = '127.0.0.1'
porta = 12345

while True:
    # Crie um socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecte o socket ao servidor
    cliente_endereco = (host, porta)
    cliente_socket.connect(cliente_endereco)

    # Solicitação de entrada do usuário para a função e o valor
    funcao = input(u"Digite a função (arccos, arcsin, arctg) ou 'sair' para encerrar: ").strip().lower()

    # Verifica se o usuário deseja sair
    if funcao == 'sair':
        break

    valor = float(input("Digite o valor: "))

    # Verifica se a função inserida é válida
    if funcao not in ['arccos', 'arcsin', 'arctg']:
        print("Função inválida. Escolha entre arccos, arcsin, arctg.")
        cliente_socket.close()
        continue

    # Monta a mensagem com a função e o valor
    mensagem = f"{funcao},{valor}"

    # Envia dados ao servidor
    cliente_socket.send(mensagem.encode('utf-8'))

    # Recebe resposta do servidor
    resposta = cliente_socket.recv(1024)
    print(f"Resposta do servidor: {resposta.decode('utf-8')}")

    # Fecha o socket do cliente
    cliente_socket.close()
