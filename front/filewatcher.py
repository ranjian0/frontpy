import os
import time
import threading
from pathlib import Path

class WatchFile:

    def __init__(self, file, callback=lambda : None):
        self.file = Path(file).absolute()
        self.modified_callback = callback

        self.thread = threading.Thread(target=self.watch)
        self.thread.start()
        self.thread.join()

    def timestamp(self):
        return os.path.getmtime(str(self.file))

    def watch(self):
        before = self.timestamp()

        while True:
            after = self.timestamp()
            time.sleep(2)
            
            if os.path.getmtime(self.file) != before:
                self.modified_callback()
                print(f"{self.file} Modified")

            before = after
