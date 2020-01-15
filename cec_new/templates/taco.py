from templates import Column, ColumnType

class TacoTable:
	def __init__(self):
		self.name = 'taco'

		self.columns = [
			Column(title="class_pos_neg", type=ColumnType.cell, template_str="{{item.class_pos_neg}}"),
			Column(
				title="author",
				type=ColumnType.array,
				array_key="cocitauthors",
				template_str="{{subitem.author}}",
			),
			Column(
				title="count",
				type=ColumnType.array,
				array_key="cocitauthors",
				template_str="{{subitem.count}}",
			),
		]

# {
#   "class_pos_neg": "positive",
#   "cocitauthors": [
#    {
#     "author": "Идрисов",
#     "count": 2
#    },
#    {
#     "author": "1ZQRVU",
#     "count": 1
#    },
#    {
#     "author": "28YyZR",
#     "count": 1
#    },
#    {
#     "author": "Alfaro",
#     "count": 1
#    },
#    {
#     "author": "Ball",
#     "count": 1
#    },
#    {
#     "author": "Crespo",
#     "count": 1
#    },
#    {
#     "author": "FDPZKP",
#     "count": 1
#    },
#    {
#     "author": "Fontoura",
#     "count": 1
#    },
#    {
#     "author": "Friedman",
#     "count": 1
#    },
#    {
#     "author": "Gertler",
#     "count": 1
#    }
#   ]
#  }