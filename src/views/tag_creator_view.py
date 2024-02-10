from .http_types.http_requests import HttpRequest
from ..views.http_types.http_responses import HttpResponse
from ..controllers.tag_creator_controller import  TagCreateController

class TagCreatorView:
    """
        Responsibility for interact with HTTP
    """
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreateController()

        body = http_request.body
        product_code = body["product_code"]

        formatted_response = tag_creator_controller.create(product_code)

        return HttpResponse(status_code=200, body=formatted_response)
