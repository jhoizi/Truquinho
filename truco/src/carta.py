import pygame
from pygame.locals import *


class Carta(pygame.sprite.Sprite):

	imagem = ""
	valor = 0
	naipe = 0
	valor_str = ""
	posicao = 0

	def __init__(self, imagem, valor, naipe, valor_str):
		pygame.sprite.Sprite.__init__(self)
		self.imagem = imagem
		self.valor = valor
		self.naipe = naipe
		self.valor_str = valor_str
		self.posicao = imagem.get_rect()