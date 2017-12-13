from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


def create_app():
    app = Flask(__name__)

    # berguna untuk membuat flask mengambil perubahan2 juga pada html
    # hanya digunakan untuk development bukan untuk production
    #  app.config['DEBUG'] = True

    # config diambil dari python file settings.py
    app.config.from_pyfile('settings.py')
    db = SQLAlchemy(app)

    class Page(db.Model):
        __tablename__ = 'page'
        id = Column(Integer, primary_key=True)
        contents = Column(String)

    db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html', TITLE='Index Learning', CONTENT='''
            <div class="starter-template">
                <h1>Welcome to my page !!</h1>
                <p class="lead">Learning by Doing !!!</p>
            </div>
        ''')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Index Learning')

    @app.route('/testdb')
    def testdb():
        #import psycopg2

        #con = psycopg2.connect('dbname=flask01 user=devuser password=devpassword host=postgres')
        #cur = con.cursor()
        #cur.execute('select * from page;')

        #id, title = cur.fetchone()
        #con.close()
        #return 'ID:{}, Title:{}'.format(id, title)

        page = Page.query.filter_by(id=1).first()
        return render_template('index.html', TITLE='Simply Blog', CONTENT=page.contents)

    return app

