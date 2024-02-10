from flask import Blueprint

tags_routes_bp = Blueprint('tag_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tags():
    pass
