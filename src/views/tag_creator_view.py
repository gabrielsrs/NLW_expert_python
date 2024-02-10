from .http_types.http_requests import HttpRequest
from ..views.http_types.http_responses import HttpResponse

class TagCreatorView:
    """
        Responsibility for interact with HTTP
    """
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        print(product_code)

        return HttpResponse(status_code=200, body={})
