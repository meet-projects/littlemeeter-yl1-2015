from turtle import *
from Weapon import Weapon

class Enemy(Turtle):
	
	def __init__(self,canvas,x,y):
		RawTurtle.__init__(self,canvas)
		self.speed(0)
		self.penup()
		self.goto(x,y)
		self.shape("turtle")
		self.dx = 5
		self.dy = 5
		self.health = 100
		self.mana = 100	
		self.attack1 = Weapon(canvas,10,20,30,0,2,self.xcor(),self.ycor())
		
	def moveUp(self):
		x = self.xcor()
		y = self.ycor() + self.dy
		self.goto(x,y)

	def moveDown(self):
		x = self.xcor()
		y = self.ycor() - self.dy
		self.goto(x,y)
	
	def moveRight(self):
		x = self.xcor() + self.dx
		y = self.ycor()
		self.goto(x,y)
	
	def moveLeft(self):
		x = self.xcor() - self.dx
		y = self.ycor()
		self.goto(x,y)
	
	def checkIfPlayerIsInRange(self,player):
		if self.ycor() + self.attack1.getAttackDistanceY() - player.ycor() > 0 and self.xcor()+self.attack1.getAttackDistanceX() - player.xcor() > 0 :
			return True
		return False 
	
	def attack(self, player):
		if self.checkIfPlayerIsInRange(player) and self.attack1.canActivate(self.mana) :
			self.attack1.activate()
			player.decreaseHealth(self.attack1.getDamage())
			self.addMana(-self.attack1.getManaCost())
		
	def decreaseHealth(self,damage):
		self.health -= damage
	
	def addMana(self,manaAdd):
		self.mana += manaAdd
	
	def artificialIntelegence(self,player):
		


		while(True):
			self.attack(player)		

			if player.xcor() > self.xcor():
				self.moveRight()
			elif player.xcor() < self.xcor():
				self.moveLeft()
		
			if player.ycor() > self.ycor():
				self.moveUp()
			elif player.ycor() < self.ycor():
				self.moveDown()
			for x in range(1,1000000):
				x+1
	
	def isDead(self):
		if self.health < 0:
			return True
		return False 

	def kill(self):
		self.hideturtle()

	
		
		





