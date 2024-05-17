from flask import Flask
from src.main.routes.routes import single_asset_route_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(single_asset_route_bp)
