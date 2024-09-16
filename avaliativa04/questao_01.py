import socket, sys

strHost = 'www.ifrn.edu.br'
ipHost  = socket.gethostbyname(strHost)

lstPorts = [22, 23, 25, 80, 443, 8080]

for port in lstPorts:
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        conn = sock.connect((ipHost, port))
    except:
        print(f'PORTA {port:>5} ... ERRO... {sys.exc_info()[0]}')
    else:
        print(f'PORTA {port:>5} ... OK')
        sock.close()

# a) armazena o site.
# b) Pega o ip e o nome. family=socket.AF_INET é especificar a familia de enderenço ipv4. type=socket.SOCK_STREAM é se é conexão TCP.
# c) ipHost está com site e a port vai verificar ser quais portas que combina.
# d) O variavel IstPorts são os número da porta. Então, o que aconteça vai pega o nome do host para ver quais porta combina que está conexão e a outra número vai mostra que não combina dessa porta.