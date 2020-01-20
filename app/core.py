from enum import Enum
from jinja2 import Template


def initColumns(columns, key, object):
    row_type = type(object[key])
    if row_type == str or row_type == int:
        columns.append(
            Column(title=key, type=ColumnType.cell, template_str="{{item." + key + "}}")
        )

    elif row_type == dict:
        columns.append(
            Column(
                title=key,
                type=ColumnType.dict,
                template_str="{{key}}  ---  {{item[key]}}",
            )
        )

    elif row_type == list:
        first_array_row = type(object[key][0])

        if first_array_row == str or row_type == int:
            columns.append(
                Column(title=key, type=ColumnType.array, template_str="{{subitem}}")
            )
        if first_array_row == dict:
            for row_key in object[key][0].keys():
                columns.append(
                    Column(
                        title=row_key,
                        type=ColumnType.array,
                        array_key=key,
                        template_str="{{subitem." + row_key + "}}",
                    )
                )

    return True


class ColumnType(Enum):
    simple_cell = 0
    cell = 1
    array = 2
    dict = 3


class Column(object):
    def __init__(self, title, type, template_str, array_key=""):
        self.title = title
        self.array_key = array_key
        self.type = type
        self.template_str = template_str

    def get_template(self, input):
        # if (self.type == ColumnType.simple_cell):
        # 	return Template('<div>{{item}}</div>'.format(self.template_str)).render(item=input)

        if self.type == ColumnType.cell:
            return Template("<div>{}</div>".format(self.template_str)).render(
                item=input
            )

        if self.type == ColumnType.array:
            return Template(
                """
		<div class="list">
			{%for subitem in item."""
                + self.array_key
                + """%}
				<div class="cell">"""
                + self.template_str
                + """</div>
			{% endfor%}
		</div class="list">"""
            ).render(item=input)

        if self.type == ColumnType.dict:
            return Template(
                """
		<div class="list">
			{%for key in item.keys()%}
				<div class="cell">"""
                + self.template_str
                + """</div>
			{% endfor%}
		</div class="list">"""
            ).render(item=input)

    def set_descripton(self, desc):
        self.desc = desc