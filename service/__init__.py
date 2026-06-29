from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Enable Talisman for security headers (disable HTTPS enforcement for testing)
talisman = Talisman(app, force_https=False)
