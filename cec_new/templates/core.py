class Column(object): 
    def __init__(self, name, template):
		self.name = name
		self.template = template

	def get_template(self):
		return self.template
