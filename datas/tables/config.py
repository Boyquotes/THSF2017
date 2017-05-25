'''
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
'''

# Flask config.py
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/myDataGoliath"
SQLALCHEMY_TRACK_MODIFICATIONS = True
