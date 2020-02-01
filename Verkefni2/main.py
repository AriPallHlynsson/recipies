from markdown2 import markdown

with open('content/turkish-pide.md', 'r') as file:
    parsed_md = markdown(file.read(), extras=['metadata'])


print('Metadata: ', parsed_md.metadata)
print('Content: ', parsed_md) 
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('main', 'templates'))
test_template = env.get_template('test.html')

data = {
    'content': parsed_md,
    'title': parsed_md.metadata['title'],
    'date': parsed_md.metadata['date']
}

print(test_template.render(post=data))