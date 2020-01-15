from templates import Column, ColumnType

class TangTable:
	def __init__(self):
		self.name = 'tang'

		self.columns = [
			Column(title="class_pos_neg", type=ColumnType.cell, template_str="{{item.class_pos_neg}}"),
			Column(
				title="title",
				type=ColumnType.array,
				array_key="ngramms",
				template_str="{{subitem.title}}",
			),
			Column(
				title="count",
				type=ColumnType.array,
				array_key="ngramms",
				template_str="{{subitem.count}}",
			),
		]

# {
#   "class_pos_neg": "positive",
#   "ngramms": [
#    {
#     "title": "темп рост",
#     "count": 18
#    },
#    {
#     "title": "уровень безработица",
#     "count": 16
#    },
#    {
#     "title": "экономический рост",
#     "count": 15
#    },
#    {
#     "title": "public goods",
#     "count": 11
#    },
#    {
#     "title": "разрыв выпуск",
#     "count": 10
#    },
#    {
#     "title": "фильтр калман",
#     "count": 10
#    },
#    {
#     "title": "financial assistance",
#     "count": 8
#    },
#    {
#     "title": "естественный уровень",
#     "count": 8
#    },
#    {
#     "title": "без постоянный",
#     "count": 7
#    },
#    {
#     "title": "долгосрочный перспектива",
#     "count": 7
#    }
#   ]
#  }
