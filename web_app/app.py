from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # berguna untuk membuat flask mengambil perubahan2 juga pada html
    # hanya digunakan untuk development bukan untuk production
    #app.config['DEBUG'] = True

    # config diambil dari python file settings.py
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return render_template('index.html', TITLE='Index Learning')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Index Learning')

    return app

