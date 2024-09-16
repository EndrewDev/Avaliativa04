import socket, sys

strHost = 'www.ifrn.edu.br'
ipHost  = socket.gethostbyname(strHost)

lstPorts = [22, 23, 25, 80, 443, 8080]

for port in lstPorts:
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        conn = sock.connect_ex((ipHost, port))
    except:
        pass
    else:
        print(f'PORTA {port:>5} ... {conn}')
        sock.close()

# a) é usado tentar para fazer uma conexão com servidor remoto em um determinado endereço Ip e porta.
# b) O primeiro código executar bem rápido, mas só que a código segundo demorar para executar. E também do primiero código pega um número da porta só que combina e outro não, mas do segundo executar bem tudo.
