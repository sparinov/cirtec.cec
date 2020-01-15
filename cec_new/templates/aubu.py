from templates import Column, ColumnType

class AubuTable:
	def __init__(self):
		self.name = 'aubu'

		self.columns = [
			Column(title="aurhor", type=ColumnType.cell, template_str="{{item.aurhor}}"),
			Column(title="cits", type=ColumnType.cell, template_str="{{item.cits}}"),
			Column(title="pubs", type=ColumnType.cell, template_str="{{item.pubs}}"),
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
			Column(
				title="ngrams name",
				type=ColumnType.array,
				array_key="ngrams",
				template_str="{{subitem.ngramm}}",
			),
			Column(
				title="№",
				type=ColumnType.array,
				array_key="ngrams",
				template_str="{{subitem.count}}",
			),
		]

