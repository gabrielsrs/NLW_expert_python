from ..views.http_types.http_responses import HttpResponse

def handle_error(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "errors": [
                {
                    "title": "Server Error",
                    "detail": str(error)
                }
            ]
        }
    )
