from ..views.http_types.http_responses import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse (
            status_code=error.status_code,
            body={
                "errors": [
                    {
                        "detail": error.message,
                        "title": error.name
                    }
                ]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [
                {
                    "detail": str(error),
                    "title": "Server Error"
                }
            ]
        }
    )
