# -*- coding: latin-1 -*-

import socket
import math
import threading

# Funções matemáticas disponíveis no servidor
def calcular(funcao, valor):
    if funcao == 'arccos':
        return math.acos(valor)
    elif funcao == 'arcsin':
        return math.asin(valor)
    elif funcao == 'arctg':
        return math.atan(valor)
    else:
        return "Função inválida. Escolha entre arccos, arcsin, arctg."

# Função para iniciar o servidor
def iniciar_servidor():
    # Configurações do servidor
    host = '127.0.0.1'
    porta = 12345

    # Cria um socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associa o socket à interface de rede e número da porta
    servidor_endereco = (host, porta)
    servidor_socket.bind(servidor_endereco)

    # Coloca o socket em modo de escuta
    servidor_socket.listen(1)

    print(f"Servidor aguardando conexões em {host}:{porta}...")

    while servidor_ativo.is_set():
        try:
            # Espera por uma conexão
            conexao, endereco_cliente = servidor_socket.accept()
            print(f"Conexão estabelecida com {endereco_cliente}")

            # Recebe os dados do cliente
            dados = conexao.recv(1024)
            if not dados:
                break

            # Decodifica os dados
            mensagem = dados.decode('utf-8')
            print(f"Mensagem recebida: {mensagem}")

            # Separa a função e o valor da mensagem
            funcao, valor = mensagem.split(',')
            valor = float(valor)

            # Calcula o resultado
            resultado = calcular(funcao, valor)

            # Envia a resposta de volta ao cliente
            conexao.send(str(resultado).encode('utf-8'))

            # Fecha a conexão com o cliente
            conexao.close()
        except Exception as e:
            print(f"Erro durante a comunicação com o cliente: {e}")

    # Fecha o socket do servidor
    servidor_socket.close()

# Variável para indicar se o servidor está ativo
servidor_ativo = threading.Event()
servidor_ativo.set()

# Inicia o servidor em uma thread separada
thread_servidor = threading.Thread(target=iniciar_servidor)
thread_servidor.start()

# Aguarda até que o usuário interrompa o programa
try:
    thread_servidor.join()
except KeyboardInterrupt:
    print("Servidor interrompido pelo usuário.")
    servidor_ativo.clear()
    thread_servidor.join()
    print("Servidor encerrado.")
        