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

	def enemyisinrange(self,enemy):
	x= self.xcor()
	y=self.ycor()

	if(self.ycor()=enemy.ycor() and (enemy.xcor()-self.xcor():
		return True
	
		
	def get_mana_use(self):

		return self.mana_use
		


	def show(self):
		self.showturtle()
		self.status_bool = True

	def status(self):
		return self.status_bool


	def hide(self):
		self.hideturtle()
		self.status_bool=False


	def shoot(self):
		if mana_status==True
			for x in range(0,800,1):
				x= self.xcor()
				y=self.ycor()
				self.goto (x,y)
		else:
			print("not enof mama")	
	

	def return_weapon (self,player):
		if enemyisinrange== True:
			hide() 
			self.goto(player.xcor(),player.ycor())
#make sure

	

turtle.mainloop()
