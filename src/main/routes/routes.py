from flask import Blueprint, request, jsonify

# Import_adapters
from src.main.adapters.request_adapter import request_adapter

# Import_composers
from src.main.composers.single_asset_composer import single_asset_composer

single_asset_route_bp = Blueprint("single_asset_routes", __name__)

@single_asset_route_bp.route("/singleAsset", methods=["GET"])
def get_price():
    http_response = request_adapter(request, single_asset_composer())
    return jsonify(http_response.body), http_response.status_code
