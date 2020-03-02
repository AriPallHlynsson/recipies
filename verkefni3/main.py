
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

with open('content/turkish-pide.md', 'r') as file:
    parsed_md = markdown(file.read(), extras=['metadata'])

    env = Environment(loader=PackageLoader('main', 'templates'))
    test_template = env.get_template('test.html')

    data = {
    'hi': parsed_md.metadata['hi'],
    'content': parsed_md,
    'title': parsed_md.metadata['title'],
    'date': parsed_md.metadata['date'],
    'title1': parsed_md.metadata['title1'],
    'title2': parsed_md.metadata['title2'],
    'title3': parsed_md.metadata['title3'],
    'title4': parsed_md.metadata['title4'],
    'title5': parsed_md.metadata['title5'],
    'title6': parsed_md.metadata['title6'],
  
    }

    print(test_template.render(post=data))