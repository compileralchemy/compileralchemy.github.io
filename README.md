To build the site


In venv

```
python -m pip install requirements.txt

python static.py # python static.py --server if you want live reload.
                 # this can be combined with VSCode live reload extension, add the url to have some realtime feel.
```


Serving

```
python -m http.server --dir ./docs 8000