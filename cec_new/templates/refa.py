from templates import Column, ColumnType

class RefaTable:
	def __init__(self):
		self.name = 'refa'

		self.columns = [
			Column(title="author", type=ColumnType.cell, template_str="{{item._id}}"),
			Column(title="cits", type=ColumnType.cell, template_str="{{item.cits}}"),
			Column(title="pubs", type=ColumnType.cell, template_str="{{item.pubs}}"),
			Column(title="total_cits", type=ColumnType.cell, template_str="{{item.total_cits}}"),
			Column(title="total_pubs", type=ColumnType.cell, template_str="{{item.total_pubs}}"),
			Column(title="title", type=ColumnType.cell, template_str="{{item.title}}"),
			Column(
				title="frags",
				type=ColumnType.array,
				array_key="authors",
				template_str="{{subitem}}",
			),
		]

# {
#   "author": "IMF",
#   "cits": 62,
#   "pubs": 7,
#   "total_cits": 474,
#   "total_pubs": 248,
#   "frags": {
#    "1": 32,
#    "2": 15,
#    "3": 14,
#    "4": 10
#   }
#  }