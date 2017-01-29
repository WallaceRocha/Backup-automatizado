#Deve editar as linhas que possuem caminhos do sistema operacional
#Must be changed lines which have patch locate of S.O 
import os
import paramiko
import data
import time
import smtplib
# MAX_REQUEST_SIZE

#nome/ip/senha#
#['nome','ip','senha\n']

nome = []
ip = []
senha = []
falha = [] #contador de maquinas que falharam.

#inicio da função de 'banco de dados'.
def Banco():
    arquivo = open('log','r') #abre o arquivo de banco
    for i in arquivo.readlines():#Lê as linhas do arquivo de banco e atribui a variável 'i'
        nome.append(i.split('/')[0])#atribui os nomes do banco para a variável nome.

#as proximas linhas da função fazem o mesmo, só que para ip e senha.
    arquivo = open('log','r')
    for i in arquivo.readlines():
        ip.append(i.split('/')[1])

    arquivo = open('log','r')
    for i in arquivo.readlines():
        senha.append(i.split('/')[2][:-1])

#inicio da função de adicionar máquinas.
def Adicionar(nomex,ipx,senhax):
    time.sleep(3)
    os.system('clear')
    if os.system('ping %s -c 2 -w 3'%ipx) != 0: #Teste de conectividade com a máquina.
        os.system('clear')
        print('Parece que não há uma conexão estabelecida entre\n'\
              'as duas máquinas, mas recomendo que\n'\
              'tente adicioná-la novamente.\n')
    else:
#adicionando a máquina
        os.system('clear')
        arquivo = open('log','r')
        aux = arquivo.readlines()
        aux.append('%s/%s/%s\n'%(nomex,ipx,senhax))#adiciona e na ultima palavra o \n faz o pulo para a próxima linha.
        arquivo.close()
        arquivo = open('log','w')
        arquivo.writelines(aux)#Escreve a linha criada no arquivo log(de logins)
        arquivo.close()
        print('Máquina adicionada. \n')

def Remover(nomex):
    try:
        indice = nome.index(nomex)
        arquivo = open('log','r')
        aux = arquivo.readlines()
        aux.pop(indice)
        arquivo.close()
        arquivo = open('log','w')# "w" significa 'write' de escrita.
        arquivo.writelines(aux)
        arquivo.close()
        os.system('clear')
        print('O usuário foi removido com sucesso.\n')
    except:
        os.system('clear')
        print('\nNome não existe aqui.\n')


def BackupM():

    a = 1
    count = 0
    print('iniciando...')
    while a in range(len(nome)+1):

        try:
            print(nome[a-1])
            paf = ('/home/%s/backup.tar.gz'%nome[a-1])
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip[a-1],username= nome[a-1],password= senha[a-1])
            sftp = ssh.open_sftp()
            #stdin, stdout, stderr = ssh.exec_command('tar -czvf /home/%s/backup.tar.gz /home/%s/Backup'%(nome[a-1],nome[a-1]))
            sftp.get(format(paf),'/home/user208/%s%s.tar.gz'%(nome[a-1],data.data()))
            sftp.close()

            paf = ("cp /home/user208/'%s%s.tar.gz' /home/user208/Dropbox"%(nome[a-1],data.data()))
            os.system(paf)
            print('\nEnvio concluído.\n')

        except:
            count += 1
            falha.append(nome[a-1])

        a += 1
    print('O backup foi finalizado. Das %d máquinas, %d não fizeram backup.'%(len(nome), count))

    smtp = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)

    smtp.login('mail', 'password')

    de = 'who send'
    para = ['from']

    msg = """From: %s
    To: %s
    Subject: Backup

    Backup feito.""" % (de, ', '.join(para))

    smtp.sendmail(de, para, msg)

    smtp.quit()
    print('Email enviado.\n')


def Backup(nomex,ipx,senhax):

    try:
        paf = ('/home/%s/backup.tar.gz'%nomex)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ipx,username= nomex,password= senhax)
        #stdin, stdout, stderr = ssh.exec_command('tar -czvf /home/%s/backup.tar.gz /home/%s/Backup'%(nomex,nomex))
        sftp = ssh.open_sftp()
        sftp.get(format(paf),'/home/user208/%s%s.tar.gz'%(nomex,data.data()))
        sftp.close()
#------------------------Envio ao dropbox-------------------------------------
        paf = ("cp /home/user208/'%s%s.tar.gz' /home/user208/Dropbox"%(nomex,data.data()))
        os.system(paf)
        print('\nEnvio concluído.\n')

    except:
        os.system('clear')
        print('Ops! Alguns dos parametros passados podem estar errados.')
        time.sleep(2)
        os.system('clear')
