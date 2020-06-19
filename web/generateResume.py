from jinja2 import Environment, FileSystemLoader
import sys
import json

if __name__ == "__main__":

	fsl = FileSystemLoader('./jinjaTemplates')

	env = Environment(loader=fsl)

	context = json.loads(open(sys.argv[1]).read())

	template = env.get_template('test.html')

	out = open(sys.argv[2], 'w')

	out.write(template.render(context))



