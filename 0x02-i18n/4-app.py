#!/usr/bin/env python3
"""Flask app module"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Reperesent babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    queries = request.query_string.decode('utf-8').split('&')
    query_t = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries
    ))
    if 'locale' in query_t:
        if query_t['locale'] in app.config["LANGUAGES"]:
            return query_t['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
