from templates import Column, ColumnType


class RautTable:
    def __init__(self):
        self.columns = [
            Column(title="№", type=ColumnType.cell, template_str="1"), #{{ loop.index }}
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

