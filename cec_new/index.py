from jinja2 import Template
from enum import Enum
import os
import json
import requests

urls = {}
urls["tore"] = "http://cirtec.ranepa.ru/cirtec/top/ref_bundles/"
urls["taur"] = "http://cirtec.ranepa.ru/cirtec/top/ref_authors/"

urls["raut"] = "http://cirtec.ranepa.ru/cirtec/pubs/ref_authors/"

urls["frap"] = "http://cirtec.ranepa.ru/cirtec/frags/publications/"
urls["foci"] = "http://cirtec.ranepa.ru/cirtec/frags/cocitauthors/"
urls["cauc"] = "http://cirtec.ranepa.ru/cirtec/frags/cocitauthors/cocitauthors/"
urls["rebu"] = "http://cirtec.ranepa.ru/cirtec/ref_bund4ngramm_tops/?topn=100"
urls["aubu"] = "http://cirtec.ranepa.ru/cirtec/ref_auth4ngramm_tops/"
urls["febu"] = "http://cirtec.ranepa.ru/cirtec/frags/ref_bundles/"
urls["refa"] = "http://cirtec.ranepa.ru/cirtec/frags/ref_authors/"
urls["popu"] = "http://cirtec.ranepa.ru/cirtec/pos_neg/pubs/"
urls["pobu"] = "http://cirtec.ranepa.ru/cirtec/pos_neg/ref_bundles/"
urls["paut"] = "http://cirtec.ranepa.ru/cirtec/pos_neg/ref_authors/"
urls["toco"] = "http://cirtec.ranepa.ru/cirtec/frags/topics/ngramms/"
urls["taut"] = "http://cirtec.ranepa.ru/cirtec/frags/topics/cocitauthors/"
urls["fato"] = "http://cirtec.ranepa.ru/cirtec/frags/ngramms/topics/"
urls["nagu"] = "http://cirtec.ranepa.ru/cirtec/frags/ngramms/cocitauthors/"
urls["foat"] = "http://cirtec.ranepa.ru/cirtec/frags/cocitauthors/topics/"
urls["fano"] = "http://cirtec.ranepa.ru/cirtec/frags/cocitauthors/ngramms/"
urls["frat"] = "http://cirtec.ranepa.ru/cirtec/frags/topics/"
urls["legn"] = "http://cirtec.ranepa.ru/cirtec/frags/ngramms/?ltype=lemmas"
urls["copu"] = "http://cirtec.ranepa.ru/cirtec/top/cocitauthors/publications/"
urls["pung"] = "http://cirtec.ranepa.ru/cirtec/top/ngramms/publications/?ltype=lemmas"
urls["topu"] = "http://cirtec.ranepa.ru/cirtec/top/topics/publications/"
urls["tabu"] = "http://cirtec.ranepa.ru/cirtec/pos_neg/ref_bundles/"
urls["tona"] = "http://cirtec.ranepa.ru/cirtec/pos_neg/ref_authors/"
urls["tang"] = "http://cirtec.ranepa.ru/cirtec/pos_neg/ngramms/"
urls["tato"] = "http://cirtec.ranepa.ru/cirtec/pos_neg/topics/"
urls["taco"] = "http://cirtec.ranepa.ru/cirtec/pos_neg/cocitauthors/"
urls["tant"] = "http://cirtec.ranepa.ru/cirtec/frags/pos_neg/contexts/"


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

def initColumns(columns, key, object):
    row_type = type(object[key])
    if row_type == str or row_type == int:
        columns.append(
            Column(
                title=key, type=ColumnType.cell, template_str="{{item." + key + "}}"
            )
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
        first_array_row = type(first_row[key][0])

        if first_array_row == str or first_array_row == int:
            columns.append(
                Column(title=key, type=ColumnType.array, template_str="{{subitem}}")
            )
        if first_array_row == dict:
            for row_key in first_row[key].keys():
                columns.append(
                    Column(
                        title=key,
                        type=ColumnType.array,
                        template_str="{{subitem" + row_key + "}}",
                    )
                )

    return True



for url_key in urls:
    request = requests.get(urls[url_key])
    print("{key} : {code}".format(key=url_key, code=request.status_code))

    data = request.json()

    columns = []
    jinja2_args = {"data": data, "columns": columns}

    # по первой строчке создаём схему

    first_row = {}
    if type(data) == list:
        jinja2_args["data_type"] = 1
        first_row = data[0]

    if type(data) == dict:
        jinja2_args["data_type"] = 2
        jinja2_args["data_keys"] = list(data.keys())
        first_row = data[list(data.keys())[0]]

    for key in first_row.keys():
        row_type = type(first_row[key])
        if row_type == str or row_type == int:
            columns.append(
                Column(
                    title=key, type=ColumnType.cell, template_str="{{item." + key + "}}"
                )
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
            first_array_row = type(first_row[key][0])

            if row_type == str or row_type == int:
                columns.append(
                    Column(title=key, type=ColumnType.array, template_str="{{subitem}}")
                )
            if row_type == dict:
                for row_key in first_row[key].keys():
                    columns.append(
                        Column(
                            title=key,
                            type=ColumnType.array,
                            template_str="{{subitem" + row_key + "}}",
                        )
                    )

    html = open("cec_new/template 4.html", encoding="utf-8").read()
    template = Template(html)

    with open(
        "cec_new/output/{}.html".format(url_key), "w", encoding="utf-8"
    ) as output:
        output.write(template.render(**jinja2_args))

