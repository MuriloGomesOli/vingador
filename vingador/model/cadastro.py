class Vingadores:
    lista_de_herois = []

    def __init__(self, heroi, nome, categoria, poderes, poderzao, fraqueza, forca):
        self.heroi = heroi
        self.nome = nome
        self.categoria = categoria
        self.poderes = poderes
        self.poderzao = poderzao
        self.fraqueza = fraqueza
        self.forca = forca
        self.tornozeleira_ativa = False  
        self.chip_gps_aplicado = False    
        Vingadores.lista_de_herois.append(self)

    def ativar_tornozeleira(self):
        if not self.tornozeleira_ativa:
            self.tornozeleira_ativa = True
            print(f'Tornozeleira ativada no herói {self.nome}.')
        else:
            print(f'A tornozeleira de {self.nome} já está ativada.')

    def desativar_tornozeleira(self):
        if self.tornozeleira_ativa:
            self.tornozeleira_ativa = False
            print(f'Tornozeleira desativada no herói {self.nome}.')
        else:
            print(f'A tornozeleira de {self.nome} já está desativada.')

    def aplicar_chip_gps(self):
        if not self.tornozeleira_ativa:
            print(f'Erro: O herói {self.nome} precisa ter a tornozeleira ativada antes de aplicar o chip GPS.')
        elif self.chip_gps_aplicado:
            print(f'O chip GPS já foi aplicado ao herói {self.nome}.')
        else:
            self.chip_gps_aplicado = True
            print(f'Chip GPS aplicado ao herói {self.nome}.')

    @classmethod
    def listar_vingadores(cls):
        if not cls.lista_de_herois:
            print("Nenhum vingador cadastrado.")
        else:
            print(f'{"Vingador".ljust(10)} | {"Nome".ljust(20)} | {"Categoria".ljust(10)} | {"Poderzao".ljust(10)} | {"Forca".ljust(5)}')
            for vingador in cls.lista_de_herois:
                print(f"{str(vingador.heroi).ljust(10)} | {str(vingador.nome).ljust(20)} | {str(vingador.categoria).ljust(10)} | {str(vingador.poderzao).ljust(10)} | {str(vingador.forca).ljust(5)}")

    @classmethod
    def buscar_vingador(cls, nome_ou_heroi):
        for vingador in cls.lista_de_herois:
            if nome_ou_heroi.lower() in [vingador.heroi.lower(), vingador.nome.lower()]:
                return vingador
        print(f"Vingador {nome_ou_heroi} não encontrado.")
        return None
