from enum import Enum
from jinja2 import Template


class ColumnType(Enum):
    simple_cell = 0
    cell = 1
    array = 2
    dict_keys = 3


class Column(object):
    def __init__(self, title, type, template_str, array_key=''):
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
			{%for subitem in item.""" + self.array_key +  """%}
				<div class="cell">"""+
					self.template_str + 
				"""</div>
			{% endfor%}
		</div class="list">"""
            ).render(item=input)

        
        # if self.type == ColumnType.key_value_dict:
        #     return Template(
        #         """
		# <div class="list">
		# 	{%for subitem in item.keys()%}
		# 		<div class="cell">"""+
		# 			self.template_str + 
		# 		"""</div>
		# 	{% endfor%}
		# </div class="list">""")
        

