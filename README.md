## My attempt at a pure python frontend


``` python
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python -m front

[I 210613 01:57:09 server:335] Serving on http://127.0.0.1:8000
[I 210613 01:57:09 handlers:62] Start watching changes
[I 210613 01:57:09 handlers:64] Start detecting changes
```

HTML is generated using [**dominate**](https://github.com/Knio/dominate).

Javascript is generated using [**transcrypt**](https://github.com/QQuick/Transcrypt).

Server and file watch with [**livereload**](https://github.com/lepture/python-livereload).

# DEMO
