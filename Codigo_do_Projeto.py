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
  
  def cadastro_placa(self):
    pass
    
  def cadastro_modelo(self):
    pass
  
  
class Carro(Veiculo):

  
class Caminhao(Veiculo):

  
