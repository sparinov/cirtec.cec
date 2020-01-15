from templates import Column, ColumnType

class PopuTable:
    def __init__(self):
        self.name = 'popu'

        self.columns = [
            Column(title="pub", type=ColumnType.array,	template_str="{{subitem.pub}}"),
            Column(title="name", type=ColumnType.array,	template_str="{{subitem.name}}"),
            Column(title="neutral", type=ColumnType.array,	template_str="{{subitem.neutral}}"),
            Column(title="positive", type=ColumnType.array,	template_str="{{subitem.positive}}"),
            Column(title="negative", type=ColumnType.array,	template_str="{{subitem.negative}}"),
        ]
        
# {
#     "pub": "ranepa:rosa:doppubs:2169871",
#     "name": "Качество администрирования налога на добавленную стоимость в странах ОЭСР и России (Quality of VAT Administration in OECD Countries and Russia)",
#     "neutral": 16,
#     "positive": 0,
#     "negative": 1
# }