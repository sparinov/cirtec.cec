from templates import Column, ColumnType

class TestTable:
	def __init__(self):
		self.name = 'test'

		self.columns = [
			Column(title="sum", type=ColumnType.cell, template_str="{{item.sum}}"),
			# Column(title="probability_avg", type=ColumnType.cell, template_str="{{item.probability_avg}}"),
			# Column(title="probability_stddev", type=ColumnType.cell, template_str="{{item.probability_stddev}}"),
			# Column(title="count_pubs", type=ColumnType.cell, template_str="{{item.count_pubs}}"),
			# Column(title="count_conts", type=ColumnType.cell, template_str="{{item.count_conts}}"),
			# Column(
			# 	title="publications",
			# 	type=ColumnType.array,
			# 	array_key="publications",
			# 	template_str="{{subitem}}",
			# ),
		]

# {
#     "expenditure, see, government, budget, output": {
#         "sum": 206,
#         "frags": {"1": 49, "2": 68, "3": 49, "4": 31, "5": 9},
#     },
#     "оценка, расход, государственный, бюджет, обязательство": {
#         "sum": 158,
#         "frags": {"1": 53, "2": 22, "3": 35, "4": 41, "5": 7},
#     },
#     "цена, товар, уровень, работа, результат": {
#         "sum": 155,
#         "frags": {"1": 81, "2": 43, "3": 23, "4": 5, "5": 3},
#     },
#     "рост, оценка, ввп, экономический, разрыв": {
#         "sum": 152,
#         "frags": {"1": 39, "2": 42, "3": 26, "4": 24, "5": 21},
#     },
#     "public, goods, provision, region, see": {
#         "sum": 149,
#         "frags": {"1": 82, "2": 41, "3": 12, "4": 8, "5": 6},
#     },
#     "цена, фильтр, разрыв, работа, выпуск": {
#         "sum": 140,
#         "frags": {"1": 31, "2": 58, "3": 44, "4": 7, "5": 0},
#     },
#     "рост, уровень, высокий, ставка, экономический": {
#         "sum": 116,
#         "frags": {"1": 65, "2": 19, "3": 18, "4": 12, "5": 2},
#     },
#     "expenditure, see, economic, growth, al": {
#         "sum": 113,
#         "frags": {"1": 23, "2": 45, "3": 24, "4": 17, "5": 4},
#     },
#     "ндс, таможенный, страна, работа, капитал": {
#         "sum": 105,
#         "frags": {"1": 71, "2": 24, "3": 7, "4": 2, "5": 1},
#     },
#     "ряд, компонент, цена, страна, уровень": {
#         "sum": 102,
#         "frags": {"1": 41, "2": 15, "3": 33, "4": 1, "5": 12},
#     },
#     "рост, экономический, ввп, уровень, фактор": {
#         "sum": 96,
#         "frags": {"1": 43, "2": 7, "3": 12, "4": 3, "5": 31},
#     },
#     "see, рост, экономика, доход, government": {
#         "sum": 95,
#         "frags": {"1": 33, "2": 28, "3": 15, "4": 10, "5": 9},
#     },
#     "see, год, ввп, уровень, цена": {
#         "sum": 92,
#         "frags": {"1": 39, "2": 25, "3": 13, "4": 8, "5": 7},
#     },
#     "работа, страна, see, капитал, политика": {
#         "sum": 79,
#         "frags": {"1": 35, "2": 23, "3": 12, "4": 6, "5": 3},
#     },
#     "получить, уровень, потенциальный, можно, цена": {
#         "sum": 78,
#         "frags": {"1": 29, "2": 22, "3": 11, "4": 10, "5": 6},
#     },
#     "government, see, работа, ряд, бюджетный": {
#         "sum": 75,
#         "frags": {"1": 34, "2": 27, "3": 10, "4": 3, "5": 1},
#     },
#     "экономика, фискальный, риск, страна, государственный": {
#         "sum": 75,
#         "frags": {"1": 37, "2": 23, "3": 4, "4": 5, "5": 6},
#     },
#     "political, model, уровень, voter, policy": {
#         "sum": 69,
#         "frags": {"1": 41, "2": 8, "3": 6, "4": 3, "5": 11},
#     },
#     "рост, долгосрочный, значение, функция, модель": {
#         "sum": 54,
#         "frags": {"1": 25, "2": 14, "3": 4, "4": 9, "5": 2},
#     },
#     "уровень, цена, bear, component, selffunded": {
#         "sum": 38,
#         "frags": {"1": 11, "2": 3, "3": 18, "4": 4, "5": 2},
#     },
# }

