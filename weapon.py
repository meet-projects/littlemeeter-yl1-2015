import turtle

class weapon(Turtle):
	def __init__(self,canvas,x,y,dz,dy,shape,damage,mana_cost,mana_use):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.status_bool = False
		self.goto(x,y)
	`	self.damage=damage
		self.mana_cost=mana_cost
		self.dx = dx
        self.dy = dy
        self.mana_use = mana_use
		self.shape("weapon")

	#def checkifenemyisinrange(self,enemy):
		#x= self.xcor()
		#y=self.ycor()
		#if((self.ycor()=enemy.ycor()) and (enemy.xcor()-self.xcor()<0)):
					#return True
		#else:
			#return False 

		
	def get_mana_use(self):

		return self.mana_use
		
	def shoot(self,distance):
		x= self.xcor()
		y=self.ycor()
                                
		self.goto(x+distance,y)


	def show(self):
		self.showturtle()
		self.status_bool = True

	def status(self):
		return self.status_bool


	def hide(self):
		self.hideturtle()
		self.status_bool=False



	

turtle.mainloop()
