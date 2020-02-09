import pygame, sys
from pygame.locals import *
from time import *
import os

current_path = os.path.dirname(__file__)

class Player:

	def __init__(self, name, image, position,team,range=1,max_health=50, damage=25, max_moves=3):
		self.name = name
		self.sprite = pygame.image.load(image)
		self.original_sprite=image
		self.position = position
		self.facing = 'UP'
		self.team=team
		self.range=range

		self.portrait = self.sprite
		self.isAlive=True

		self.has_attacked=False
		self.moves_left=3
		self.max_moves=max_moves

		self.max_health=max_health
		self.health=self.max_health
		self.damage=damage
	def start_turn(self):
		self.moves_left=3
		self.has_attacked = False
		self.sprite = pygame.image.load(self.original_sprite)
	def decrement_Moves(self,num):
		self.moves_left -= num
		if self.moves_left < 1:
			print(self.original_sprite[:-4]+"_gray.png")
			self.sprite = pygame.image.load(os.path.join(current_path,self.original_sprite[:-4]+"_gray.png"))
	def setPos(self,position):
		self.position=position
		return self
	def restoreSprite(self):
		self.sprite = pygame.image.load(self.original_sprite)
	def giveHit(self):
		self.has_attacked=True
		self.sprite = pygame.image.load(os.path.join(current_path,self.original_sprite[:-4]+"_gray.png"))
		return self
	def takeHit(self,attacker):
		self.health -= attacker.damage
		if self.health <= 0:
			self.isAlive = False
