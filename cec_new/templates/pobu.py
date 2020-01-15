from templates import Column, ColumnType

class PobuTable:
	def __init__(self):
		self.name = 'pobu'

		self.columns = [
			Column(title="_id", type=ColumnType.cell, template_str="{{item._id}}"),
			Column(title="cits", type=ColumnType.cell, template_str="{{item.cits}}"),
			Column(title="pubs", type=ColumnType.cell, template_str="{{item.pubs}}"),
			Column(title="total_cits", type=ColumnType.cell, template_str="{{item.total_cits}}"),
			Column(title="total_pubs", type=ColumnType.cell, template_str="{{item.total_pubs}}"),
			Column(title="year", type=ColumnType.cell, template_str="{{item.year}}"),
			Column(title="title", type=ColumnType.cell, template_str="{{item.title}}"),
			Column(
				title="authors",
				type=ColumnType.array,
				array_key="authors",
				template_str="{{subitem}}",
			),
              ]
        
# {
#   "_id": "2Q9OPZ",
#   "cits": 42,
#   "pubs": 2,
#   "total_cits": 134,
#   "total_pubs": 53,
#   "year": "1999",
#   "authors": [
#    "Baxter",
#    "King"
#   ],
#   "title": "Measuring Business Cycles Approximate Band-Pass Filters for Economic Time Series",
#   "class_pos_neg": {
#    "neutral": 30,
#    "positive": 4,
#    "negative": 8
#   }
#  }