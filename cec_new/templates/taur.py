from templates import Column, ColumnType

class TaurTable:
	def __init__(self):
		self.name = 'taur'

		self.columns = [
			Column(title="author", type=ColumnType.cell, template_str="{{item.author}}"),
			Column(title="cits", type=ColumnType.cell, template_str="{{item.cits}}"),
			Column(title="pubs", type=ColumnType.cell, template_str="{{item.pubs}}"),
			Column(title="total_cits", type=ColumnType.cell, template_str="{{item.total_cits}}"),
			Column(title="total_pubs", type=ColumnType.cell, template_str="{{item.total_pubs}}"),
		]

# {
#   "author": "IMF",
#   "cits": 62,
#   "pubs": 7,
#   "total_cits": 474,
#   "total_pubs": 248
#  },