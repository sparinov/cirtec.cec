from jinja2 import Template
import os
import json


with open('cec_new/raut.json', 'rb') as json_file:
    data = {
        'autors_info': list(filter(lambda item : len(item['ref_authors']), json.load(json_file)))
    }
    html = open('cec_new/template 2.html', encoding='utf-8').read()
    template = Template(html)
    
    with open('cec_new/output.html', 'w', encoding='utf-8') as output:
        output.write(template.render(**data))

