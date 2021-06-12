import os
import sys
from pathlib import Path

from .filewatcher import WatchFile

def run():
    workdir = Path(os.curdir).absolute()
    builddir = workdir / 'build'

    # indexfile = workdir / 'index.py'
    # watcheri = WatchFile(str(indexfile), callback=lambda : os.system(f'python {str(indexfile)}'))

    appfile = workdir / 'app.py'
    watchera = WatchFile(str(appfile), callback=lambda : os.system(f'python -m transcrypt -od {builddir / "js"} {str(appfile)}'))
    

if __name__ == "__main__":
    if len(sys.argv) == 1:
        action = "build"
    else:
        action = sys.argv[1]

    if action.lower() == 'run':
        run()
    else:
        print(f"Unrecognized argument '{action}', use one of [run]")