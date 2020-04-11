from nbconvert.exporters import HTMLExporter
html_exporter = HTMLExporter()

## Create an HTML report from a Jupyter notebook
contents = html_exporter.from_filename('Exercise2pt5.ipynb')[0]

from pathlib import Path

Path('Exercise2pt5.html').write_text(contents)