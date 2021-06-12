from os import O_NONBLOCK
from front import export 
from front.tags import *
from front.cdn import bootstrap
from front.document import document

@export
def index():
    doc = document(title='Python Frontend')

    with doc.head:
        bootstrap()
        module("app")

    with doc:
        with div(id='header').add(ol()):
            for i in ['home', 'about', 'contact']:
                li(a(i.title(), href='/%s.html' % i))

        button("Click Me", onclick="app.action()")

    return doc