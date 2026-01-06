import nbformat
from nbconvert import PythonExporter

with open("data_clean.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

py_exporter = PythonExporter()
body, _ = py_exporter.from_notebook_node(nb)

with open("data_clean.py", "w") as f:
    f.write(body)
