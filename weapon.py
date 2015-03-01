import turtle

class weapon(Turtle):
	def _init_(self,canvas,x,y,dz,dy,shape,damage,mana_cost):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
	`	self.damage=damage
		self.mana_cost=mana_cost
		self.dx = dx
        self.dy = dy
		self.shape("weapon")

	#def checkifenemyisinrange(self,enemy):
		#x= self.xcor()
		#y=self.ycor()
		#if((self.ycor()=enemy.ycor()) and (enemy.xcor()-self.xcor()<0)):
					#return True
		#else:
			#return False 

		
	def mana_use(self):

		mana_power-self.mana_cost
		
	def shoot(self,distance):
		x= self.xcor()
		y=self.ycor()
                                
		self.goto(x+distance,y)


	def weapon.show(self):
		turtle.showturtle()


	def weapon.hide(self):
		turtle.hideturtle()



	

turtle.mainloop()
