from flask import Flask, Blueprint
from flask_debugtoolbar import DebugToolbarExtension
from controller.home import *
from controller.about import *
from controller.post import *
from controller.contact import *
from admin.admin import *
from controller.login import *

app = Flask(__name__)


app.secret_key = '1'
app.debug = True

toolbar = DebugToolbarExtension(app)


app.register_blueprint(home, url_prefix='/' )
app.register_blueprint(about, url_prefix='/about')
app.register_blueprint(post, url_prefix='/post')
app.register_blueprint(contact, url_prefix='/contact')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(login, url_prefix='/')


if __name__ == '__main__':
    app.run()