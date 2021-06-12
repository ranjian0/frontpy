from front.tags import link, script

def bootstrap_5():
    link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css')
    script(src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js')

def bootstrap_4():
    link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css')
    script(src='https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js')

# default is latest
bootstrap = bootstrap_5
