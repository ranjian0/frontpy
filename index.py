from front import export 
from front.tags import *
from front.cdn import bootstrap
from front.document import document

def navbar():
    with nav(cls="navbar navbar-expand-lg navbar-dark bg-dark").add(ol(cls="navbar-nav me-auto mb-2 mb-lg-0")):
        for i in ['home', 'about', 'contact']:
            page = "index.html" if  i == 'home' else f"{i}.html"
            li(a(i.title(), href=f'{page}', cls='nav-link'), cls="nav-item")



@export
def index():
    doc = document(title='Python Frontend')

    with doc.head:
        bootstrap()
        module("app")

    with doc:
        navbar()
        button("Click Me", onclick="app.action()", cls="btn btn-primary")

    return doc

@export
def about():
    doc = document(title='Python Frontend')

    with doc.head:
        bootstrap()
        module("app")

    with doc:
        navbar()
        button("Click Me", onclick="app.action()", cls="btn btn-primary")

    return doc

@export
def contact():
    doc = document(title='Python Frontend')

    with doc.head:
        bootstrap()
        module("app")

    with doc:
        navbar()
        button("Click Me", onclick="app.action()", cls="btn btn-primary")

    return doc