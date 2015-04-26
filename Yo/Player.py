from turtle import *
from Weapon import Weapon

class Player(Turtle):
	def __init__(self, maxMana,maxHealth,shapeNumber,canvas,x,y):
		RawTurtle.__init__(self,canvas)
		self.speed(0)
		self.penup()
		self.goto(x,y)
		self.mana = maxMana
		self.health = maxHealth
		self.weapon = Weapon(canvas,50,200,30,5,1,self.xcor(),self.ycor())
		#self.shape("Player" + str(shapeNumber))

	def decreaseHealth(self, damage):
		self.health = self.health - damage

	def attack(self):
		if self.weapon.canActivate(self.mana):
			self.weapon.disaMove(self.xcor(),self.ycor())
			self.weapon.activate()
			self.addMana(-self.weapon.getManaCost())

	def addMana(self,manaAdd):
		self.mana += manaAdd

	def getWeapon(self):
		return self.weapon

	def goUp(self):
		if self.ycor() + 5 > 500:
			return
		self.goto(self.xcor(),self.ycor()+5)
		if not self.weapon.isActivated():
			self.weapon.disaMove(self.xcor(),self.ycor())
		

	def goDown(self):
		if self.ycor() - 5 < 0:
			return
		self.goto(self.xcor(),self.ycor()-5)
		if not self.weapon.isActivated():
			self.weapon.disaMove(self.xcor(),self.ycor())

	def goLeft(self):
		if self.xcor() - 5 < 0:
			return
		self.goto(self.xcor()-5, self.ycor())
		if not self.weapon.isActivated():
			self.weapon.disaMove(self.xcor(),self.ycor())
		
	def goRight(self):
		if self.xcor() + 5 > 500:
			return
		self.goto(self.xcor()+5, self.ycor())
		if not self.weapon.isActivated():
			self.weapon.disaMove(self.xcor(),self.ycor())


