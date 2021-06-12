from front import export 
from front.tags import *
from front.cdn import bootstrap
from front.document import document

def metadata():
    meta(charset="UTF-8")
    meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no")

def navbar():
    with nav(cls="navbar navbar-expand-lg navbar-dark bg-dark").add(ol(cls="navbar-nav me-auto mb-2 mb-lg-0")):
        for i in ['home', 'about', 'contact']:
            page = "index.html" if  i == 'home' else f"{i}.html"
            li(a(i.title(), href=f'{page}', cls='nav-link'), cls="nav-item")

def container():
    with div(id="dataContainer", cls="container"):
        with div(cls="row justify-content-center").add(div(cls="col-4")):
            h1("No items found!", cls="text-center")

    with div(cls="container").add(div(cls="row justify-content-center")).add(div(cls="col-4 text-center")):
        button("Load Data", onclick="app.load_data()", cls="btn btn-primary")

@export
def index():
    doc = document(title='Python Frontend')

    with doc.head:
        metadata()
        bootstrap()
        module("app")

    with doc:
        navbar()
        container()

    return doc

@export
def about():
    doc = document(title='Python Frontend')

    with doc.head:
        metadata()
        bootstrap()
        module("app")

    with doc:
        navbar()
        container()

    return doc

@export
def contact():
    doc = document(title='Python Frontend')

    with doc.head:
        metadata()
        bootstrap()
        module("app")

    with doc:
        navbar()
        container()

    return doc