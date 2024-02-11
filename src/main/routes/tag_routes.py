from flask import Blueprint, request, jsonify
from ...views.http_types.http_requests import HttpRequest
from ...views.tag_creator_view import TagCreatorView
from ...errors.error_handler import handle_error
from ...validators.tag_creator_validator import tag_creator_validator

tags_routes_bp = Blueprint('tag_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tags():
    response = None
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()
        http_requests = HttpRequest(body=request.json)

        response = tag_creator_view.validate_and_create(http_requests)

    except Exception as exception:
        response = handle_error(exception)

    return jsonify(response.body), response.status_code
