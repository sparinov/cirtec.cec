from templates import Column, ColumnType

class TatoTable:
	def __init__(self):
		self.name = 'tato'

		self.columns = [
			Column(title="class_pos_neg", type=ColumnType.cell, template_str="{{item.class_pos_neg}}"),
			Column(title="topic_cnt", type=ColumnType.cell, template_str="{{item.topic_cnt}}"),
			Column(
				title="topics name",
				type=ColumnType.array,
				array_key="topics",
				template_str="{{subitem.topic}}",
			),
			Column(
				title="№",
				type=ColumnType.array,
				array_key="topics",
				template_str="{{subitem.count}}",
			),
		]

# {
#   "class_pos_neg": "positive",
#   "topic_cnt": 11,
#   "topics": [
#    {
#     "topic": "рост, экономический, ввп, темп, экономика",
#     "count": 14
#    },
#    {
#     "topic": "разрыв, уровень, оценка, работа, выпуск",
#     "count": 13
#    },
#    {
#     "topic": "public, government, expenditure, budget, financial",
#     "count": 6
#    },
#    {
#     "topic": "see, authority, экономический, рост, subnational",
#     "count": 6
#    },
#    {
#     "topic": "see, tax, budget, выпуск, фильтр",
#     "count": 5
#    },
#    {
#     "topic": "government, growth, see, rate, модель",
#     "count": 3
#    },
#    {
#     "topic": "компонент, factor, фильтр, частота, technology",
#     "count": 2
#    },
#    {
#     "topic": "уровень, ввп, фильтр, цена, оценка",
#     "count": 2
#    },
#    {
#     "topic": "see, budget, ндс, country, constraint",
#     "count": 1
#    },
#    {
#     "topic": "цена, уровень, товар, регион, работа",
#     "count": 1
#    },
#    {
#     "topic": "страна, оценка, ввп, работа, цена",
#     "count": 1
#    }
#   ]
#  }