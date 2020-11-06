# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Create flask app
from flask import Flask
app = Flask(__name__)

# Database connection
from database import init_db
db = init_db(app)

# Setup serialization/deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

# Controller registration
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
