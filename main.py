from flask import Flask, render_template, session, request, redirect, url_for
import praw
import json

CONFIG_FILE = "config.json"

with open(CONFIG_FILE) as cfg:
    config = json.load(cfg)

app = Flask(__name__)

app.secret_key = config['app']['secret_key']

rGetUrl = praw.Reddit(site_name="app_config")

@app.route('/')
def mainview():
    if 'refresh_token' in session:
        rGetAuthorized = praw.Reddit(site_name="app_config", refresh_token = session['refresh_token'])
        user = rGetAuthorized.user.me()
        return render_template('mainview.html', user=user)
    elif 'code' in session:
        rGetRefreshToken = praw.Reddit(site_name="app_config")
        session['refresh_token'] = rGetRefreshToken.auth.authorize(session['code'])
        user = rGetRefreshToken.user.me()
        return render_template('mainview.html', user=user)
    else:
        auth_url = rGetUrl.auth.url(scopes=["identity"], state="...", duration="permanent")
        return render_template('mainview.html', auth_url=auth_url)

@app.route('/redir')
def redir():
    key = request.args.get('code')
    state = request.args.get('state')
    session['code'] = key
    session['state'] = state
    return redirect(url_for('mainview'))

@app.route('/logoff')
def logoff():
    session.pop('code', None)
    session.pop('refresh_token', None)
    session.pop('state',None)
    return redirect(url_for('mainview'))

if __name__ == '__main__':
    app.run(port=5000)