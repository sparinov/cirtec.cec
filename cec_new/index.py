from jinja2 import Template
import os
import json
from templates.raut import RautTable


with open("cec_new/raut.json", "rb") as json_file:
    data = list(filter(lambda item: len(item["ref_authors"]), json.load(json_file)))
    html = open("cec_new/template 3.html", encoding="utf-8").read()
    template = Template(html)
    table = RautTable()

    with open("cec_new/output.html", "w", encoding="utf-8") as output:
        output.write(template.render(data=data, table=table))

