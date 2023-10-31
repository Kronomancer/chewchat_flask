class Comment: 
	_id_counter = 0 #Every class receives a unique ID starting from 0
	
	def __init__ (self, user, content):
		self.id = Comment._get_next_id()
		self.user = user
		self.content = content
		self.rating = 1

	@classmethod	
	def _get_next_id(cls): 
		current_id = cls._id_counter
		cls._id_counter += 1
		return current_id
		
	def increment_rating(self):
		self.rating += 1

	def decrement_rating(self):
		self.rating -= 1

class Thread(Comment):
	def __init__ (self, user, content, title):
		super().__init__(user, content)
		self.title = title
