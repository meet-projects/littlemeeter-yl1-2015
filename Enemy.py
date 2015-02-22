from turtle import *
import weapon

class Enemy(Turtle):
	
	def __init__(self,canvas,x,y):
		RawTurtle.__init__(self,canvas,maxHealth,maxMana,dx,dy)

		self.penup()
		self.goto(x,y)
		self.shape("enemy")
		self.dx = dx
		self.dy = dy
		self.health = maxHealth
		self.mana = maxMana	
		self.attack1 = Weapon()
		
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
		if((self.attack1.getAttackDistanceY() - player.ycor() < 0) and (self.attack1.getAttackDistanceX() - player.xcor() < 0)):
			return True
		return False 
	
	def attack(self, player):
		if(checkIfPlayerIsInRange(player) and self.attack1.canActivate(self.mana)):
			self.attack1.activate()
			player.decreaseHealth(self.attack1.getDamage())
		
	def decreaseHealth(self,damage):
		self.health -= damage
	
	def addMana(self,manaAdd):
		self.mana += manaAdd
	
	def artificialIntelegence(self,player):
		
		self.attack(player)		

		if(player.xcor() > self.xcor())
			self.moveRight()
		elif(player.xcor() < self.xcor()):
			self.moveLeft()
		
		if(player.ycor() > self.ycor()):
			self.moveUp()
		elif(player.ycor() < self.ycor()):
			self.moveDown()
	
	def isDead(self):
		if(self.health < 0)
			return True
		return False 

	
		
		





