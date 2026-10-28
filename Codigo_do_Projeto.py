#chamar método de abstração
from abc import ABC, abstractmethod

class Veiculo(ABC):
  def __init__(self,placa, hora_saida):
    self.__placa = placa
    self.__produto = ""
    self.__hora_saida = hora_saida

  @property
  def placa(self):
    return self.__placa
  @property
  def produto(self):
    return self.__produto
  @property
  def hora_saida(self):
    return self.__hora_saida
  @abstractmethod
  @placa.setter
  def placa(self, p):
    self.__placa = p
    
  @produto.setter
  def produto(self, m):
    self.__produto = m
  
  def cadastro_produto(self):
    pass
  
class Carro(Veiculo): #classe carro apartir de veiculo
    def cadastro_placa(self):
      self.placa = input('digite a placa do carro: ')
      
    def cadastro_produto(self):
      self.produto = input('digite o produto do carro: ')

    def calcular_custo(self):
      custo_medio = 0.55
      km_percorrido = input('quantos quilômetros você percoreu? ')
      custo_total = (km_percorrido // custo_medio) * 6.54
      
class Caminhao(Veiculo):
  def cadastro_placa(self):
    self.placa = input('digite a placa do caminhão: ')

  def cadastro_produto(self):
    self.produto = input('digite o produto do caminhão: ')

  def calcular_custo(self):
    custo_medio = 1.22
    km_percorrido = input('quantos quilômetros você percoreu? ')
    custo_total = (km_percorrido // custo_medio) * 6.54

class Motorista:
  def __init__(self):
    self.nome = ''
    self.cnh = ''
    self.tipo_veiculo = ''

  def viagens_

  
  class CadastroGeral(Veiculo):
  def __init__(self):
    self.placas_carros = []
    self.placas_caminhoes = []
    
  def cadastrar_placas(self, veiculo):
    if isinstance(veiculo, Carro):
      self.placas_carros.append(veiculo.placa)
      print('carro cadastrado com sucesso')

    elif isinstance(veiculo, Caminhao):
      self.placas_caminhoes.append(veiculo.placa)
      print('caminhão cadastrado com sucesso')
      
    else:
      print('cadastro falho')


#Menu de entrada do código principal
print('')

#Código principal
qtde = int(input('Quantas seções quer registrar?'))
for i in range(qtde):
  tipo = input('Qual tipo de veículo você maneja? ').lower()
  if tipo == 'carro':
    v = Carro('','')
  else:
    v = Caminhao()
  #Viagens
  v.calcular_custo()
