import os
from pathlib import Path
from livereload import Server
from livereload.server import shell


if __name__ == "__main__":
    workdir = Path(os.curdir).absolute()

    appfile =  workdir / 'app.py'
    indexfile = workdir / 'index.py'

    server = Server()
    server.watch(str(indexfile), shell(f'python {indexfile}'))
    server.watch(str(appfile), shell(f'python -m transcrypt -od {workdir / "build" / "js"} {str(appfile)}'))
    server.serve(root=f'{str(workdir / "build")}', port=8000)