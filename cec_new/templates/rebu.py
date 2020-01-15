from templates import Column, ColumnType

class RebuTable:
	def __init__(self):
		self.name = 'rebu'

		self.columns = [
			Column(title="cits", type=ColumnType.cell, template_str="{{item.cits}}"),
			Column(title="bundle", type=ColumnType.cell, template_str="{{item.bundle}}"),
			Column(title="pubs", type=ColumnType.cell, template_str="{{item.pubs}}"),
			Column(title="total_cits", type=ColumnType.cell, template_str="{{item.total_cits}}"),
			Column(title="total_pubs", type=ColumnType.cell, template_str="{{item.total_pubs}}"),
			Column(title="title", type=ColumnType.cell, template_str="{{item.title}}"),
			Column(title="year", type=ColumnType.cell, template_str="{{item.year}}"),
			Column(
				title="authors",
				type=ColumnType.array,
				array_key="authors",
				template_str="{{subitem}}",
			),
			Column(
				title="pubs_ids",
				type=ColumnType.array,
				array_key="pubs_ids",
				template_str="{{subitem}}",
			),
			Column(
				title="topic",
				type=ColumnType.array,
				array_key="topics",
				template_str="{{subitem.topic}}",
			),
			Column(
				title="count",
				type=ColumnType.array,
				array_key="topics",
				template_str="{{subitem.count}}",
			),
		]

# {
#   "cits": 42,
#   "bundle": "2Q9OPZ",
#   "pubs": 2,
#   "pubs_ids": [
#    "repec:gai:rpaper:128",
#    "repec:gai:rpaper:126"
#   ],
#   "total_cits": 134,
#   "total_pubs": 53,
#   "year": "1999",
#   "authors": [
#    "Baxter",
#    "King"
#   ],
#   "title": "Measuring Business Cycles Approximate Band-Pass Filters for Economic Time Series",
#   "cont_ids": [
#    "repec:gai:rpaper:126@34159",
#    "repec:gai:rpaper:126@66978",
#    "repec:gai:rpaper:126@73815",
#    "repec:gai:rpaper:128@74297",
#    "repec:gai:rpaper:128@92602",
#    "repec:gai:rpaper:128@66567",
#    "repec:gai:rpaper:128@64782",
#    "repec:gai:rpaper:126@65637",
#    "repec:gai:rpaper:128@66978",
#    "repec:gai:rpaper:126@65636",
#    "repec:gai:rpaper:126@66567",
#    "repec:gai:rpaper:128@65636",
#    "repec:gai:rpaper:128@61992",
#    "repec:gai:rpaper:128@63929",
#    "repec:gai:rpaper:126@66979",
#    "repec:gai:rpaper:126@64783",
#    "repec:gai:rpaper:126@92602",
#    "repec:gai:rpaper:126@41170",
#    "repec:gai:rpaper:128@34160",
#    "repec:gai:rpaper:128@61993",
#    "repec:gai:rpaper:128@65637",
#    "repec:gai:rpaper:128@73816",
#    "repec:gai:rpaper:126@61993",
#    "repec:gai:rpaper:128@66979",
#    "repec:gai:rpaper:128@74296",
#    "repec:gai:rpaper:126@73816",
#    "repec:gai:rpaper:126@41169",
#    "repec:gai:rpaper:126@63929",
#    "repec:gai:rpaper:126@64782",
#    "repec:gai:rpaper:128@34159",
#    "repec:gai:rpaper:126@74297",
#    "repec:gai:rpaper:126@61992",
#    "repec:gai:rpaper:128@66568",
#    "repec:gai:rpaper:126@74296",
#    "repec:gai:rpaper:126@34160",
#    "repec:gai:rpaper:128@41170",
#    "repec:gai:rpaper:128@41169",
#    "repec:gai:rpaper:126@92603",
#    "repec:gai:rpaper:128@73815",
#    "repec:gai:rpaper:126@66568",
#    "repec:gai:rpaper:128@92603",
#    "repec:gai:rpaper:128@64783"
#   ],
#   "topics": [
#    {
#     "topic": "уровень, ввп, фильтр, цена, оценка",
#     "count": 6
#    },
#    {
#     "topic": "компонент, factor, фильтр, частота, technology",
#     "count": 4
#    },
#    {
#     "topic": "цена, уровень, товар, квартал, год",
#     "count": 4
#    },
#    {
#     "topic": "see, authority, экономический, рост, subnational",
#     "count": 2
#    },
#    {
#     "topic": "see, tax, budget, выпуск, фильтр",
#     "count": 2
#    },
#    {
#     "topic": "государственный, экономика, долг, кризис, потенциальный",
#     "count": 2
#    },
#    {
#     "topic": "страна, оценка, ввп, работа, цена",
#     "count": 2
#    }
#   ],
#   "ngrams": [
#    {
#     "ngramm": "полосовый фильтр",
#     "count": 14
#    },
#    {
#     "ngramm": "оценка потенциальный",
#     "count": 8
#    },
#    {
#     "ngramm": "потенциальный ввп",
#     "count": 8
#    },
#    {
#     "ngramm": "фильтр ходрикапрескотта",
#     "count": 8
#    },
#    {
#     "ngramm": "метод оценка",
#     "count": 6
#    },
#    {
#     "ngramm": "фильтр фильтр",
#     "count": 6
#    },
#    {
#     "ngramm": "фильтр являться",
#     "count": 6
#    },
#    {
#     "ngramm": "бизнесцикл статья",
#     "count": 4
#    },
#    {
#     "ngramm": "более высокий",
#     "count": 4
#    },
#    {
#     "ngramm": "высокий частота",
#     "count": 4
#    }
#   ]
#  }