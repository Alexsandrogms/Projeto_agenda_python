# Blibiotecas:
from time import sleep
from os import system

# Dicionário:
AGENDA = {}


# Funções:

# [1] - Lista de contatos
def mostrar_contatos():
    cont = 0
    if AGENDA:
        for contato in AGENDA:
            cont += 1
            linhas (f'{cont}º Contato')
            buscar_contato (contato)
    else:
        print ('>> Agenda vazia')
    pausar ()


# [2] - Buscar contato
def buscar_contato(contato):
    try:
        print (f'Nome: \t\t{contato}')
        print (f'Telefone: \t{AGENDA[contato]["telefone"]}')
        print (f'Email: \t\t{AGENDA[contato]["email"]}')
        print (f'Endereço: \t{AGENDA[contato]["endereco"]}')
    except KeyError:
        print ('>> Erro: contato inexistente')
    except Exception as error:
        print ('Erro: algo inesperado ocorreu')


# [3] - Adicionar contato, [4] - Editar contato
def ler_detalhes_contato():
    telefone = str (input (' Telefone: '))
    email = str (input (' E-mail: '))
    endereco = str (input (' Endereço: '))
    return telefone, email, endereco


# [3] - Adicionar contato, [4] - Editar contato
def adc_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar ()
    print (f'Contato {contato} adicionado/editado com sucesso')
    pausar ()


# [5] - Excluir contato
def excluir_contato(contato):
    try:
        AGENDA.pop (contato)
        salvar ()
    except KeyError:
        print ('>> Erro: contato inexistente')
    except Exception as error:
        print ('Erro: algo inesperado ocorreu')
        print (error)
    else:
        print (f'Contato {contato} excluido com sucesso')
    pausar ()


# [6] - Exportar contatos para CSV
def exportar_contatos(nome_do_arquivo):
    try:
        with open (nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write (f'{contato};{telefone};{email};{endereco}\n')
        print ('>> Agenda exportada com sucesso')
    except Exception as error:
        print ('Erro: algo inesperado ocoreu')
        print (error)
    pausar ()


# [7] - Importa contatos CSV'
def importar_arquivo(nome_do_arquivo):
    try:
        with open (nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines ()
            for linha in linhas:
                detalhes = linha.strip ().split (';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                adc_contato (nome, telefone, email, endereco)
    except FileNotFoundError:
        print ('>> Arquivo não encontrado')
    except Exception as error:
        print ('Erro: algo inesperado ocorreu')
        print (error)
    pausar ()


# Salvar contatos
def salvar():
    exportar_contatos ('database.csv')


# Carrega contatos toda vez que inicia o programa.
def carregar_contatos():
    try:
        with open ('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines ()
            for linha in linhas:
                detalhes = linha.strip ().split (';')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print ('>> Database carregando', end='')
        loading ()
        print (f'\n>> {len (AGENDA)} Contatos carregado')
        print ('>> Processo concluido')
    except FileNotFoundError:
        print ('>> Arquivo não encontrado')
    except Exception as error:
        print ('Erro: algo inesperado ocorreu')
        print (error)
    pausar ()


# Função para formatação de linhas
def linhas(txt):
    print ('=' * 35)
    print (f'{txt:^35}')
    print ('=' * 35)


# Funcôes para pausar a aplicaçaõ e limpar.
def pausar():
    system ('pause')  # Pausar
    system ('cls')  # Limpar


def loading():
    cont = 0
    while True:
        cont += 1
        print('.', end='')
        sleep(1)
        if cont == 5:
            break


# Menu do programa principal
def menu():
    sleep (0.5)
    linhas ('MENU AGENDA')
    print ('> [1] - Lista de contatos')
    print ('> [2] - Buscar contato')
    print ('> [3] - Adicionar contato')
    print ('> [4] - Editar contato')
    print ('> [5] - Excluir contato')
    print ('> [6] - Exportar contatos para CSV')
    print ('> [7] - Importa contatos CSV')
    print ('> [0] - Fechar agenda')
    print ('-'*35)


carregar_contatos ()
# Programa principal:
while True:
    menu ()
    opc = input ('Escolha uma opção: ')
    print ()
    if opc == '1':
        mostrar_contatos ()
    elif opc == '2':
        contato = input ('Digite o nome do contato: ')
        buscar_contato (contato)
    elif opc == '3' or opc == '4':
        linhas ('Adicionar contato')
        contato = str (input (' Nome: '))
        telefone, email, endereco = ler_detalhes_contato ()
        adc_contato (contato, telefone, email, endereco)
    elif opc == '5':
        contato = input ('Digite o nome do contato: ')
        excluir_contato (contato)
    elif opc == '6':
        nome_do_arquivo = str (input ('Digite o nome do arquivo: '))
        exportar_contatos (nome_do_arquivo)
    elif opc == '7':
        nome_do_arquivo = str (input ('Digite o nome do arquivo: '))
        importar_arquivo (nome_do_arquivo)
    elif opc == '0':
        print ('>>>> Fechando programa')
        break
    else:
        print ('>>>> Opção inválida')
print ()
