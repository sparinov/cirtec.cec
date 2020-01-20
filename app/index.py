import json
import os
from enum import Enum

import requests
from jinja2 import Template
from lxml import etree

from app.core import initColumns

parser = etree.XMLParser
xml = {}

doc = etree.parse("after_table_edited.xml")
items = [*doc.findall("section/item"), *doc.findall("section/*/item")]
# items = [*doc.findall("section/item")][:1]
print(len(items))

for item in items:
    url_key = item.attrib["id"]
    print("Начинаем обработку элемента с id = {url}".format(url=url_key))

    url = item.attrib["source"] # там лежит уже готовый url
    # data = {}
    data = requests.get(url).json()
    print("Получен ответ с url {key} - {type}".format(key=url_key, type=type(data)))

    title = item.find("title").findtext("ru")
    desc = item.find("desc").find("ru")
    expl = item.find("expl").find("ru")

    columns = []
    jinja2_args = {
        "data": data,
        "columns": columns,
        "title": title,
        "desc": etree.tostring(desc, encoding="unicode"),
        "expl": etree.tostring(expl, encoding="unicode"),
    }

    # Инициализация колонок табилцы
    first_row = {}
    if type(data) == list:
        jinja2_args["data_type"] = 1
        first_row = data[0]

    elif type(data) == dict:
        jinja2_args["data_type"] = 2
        jinja2_args["data_keys"] = list(data.keys())
        first_row = data[list(data.keys())[0]]

    for key in first_row.keys():
        initColumns(columns=columns, key=key, object=first_row)

    legend = item.find("legend") # вставляем в каждую колонку данные о легенде
    if (legend is not None):
        for element in list(legend.find("ru").getiterator()):
            if "title" not in element.attrib:
                continue

            title = element.attrib["title"]
            cols = [col for col in columns if col.title == title]
            if (len(cols) == 1):
                cols[0].desc = element.text


    html = open("app/template 4.html", encoding="utf-8").read()
    template = Template(html)

    with open("output/{}.html".format(url_key), "w", encoding="utf-8") as output:
        output.write(template.render(**jinja2_args))
    with open("saved_json/{}.json".format(url_key), "w", encoding="utf-8") as output:
        output.write(json.dumps(data, indent=4))
        
