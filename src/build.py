import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader = FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

for filename in os.listdir('templates/'):
    if filename.endswith(".html"):
        template = env.get_template(filename)
        output = template.render(the="variables", go="here")
        with open(os.path.join("output", filename), "wt") as f:
            f.write(output)

