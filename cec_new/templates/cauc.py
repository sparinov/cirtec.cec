from templates import Column, ColumnType

class CaucTable:
	def __init__(self):
		self.name = 'cauc'

		self.columns = [
			Column(
				title="cocitpair",
				type=ColumnType.array,
				array_key="cocitpair",
				template_str="{{subitem}}",
			),
			Column(title="cont_cnt", type=ColumnType.cell, template_str="{{item.cont_cnt}}"),
			Column(title="pub_cnt", type=ColumnType.cell, template_str="{{item.pub_cnt}}"),
			Column(
				title="frags",
				type=ColumnType.array,
				array_key="frags",
				template_str="{{subitem}}",
			),
		]
