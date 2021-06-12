from pathlib import Path

def export(func):
    filename = f"build/{func.__name__}.html"

    path = Path(filename).absolute()
    path.parent.mkdir(parents=True, exist_ok=True)

    dom = func()
    with open(path, 'w') as htmlfile:
        htmlfile.write(dom.render(pretty=True))