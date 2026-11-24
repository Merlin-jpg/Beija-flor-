from abc import ABC, abstractmethod # Aqui é a implementaçã ode classes abstratadas no código como
from collections import defaultdict # Isso serve para a criação de listas de produtos

class Produto: # Usamos essas classe para criar e guardar informações de produto que forem chegar na empresa
    def __init__(self, nome, data_validade, data_entrega, valor_mercado, quant, marca=""):
	# Dentre as informações que recebremos dos produtos temos:
        self.__nome = nome # Seu nome para a identificação e organização da lista 
        self.__data_validade = data validade # Támbem obtemos o tempo dos pereciveis, o formato deve ser "DD/MM/AAAA"
        self.__data_entrega = data entrega # Aqui usamos a data em que foi entregue para sabermos quanto tempo temos para entregar apartir da comparação com a data de validade , o formato deve ser "DD/MM/AAAA"
        self.__valor = valor mercado # Quanto o produto custa no mercado para saber quanto vamos cobrar pela entrega
        self.__marca = marca # Essa parte é opcional, mas pode ser utilizado para separar ela na lista
        self.__quant = quant # A quantidade é pra diminuir na lista para que não seja necessário fazer um objeto para cada produto com nome igual

    # Como as classes são privados então temos que por os propertys para que seja visivel o que está sendo posto em produtos		
    @property
    def nome(self):
        return self.__nome

    @property
    def data_entrega(self):
        return self.__data_entrega

    @property
    def data_validade(self):
        return self.__data_validade

    @data_validade.setter
    def data_validade(self, nova_data):
        self.__data_validade = nova_data

    @abstactmethod
    def cadastro_produto(lista_de_produtos):
        produtos_agrupados = defaultdict(list)
        for produto in lista_de_produtos:
            produtos_agrupados[produto.nome].append(produto)

        return {
            nome: sorted(lista, key=lambda p: p.data_entrega)
            for nome, lista in produtos_agrupados.items()
        }

    def __repr__(self):
        return f"Produto({self.__nome}, Entrega: {self.__data_entrega}, Qtd: {self.__quant})"


class Veiculo(ABC):
    def __init__(self, placa, hora_saida, km_percorrido=0.0, produto_entregue=None):
        self.__placa = placa
        self.__hora_saida = hora_saida
        self.__km_percorrido = km_percorrido
        self.__produto_entregue = {}
        self.__abastecido = False

        if produto_entregue:
            self.cadastro_produto_entregue(produto_entregue)

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, nova_placa):
        self.__placa = nova_placa

    @property
    def hora_saida(self):
        return self.__hora_saida

    @property
    def km_percorrido(self):
        return self.__km_percorrido

    @km_percorrido.setter
    def km_percorrido(self, km):
        self.__km_percorrido = km

    @property
    def produto_entregue(self):
        return self.__produto_entregue

    def cadastro_produto_entregue(self, lista_bruta):
        self.__produto_entregue = Produto.cadastro_produto(lista_bruta)
        return self.__produto_entregue

    @abstractmethod
    def calcular_consumo(self):
        pass


class Carro(Veiculo):
    def calcular_consumo(self):
        return (self.km_percorrido / 10) * 5.80


class Caminhao(Veiculo):
    def __init__(self, placa, hora_saida, km_percorrido=0.0, eixos=2, produto_entregue=None):
        super().__init__(placa, hora_saida, km_percorrido, produto_entregue)
        self.__eixos = eixos

    def calcular_consumo(self):
        return (self.km_percorrido * 1.22) * 6.54


class Motorista:
    def __init__(self, nome, cnh, tipo_veiculo):
        self.nome = nome
        self.cnh = cnh
        self.tipo_veiculo = tipo_veiculo

    def __repr__(self):
        return f"{self.nome} (CNH: {self.cnh} - {self.tipo_veiculo})"


class CadastroGeral:
    def __init__(self):
        self.veiculos = []
        self.placas_carros = []
        self.placas_caminhoes = []
        self.motoristas = []
        self.produtos = []

    def cadastrar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
        if isinstance(veiculo, Carro):
            self.placas_carros.append(veiculo.placa)
            print("-> Carro cadastrado!")
        elif isinstance(veiculo, Caminhao):
            self.placas_caminhoes.append(veiculo.placa)
            print("-> Caminhão cadastrado!")

    def cadastrar_motorista(self, motorista):
        self.motoristas.append(motorista)
        print("-> Motorista cadastrado!")

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)
        print("-> Produto cadastrado!")

sistema = CadastroGeral()

# Cadastro inicial de um carro
print("\n--- Cadastro de Carro ---")
placa = input("Digite a placa do carro: ")
hora = input("Digite a hora de saída: ")
km = float(input("Digite os KM percorridos: "))

sistema.cadastrar_veiculo(Carro(placa, hora, km))


# Cadastro inicial de um caminhão
print("\n--- Cadastro de Caminhão ---")
placa = input("Digite a placa do caminhão: ")
hora = input("Digite a hora de saída: ")
km = float(input("Digite os KM percorridos: "))
eixos = int(input("Digite a quantidade de eixos: "))

sistema.cadastrar_veiculo(Caminhao(placa, hora, km, eixos))


# Cadastro inicial de um motorista
print("\n--- Cadastro de Motorista ---")
nome = input("Digite o nome do motorista: ")
cnh = input("Digite a CNH: ")
tipo = input("Digite o tipo de veículo: ")

sistema.cadastrar_motorista(Motorista(nome, cnh, tipo))


# Cadastro inicial de um produto
print("\n--- Cadastro de Produto ---")
nome = input("Digite o nome do produto: ")
validade = input("Digite a data de validade (DD/MM/AAAA): ")
entrega = input("Digite a data de entrega (DD/MM/AAAA): ")
valor = float(input("Digite o valor do produto: "))
quant = int(input("Digite a quantidade: "))

sistema.cadastrar_produto(Produto(nome, validade, entrega, valor, quant))

while True:
    print("\n1 - Cadastrar Veículo | 2 - Cadastrar Motorista | 3 - Cadastrar Produto | 4 - Ver Resumo | 0 - Sair")
    op = input("Opção: ").strip()

    if op == "1":
        tipo = input("Tipo (carro/caminhao): ").strip().lower()
        placa = input("Placa: ").strip()
        hora = input("Hora de saída: ").strip()
        km = float(input("KM percorrido: "))
        if tipo == "caminhao":
            eixos = int(input("Eixos: "))
            sistema.cadastrar_veiculo(Caminhao(placa, hora, km, eixos))
        else:
            sistema.cadastrar_veiculo(Carro(placa, hora, km))

    elif op == "2":
        nome = input("Nome: ").strip()
        cnh = input("CNH: ").strip()
        tipo = input("Tipo de veículo: ").strip()
        sistema.cadastrar_motorista(Motorista(nome, cnh, tipo))

    elif op == "3":
        nome = input("Produto: ").strip()
        validade = input("Validade (DD/MM/AAAA): ").strip()
        entrega = input("Entrega (DD/MM/AAAA): ").strip()
        valor = float(input("Valor: "))
        quant = int(input("Quantidade: "))
        sistema.cadastrar_produto(Produto(nome, validade, entrega, valor, quant))

    elif op == "4":
        print("\nVeículos e custos:")
        for v in sistema.veiculos:
            print(f"- {v.placa}: R$ {v.calcular_consumo():.2f}")

        print("\nMotoristas:", sistema.motoristas)
        print("Produtos organizados:", Produto.cadastro_produto(sistema.produtos))

    elif op == "0":
        break
