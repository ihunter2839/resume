# Jinja template resume generator

This is a simple program that uses Python / the Jinja template engine and json data to produce easily editable resume documents. I was tired of using programs like word or illustrator and wanted a pure HTML, CSS, and python solution instead. 

The main python file is found under
```
web/generateResume.py
```

The first argument is a path to a folder containing a Jinja template name ```template``` and any associated static files (css, images)

The second argument is a path to the json data object to populate the template

The final argument is the name of the output file

Example
```
python generateResume.py /jinjaTemplates/resume3/ jsonData/hardware.json resumeOut.html
```