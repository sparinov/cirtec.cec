from templates import Column, ColumnType

class RautTable:
    def __init__(self):
        self.name = 'raut'

        self.columns = [
            Column(
                title="paper",
                type=ColumnType.cell,
                template_str="""<a target="blank" href='{{'https://socionet.ru/publication.xml?h=' + item.pub_id}}'>
      				{{item.name}}
				</a>"""
            ),
            Column(title="3 authors", type=ColumnType.array, array_key="ref_authors", template_str="{{subitem.author}}"),
            Column(title="cits", type=ColumnType.array, array_key="ref_authors", template_str="{{subitem.cits}}"),
            Column(title="pubs", type=ColumnType.array, array_key="ref_authors", template_str="{{subitem.pubs}}"),
            Column(title="total cits", type=ColumnType.array, array_key="ref_authors", template_str="{{subitem.total_cits}}"),
            Column(title="total pubs", type=ColumnType.array, array_key="ref_authors", template_str="{{subitem.total_pubs}}"),
        ]

# {
#   "pub_id": "ranepa:rosa:doppubs:2169871",
#   "name": "Качество администрирования налога на добавленную стоимость в странах ОЭСР и России (Quality of VAT Administration in OECD Countries and Russia)",
#   "ref_authors": [
#    {
#     "author": "Aizenman",
#     "cits": 3,
#     "pubs": 1,
#     "total_cits": 9,
#     "total_pubs": 3
#    },
#    {
#     "author": "Jinjarak",
#     "cits": 3,
#     "pubs": 1,
#     "total_cits": 9,
#     "total_pubs": 3
#    },
#    {
#     "author": "Keen",
#     "cits": 3,
#     "pubs": 1,
#     "total_cits": 27,
#     "total_pubs": 17
#    }
#   ]
#  }