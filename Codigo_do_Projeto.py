from abc import ABC, abstractmethod
from collections import defaultdict 

class Produto:
    def __init__(self, nome, data_validade, data_entrega, valor_mercado, quant, marca=""):
        self.__nome = nome 
        self.__data_validade = data_validade
        self.__data_entrega = data_entrega
        self.__valor = valor_mercado
        self.__marca = marca 
        self.__quant = quant

    @property
    def nome(self):
        return self.__nome

    @property
    def data_entrega(self):
        return self.__data_entrega

    @staticmethod
    def cadastro_produto(lista_de_produtos): 'isso aqui vai organizar uma lista por data de validade cada produto'
        produtos_agrupados = defaultdict(list)
        
        for produto in lista_de_produtos:
            produtos_agrupados[produto.nome].append(produto)
            
        return {
            nome: sorted(lista, key=lambda p: p.data_entrega) 
            for nome, lista in produtos_agrupados.items()
        }

    def __repr__(self): "isso é pra nomear os produtos que forem intregues"
        return f"Produto(Nome: {self.__nome}, Entrega: {self.__data_entrega}, Qtd: {self.__quant})"


class Veiculo(ABC):
    def __init__(self, placa, hora_saida, produto_entregue=None):
        self.__placa = placa
        self.__produto = ""
        self.__hora_saida = hora_saida
        self.__produto_entregue = []
        self.__distancia_percorrida = 0
        self.__abastecido = False
        
        if produto_entregue:
            self.cadastro_produto_entregue(produto_entregue)
  
    @property
    def placa(self):
        return self.__placa
        
    @property
    def produto(self):
        return self.__produto
        
    @property
    def hora_saida(self):
        return self.__hora_saida
        
    @property 
    def produto_entregue(self):
        return self.__produto_entregue
        
    @property
    def distancia_percorrida(self):
        return self.__distancia_percorrida
    
    @distancia_percorrida.setter
    def distancia_percorrida(self, km):
        self.__distancia_percorrida = km

    @placa.setter
    def placa(self, p):
        self.__placa = p
        
    @produto.setter
    def produto(self, m):
        self.__produto = m

    def cadastro_produto_entregue(self, lista_bruta):
        produtos_organizados = Produto.cadastro_produto(lista_bruta)
        self.__produto_entregue = produtos_organizados
        return self.__produto_entregue
    
    @abstractmethod 
    def calcular_consumo(self):
        pass


class Carro(Veiculo):
    def __init__(self, placa, hora_saida, km_percorrido=0.0, produto_entregue=None):
        super().__init__(placa, hora_saida, produto_entregue)
        self.__km_percorrido = km_percorrido

    @property
    def km_percorrido(self):
        return self.__km_percorrido

    @km_percorrido.setter
    def km_percorrido(self, km):
        self.__km_percorrido = km

    def calcular_consumo(self):
        # Exemplo de cálculo para carro
        custo_total = (self.__km_percorrido / 10) * 5.80 # 10km por litro, R$ 5.80 o litro
        return custo_total
      
class Caminhao(Veiculo):
    def __init__(self, placa, hora_saida, eixos=2, produto_entregue=None):
        super().__init__(placa, hora_saida, produto_entregue)
        self.__eixos = eixos

    def calcular_consumo(self):
        try:
            km = float(input('Quantos quilômetros o caminhão percorreu? '))
        except ValueError:
            km = 0.0
            
        custo_medio_por_km = 1.22
        custo_total = (km * custo_medio_por_km) * 6.54
        return custo_total


class Motorista:
    def __init__(self, nome, cnh, tipo_veiculo):
        self.nome = nome
        self.cnh = cnh
        self.tipo_veiculo = tipo_veiculo

    def __repr__(self):
        return f"Motorista: {self.nome} (CNH: {self.cnh})"


class CadastroGeral:
    def __init__(self):
        self.placas_carros = []
        self.placas_caminhoes = []
        self.motoristas = []
        
    def cadastrar_veiculo(self, veiculo):
        if isinstance(veiculo, Carro):
            self.placas_carros.append(veiculo.placa)
            print('-> Carro cadastrado com sucesso!')
        elif isinstance(veiculo, Caminhao):
            self.placas_caminhoes.append(veiculo.placa)
            print('-> Caminhão cadastrado com sucesso!')
        else:
            print('-> Falha no cadastro do veículo.')

    def cadastrar_motorista(self, motorista):
        self.motoristas.append(motorista)
        print(f'-> Motorista {motorista.nome} cadastrado com sucesso!')
        
#Criar o sistema de cadastro geral
sistema = CadastroGeral()

#Criar os objetos
meu_carrinho = Carro("ABC-123")
meu_caminhaozinho = Caminhao("XYZ-987")
motoristinha = motorista("Cholinha")

#Cadastrar os objetos
sistema.meu_carrinho = 
print(sistema.placas_carros)
print(sistema.placas_camihoes)
print(sistema.motorista)
