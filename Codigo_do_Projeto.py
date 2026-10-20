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
      
class Caminhao(Veiculo):
  def cadastro_placa(self):
    self.placa = input('digite a placa do caminhão: ')

  def cadastro_modelo(self):
    self.modelo = input('digite o modelo do caminhão: ')

  
