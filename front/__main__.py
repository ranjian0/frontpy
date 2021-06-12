import os
import sys
from pathlib import Path

def run():
    workdir = Path(os.curdir).absolute()

    build_default_files(workdir)

    # -- start the server
    os.system('python -m http.server --directory build')

def build_default_files(workdir):
    """
    index.py to generate the html files
    app.py to generate the javascript
    """
    indexfile = workdir / 'index.py'
    os.system(f'python {str(indexfile)}')

    appfile = workdir / 'app.py'
    os.system(f'python -m transcrypt -od {workdir / "build" / "js"} {str(appfile)}')


if __name__ == "__main__":
    run()