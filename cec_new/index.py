from jinja2 import Template
import os
import json



with open('raut.json', 'rb') as json_file:
    data = {
        'autors_info': list(filter(lambda item : len(item['ref_authors']), json.load(json_file)))
    }
    html = open('template.html', encoding='utf-8').read()
    template = Template(html)
    
    with open('output.html', 'w', encoding='utf-8') as output:
        output.write(template.render(**data))

