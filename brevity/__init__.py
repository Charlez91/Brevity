'''
When the package is imported, 
    __init__.py is executed automatically.

If we import something from __init__.py module then no need to write "from brevity.__init__ import x".
    writing "from brevity import x" is enough.
'''  
import os                                                                          
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)                                  
app.config['SECRET_KEY'] = '2bbc32e8acb5196b47281166ae43eeb2'            #secrets.token_hex(16)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    #supresses warning
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'                      #when a user attempts to access a login_required view without being logged in,
                                                        #   Flask-Login will flash a message and redirect them to the log in view. 
login_manager.login_message_category = 'info'

mail = Mail(app)

from brevity import routes          
'''
route imports app. So we first initialize app then import routes.
So that we can avoid circular import.
'''
   
