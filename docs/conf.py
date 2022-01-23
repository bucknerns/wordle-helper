import sphinx_rtd_theme

name = "wordle-helper"
project = "Wordle Helper"
copyright = "2019, None"
author = "None"
version = "0.0.1"
release = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_autodoc_annotation",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram"]

napoleon_use_param = True
napoleon_use_admonition_for_examples = True
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = None
exclude_patterns = []
pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = "{0}doc".format(name)
latex_elements = {}

latex_documents = [(
    master_doc, "{0}.tex".format(name), "{0} Documentation".format(name),
    author, "manual")]

man_pages = [(
    master_doc, name, "{0} Documentation".format(name), [author], 1)]

texinfo_documents = [(
    master_doc, name, "{0} Documentation".format(name),
    author, name, "One line description of project.", "Miscellaneous")]

intersphinx_mapping = {"https://docs.python.org/": None}
default_role = "any"
todo_include_todos = True
rst_prolog = (
    ".. _requests.Response: http://docs.python-requests.org/en/master/api/"
    "#requests.Response\n"
    ".. _requests.Request: http://docs.python-requests.org/en/master/api/"
    "#requests.Request\n"
    ".. _list: https://docs.python.org/2.7/tutorial/datastructures.html")
html_static_path = ['_static']
