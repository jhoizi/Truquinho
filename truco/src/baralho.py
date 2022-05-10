import pygame
from pygame.locals import *
from carta import *
from configs import *

class Baralho:
  
  truco = {}
  naipes = ['paus', 'copas', 'espadas', 'ouros']
  cartas = ['4.png', '5.png', '6.png', '7.png', 'Q.png', 'J.png', 'K.png', 'as.png', '2.png', '3.png']


  def __init__(self):
        
    self.organizar()

    for naipe in self.naipes:
      n = 1
      c = 1
      
      for carta in self.cartas:
        valor = c 
        naipe_valor = n
        valor_str = carta[:-4]
        imagem = pygame.image.load(baralho_dir + naipe + "/" + carta)
        carta1 = Carta(imagem, valor, naipe_valor, valor_str)
        self.truco[naipe].append(carta1)
        c += 1

      n += 1

  def organizar(self):
    self.truco = dict.fromkeys(self.naipes)
    for naipe in self.naipes:
      self.truco[naipe] = []
