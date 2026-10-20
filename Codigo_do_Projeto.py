#chamar método de abstração
from abc import ABC, abstracmethod

class Veiculo(ABC):
  def __init__(self,placa, modelo):
    self.__placa = placa
    self.__modelo = modelo
  
  def cadastro_placa(self):
    pass
    
  def cadastro_modelo(self):
    pass
  
  
class Carro(Veiculo):

  
class Caminhao(Veiculo):

  
