from turtle import *

class Weapon(Turtle):
	def __init__(self,canvas,damage,attackDistanceX,attackDistanceY,manaCost,attackNumber,x,y):
		RawTurtle.__init__(self,canvas)
		self.hideturtle()
		self.speed(0)
		self.penup()
		self.goto(x,y)
		self.penup()
		self.damage = damage
		self.attackDistanceX = attackDistanceX
		self.attackDistanceY = attackDistanceY
		self.isActivate = False
		self.manaCost = manaCost
		self.distance = 0
		#self.shape("attack"+str(attackNumber))
		self.shape("turtle")

	def getAttackDistanceX(self):
		return self.attackDistanceX

	def getAttackDistanceY(self):
		return self.attackDistanceX

	def activate(self):
		self.isActivate = True
		self.showturtle()
		self.attackAnime()

	def deactivate(self):
		self.isActivate = False
		self.hideturtle()

	def isActivated(self):
		if self.xcor() < 0 or self.xcor() > 500 or self.ycor() < 0 or self.ycor() > 500:
			self.deactivate()
		return self.isActivate

	def getDamage(self):
		return self.damage

	def canActivate(self, manaAmount):
		if manaAmount > self.manaCost :
			return True
		return False

	def disaMove(self,x,y):
		self.hideturtle()
		self.goto(x,y)
		
	def getManaCost(self):
		return self.manaCost

	def attackAnime(self):
		while self.xcor() > 0 and self.xcor() < 500:
			self.goto(self.xcor()+3,self.ycor())
		self.disaMove(0,0)
		