import usuarios
import time
import os
os.system('clear')
while True:
    print('1. Importar/Salvar\n'\
          '2. Adicionar uma máquina\n'\
          '3. Remover uma máquina\n'\
          '4. Listar máquinas\n'\
          '5. Backup de uma máquina\n'\
          '6. Iniciar Backup de todas as máquinas\n'\
          'Ou escreva *Sair* sem os asteriscos para fechar')

    alt = input('Alternativa:')

    if alt == '1':
        usuarios.ip = []
        usuarios.nome = []
        usuarios.senha = []
        usuarios.Banco()
        os.system('clear')
        print('Importado.\n')
        time.sleep(1)
        os.system('clear')

    elif alt == '2':
        os.system('clear')
        nomex = input('Digite o nome do usuário: ')
        ipx = input('Digite o ip da maquina remota: ')
        senhax = input('Digite a senha da maquina remota: ')

        print('\nCaso o nome esteja correto, faremos um rápido teste conectividade para garantir a integridade.'\
              'Espere um momento por favor...\n\n')
        if nomex in usuarios.nome:
            print('O nome já está na lista.\n')
        else:
            usuarios.Adicionar(nomex,ipx,senhax)


    elif alt == '3':
        nomex = input('Digite o nome do usuário que deseja remover: ')
        usuarios.Remover(nomex)

    elif alt == '4':
        os.system('clear')
        a = 1
        print('usuarios','Ip'.rjust(20),'Senhas'.rjust(20),'\n')
        while a <= len(usuarios.ip):
            print(usuarios.nome[a-1],usuarios.ip[a-1].rjust(25),usuarios.senha[a-1].rjust(20))
            print('-'*60)
            a += 1

    elif alt == '5':
        os.system('clear')
        nomex = input('Digite o nome do usuário: ')
        ipx = input('Digite o ip da maquina remota: ')
        senhax = input('Digite a senha da maquina remota: ')
        usuarios.Backup(nomex,ipx,senhax)

    elif alt == '6':                    ######Editada#####
        os.system('clear')
        print('Fazer backup a cada:\n'\
              '1. a cada minuto.\n'\
              '2. vinte e quatro horas')
        alt = input('Digite o valor: ')

        if alt == '1':
            os.system('clear')
            print('Esperando o horário...')
            while True:
                if time.ctime().split(' ')[-2].split(':')[2] == '00':
                    usuarios.BackupM()
                    print('Esperando o horário...')

        elif alt == '2':
            os.system('clear')
            horax = input('Em qual horario seria melhor? Digite no estilo "hh:mm:ss": ')
            os.system('clear')
            print('Esperando o horário: %s'%horax)
            while True:
                if time.ctime().split(' ')[-2] == horax:
                    usuarios.BackupM()
                    print('Esperando o horário: %s'%horax)

    elif alt.upper() == 'SAIR':
        break


    else:
        print('\n\nOpção errada.')
        time.sleep(1)
        os.system('clear')
