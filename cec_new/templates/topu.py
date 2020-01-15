from templates import Column, ColumnType

class TopuTable:
	def __init__(self):
		self.name = 'topu'

		self.columns = [
			Column(title="topic", type=ColumnType.cell, template_str="{{item.topic}}"),
			Column(title="probability_avg", type=ColumnType.cell, template_str="{{item.probability_avg}}"),
			Column(title="probability_stddev", type=ColumnType.cell, template_str="{{item.probability_stddev}}"),
			Column(title="count_pubs", type=ColumnType.cell, template_str="{{item.count_pubs}}"),
			Column(title="count_conts", type=ColumnType.cell, template_str="{{item.count_conts}}"),
			Column(
				title="publications",
				type=ColumnType.array,
				array_key="publications",
				template_str="{{subitem}}",
			),
		]

# {
#   "topic": "рост, экономический, ввп, темп, экономика",
#   "probability_avg": 0.8654285714285714,
#   "probability_stddev": 0.1506574706723425,
#   "count_pubs": 20,
#   "count_conts": 140,
#   "publications": [
#    "repec:rnp:ppaper:021911",
#    "ranepa:rosa:doppubs:3339298",
#    "ranepa:rosa:doppubs:2169871",
#    "repec:gai:rpaper:128",
#    "repec:rnp:ecopol:1532",
#    "repec:rnp:ppaper:021915",
#    "ranepa:rosa:doppubs:3338329",
#    "ranepa:rosa:doppubs:3339270",
#    "repec:rnp:ecopol:ep1426",
#    "repec:gai:rpaper:rpaper-2018-173p-904",
#    "repec:ris:apltrx:0084",
#    "repec:gai:rpaper:126",
#    "repec:rnp:ecopol:ep1457",
#    "ranepa:rosa:doppubs:2600000",
#    "repec:gai:rpaper:125",
#    "repec:gai:wpaper:0113",
#    "repec:rnp:ppaper:011801",
#    "repec:rnp:ppaper:021907",
#    "ranepa:rosa:doppubs:3109344",
#    "repec:rnp:ecopol:ep1711"
#   ]
#  }