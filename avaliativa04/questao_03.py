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
            conn = sockTeste.connect((ipHost, portaTest))
        except:
            print(f'PORTA {portaTest:>5} ... ERRO...')
        else:
            print(f'PORTA {portaTest:>5} ... OK')
            sockTeste.close()
