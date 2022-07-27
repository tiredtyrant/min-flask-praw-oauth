# min-flask-praw-oauth
Minimal OAuth example with Praw and Flask

* Create venv: `$ python -m venv path/to/venv`
* Activate venv: `$ source path/to/venv/bin/activate`
* Install requirements.txt: `$ python -m pip install -r requirements.txt`
* Setup FLASK_APP: `$ export FLASK_APP=main.py`
* Create a [web app](https://www.reddit.com/prefs/apps) on Reddit, and input its data in `praw.ini` (follow [PRAW guidelines](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html) for `user_agent`)
* Generate a random key for `secret_key` in `config.json`. This key will be used by Flask to encrypt session data.
* Run development server: `$ flask run`.
* Visit `127.0.0.1:5000` on your browser.
