#chamar método de abstração
from abc import ABC, abstractmethod

class Veiculo(ABC):
  def __init__(self,placa, modelo):
    self.__placa = placa
    self.__modelo = modelo

  @property
  def placa(self):
    return self.__placa
  @property
  def modelo(self):
    return self.__modelo

  @placa.setter
  def placa(self, p):
    self.__placa = p
  @modelo.setter
  def modelo(self, m):
    self.__modelo = m
  
  @abstractmethod
  def cadastro_placa(self):
    pass
  @abstractmethod
  def cadastro_modelo(self):
    pass
  
class Carro(Veiculo):
    def cadastro_placa(self):
      self.placa = input('digite a placa do carro: ')
      
    def cadastro_modelo(self):
      self.modelo = input('digite o modelo do carro: ')

    def calcular_custo(self):
      custo_medio = 0,55
      km_percorrido = input('quantos quilômetros você percoreu? ')
      custo_total = (km_percorrido / custo_medio) * 6,54
      
class Caminhao(Veiculo):
  def cadastro_placa(self):
    self.placa = input('digite a placa do caminhão: ')

  def cadastro_modelo(self):
    self.modelo = input('digite o modelo do caminhão: ')

  def calcular_custo(self):
    custo_medio = 1,22
    km_percorrido = input('quantos quilômetros você percoreu? ')
    custo_total = (km_percorrido / custo_medio) * 6,54

class Motorista:
  def __init__(self):
    self.nome = ''

  def nome(self):
    self.nome = input('digite seu nome: ')

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
