class Page: 
    def __init__ (self, name, description=""):
        self.name = name
        self.description = description
        self.threads = []
    def add_thread(self, thread):
        self.threads.append(thread)

class City(Page):
	def __init__ (self, name):
		super().__init__(name)
		self.restaurants = []
	def add_restaurant(self, restaurant):
		self.restaurants.append(restaurant)

class Restaurant(Page):
	def __init__ (self, name, city, description=""):
		super().__init__(name, description)
		self.city = city
		self.menuItems = []
	def add_menuItem(self, menuItem):
		self.menuItems.append(menuItem)