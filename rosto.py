from vingadores.cadastro import Vingadores
import os  
import platform

class Rosto:
    @staticmethod
    def limpar_tela():
        sistema = platform.system()
        if sistema == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def titulo_app():
        Rosto.limpar_tela()
        print('''

    ██╗░░░██╗██╗███╗░░██╗░██████╗░░█████╗░██████╗░░█████╗░██████╗░███████╗░██████╗ 
    ██║░░░██║██║████╗░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
   ╚██╗░██╔╝██║██╔██╗██║██║░░██╗░███████║██║░░██║██║░░██║██████╔╝█████╗░░╚█████╗░
  ░╚████╔╝░██║██║╚████║██║░░╚██╗██╔══██║██║░░██║██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
 ░░╚██╔╝░░██║██║░╚███║╚██████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║███████╗██████╔╝
░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░ 🦸‍♂
              

              ''')

    @staticmethod
    def menu_vingadores():
        Rosto.titulo_app()
        print('''

                                Menu Principal
                            ---------------------
 _________________________________
|1. Cadastrar o Vingador          |
|2. Quem são os Vingadores?       |
|3. Convocar um Vingador          |
|4. Ativar/Desativar Tornozeleira |
|5. Aplicar Chip GPS              |
|6. Sair do APP                   |
|_________________________________|''')
        Rosto.ler_opcao_usuario()

    @staticmethod
    def ler_opcao_usuario():
        try:
            opcao = int(input('Digite sua opção: '))

            if opcao == 1:
                Rosto.cadastrar_vingador()
            elif opcao == 2:
                Rosto.titulo_app()
                Vingadores.listar_vingadores()
            elif opcao == 3:
                Rosto.convocar_vingador()
            elif opcao == 4:
                Rosto.ativar_desativar_tornozeleira()
            elif opcao == 5:
                Rosto.aplicar_chip_gps()
            elif opcao == 6:
                print('Encerrando o programa')
                exit()
            else:
                print('ERRADO, escolha entre 1, 2, 3, 4, 5 e 6')
                Rosto.voltar_ao_menu()
        except ValueError:
            print('ERRADO, escolha entre 1, 2, 3, 4, 5 e 6')
            Rosto.voltar_ao_menu()
        Rosto.voltar_ao_menu()

    
    @staticmethod
    def convocar_vingador():
        nome_ou_heroi = input('Digite o nome do herói ou nome real para convocar: ')
        vingador = Vingadores.buscar_vingador(nome_ou_heroi)  # Alteração aqui
        return vingador


    @staticmethod
    def ativar_desativar_tornozeleira():
        vingador = Rosto.convocar_vingador()  
        if vingador:
            acao = input(f'Deseja {vingador.heroi} ativar ou desativar a tornozeleira? (Digite "ativar" ou "desativar"): ').strip().lower()
        if acao == 'ativar':
            vingador.ativar_tornozeleira() 
        elif acao == 'desativar':
            vingador.desativar_tornozeleira()  
        else:
            print('Opção inválida! Por favor, digite "ativar" ou "desativar".')

    @staticmethod
    def aplicar_chip_gps():
        nome_heroi = input("Digite o nome do herói para aplicar o chip GPS: ").strip()
        vingador = Vingadores.buscar_vingador(nome_heroi) 
        if vingador:
            vingador.aplicar_chip_gps() 
        else:
            print(f"Vingador {nome_heroi} não encontrado.")

    @staticmethod
    def cadastrar_vingador():
        Rosto.titulo_app()
        print('Cadastrando o novo Herói aos dados...')
        heroi = input('Coloque o Nome do Herói: ')
        nome = input('Nome Completo pessoal: ')
        categoria = input('Coloque a sua categoria adequada: HUMANO/META-HUMANO/ALIENÍGENA/DEUS - escreva em maiúsculo, como no exemplo: ')
        if categoria not in ['HUMANO', 'META-HUMANO', 'ALIENÍGENA', 'DEUS']:
            print('Categoria inválida! Programa encerrado. Tente novamente.')
            Rosto.voltar_ao_menu()
            return 
        poderes = input('Coloque os poderes secundários do herói: ')
        poderzao = input('Coloque o poder principal do herói: ')
        fraqueza = input('Coloque a Fraqueza do herói: ')
        forca = int(input('Coloque o nível de força do herói de 0 a 1000: '))

        if 0 <= forca <= 1000:
             print(f"Sua escolha foi: {forca}")
        else:
             print("Por favor, escolha um número entre 0 e 1000.")
        
        v = Vingadores(heroi, nome, categoria, poderes, poderzao, fraqueza, forca)
        print(f"O herói {heroi} foi cadastrado com sucesso.")
        Rosto.voltar_ao_menu()

    @staticmethod
    def voltar_ao_menu():
        input('Pressione ENTER para continuar...')
        Rosto.menu_vingadores()
