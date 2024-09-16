import sys, os, socket

# Arquivo de entrda:
dirInput = os.path.dirname(os.path.abspath(__file__))
strNomeArq = f'{dirInput}/portas.txt'

# Ler arquivo e montar uma lista:
lstPortas = list()
try:
    with open(strNomeArq, 'r') as arqInput:
        for strLinha in arqInput:
            lstPortas.append(strLinha[:-1].split(';'))
except:
    sys.exit(f'\nERRO: {sys.exc_info()[0]}\n')
else:
    # Solicitar URL od HOST e obter o seu respectivo IP:
    strURL = input('\Informe a URL do HOST: ')
    ipHost = socket.gethostbyname(strURL)

    # Interar a lisita de portas:
    for portaTest in lstPortas:
        sockTeste = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        try:
            conn = sockTeste.connect_ex((ipHost, portaTest))
        except:
            pass
        else:
            print(f'PORTA {portaTest[0]:>5} ... {conn}')
            sockTeste.close()


# A logica do professor Charles:
# import sys, os, socket

# # ------------------------------------------------------------
# # Arquivo de Entrada
# dirInput = os.path.dirname(os.path.abspath(__file__))
# strNomeArq = f'{dirInput}\\portas.txt' 

# # ------------------------------------------------------------
# # Ler arquivo e montar uma lista
# lstPorts = list()
# try:
#     with open(strNomeArq, 'r') as arqInput:
#         for strLinha in arqInput:
#             lstPorts.append(strLinha[:-1].split(';'))
# except:
#     sys.exit(f'\nERRO: {sys.exc_info()[0]}\n')

# # ------------------------------------------------------------
# # Solicitar URL do HOST e obter o seu respectivo IP
# strURL = input('\nInforme a URL do HOST: ')
# ipHost = socket.gethostbyname(strURL)

# # ------------------------------------------------------------
# # Iterar a lista de portas
# print('\n'+'-'*100)
# print(f'Escaneando o IP {ipHost}')
# for portTest in lstPorts:
#     try:
#         protType = socket.SOCK_STREAM if portTest[1] == 'TCP' else socket.SOCK_DGRAM 
#         sockTest = socket.socket(family=socket.AF_INET, type=protType)
#         sockTest.settimeout(3)
#         conn = sockTest.connect_ex((ipHost, int(portTest[0])))
#         status = 'Aberta' if conn == 0 else 'Fechada'
#     except KeyboardInterrupt:
#         sys.exit('AVISO: Escaneamento Interrompido (<Ctrl>+<C> Pressionado ...)')
#     except socket.gaierror:
#         sys.exit('ERRO: O HOSTNAME não pode ser resolvido...')
#     except socket.error:
#         sys.exit('ERRO: Não foi possível conectar no servidor...')
#     except:
#         print(f'Porta {portTest[0]:>5}/{portTest[1]}:{portTest[2]} ... ERRO: {sys.exc_info()[0]}')
#     else:
#         print(f'Porta {portTest[0]:>5}/{portTest[1]}:{portTest[2]} ... {status}')
#         sockTest.close()
# print('-'*100,'\n')