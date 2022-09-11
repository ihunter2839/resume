from jinja2 import Environment, FileSystemLoader
import sys
import json
import os

if __name__ == "__main__":

	help_string = "generateResume.py path/to/template path/to/jsonData output.html"

	if len(sys.argv) < 4 or sys.argv[1] in ["--h", "--help"]:
		print(help_string)

	else:
		env = Environment( loader=FileSystemLoader(sys.argv[1]) )

		context = json.loads(open(sys.argv[2]).read())

		context["path"] = sys.argv[1]

		template = env.get_template('template.html')

		out = open(sys.argv[3], 'w')

		out.write(template.render(context))



