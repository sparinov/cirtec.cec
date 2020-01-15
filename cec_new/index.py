from jinja2 import Template
import os
import json
from templates.aubu import AubuTable
from templates.cauc import CaucTable
from templates.febu import FebuTable


from templates.paut import PautTable
from templates.pobu import PobuTable
from templates.popu import PopuTable
from templates.raut import RautTable
from templates.rebu import RebuTable
from templates.refa import RefaTable
from templates.tabu import TabuTable
from templates.taco import TacoTable
from templates.tang import TangTable
from templates.tant import TantTable
from templates.tato import TatoTable
from templates.taur import TaurTable
from templates.topu import TopuTable
from templates.tore import ToreTable

#  PopuTable(),
tables = [ AubuTable(), CaucTable(), FebuTable(), PautTable(), PobuTable(), RautTable(), RebuTable(), RefaTable(), TabuTable(), TacoTable(), TangTable(), TantTable(), TatoTable(), TaurTable(), TopuTable(), ToreTable()]

for table in tables:
    with open("cec/json/{}.json".format(table.name), "rb") as json_file:
        data = list(json.load(json_file))
        html = open("cec_new/template 3.html", encoding="utf-8").read()
        template = Template(html)
        print(table.name)

        with open("cec_new/output/{}.html".format(table.name), "w", encoding="utf-8") as output:
            output.write(template.render(data=data, table=table))

