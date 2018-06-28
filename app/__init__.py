from flask import Flask
<<<<<<< HEAD
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import views
=======

app = Flask(__name__)
from app import views
>>>>>>> 2a7ff4b1c703d4905ad846630aeab3621467d0fa
