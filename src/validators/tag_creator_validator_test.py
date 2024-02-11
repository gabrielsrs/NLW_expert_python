from .tag_creator_validator import tag_creator_validator
from ..errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    """
        Correct format
    """
    mock_request = MockRequest(json={ "product_code": "Tfu498zP9f2R2XzL91awY684b18X6DcR" })
    tag_creator_validator(mock_request)


def test_tag_creator_validator_with_value_error():
    """
        Wrong value type
    """
    mock_request = MockRequest(json={ "product_code": 97028480905050635628169426720359 })

    try:
        tag_creator_validator(mock_request)
        assert False

    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)

def test_tag_creator_validator_with_key_error():
    """
        Wrong key description
    """
    mock_request = MockRequest(json={ "random_key": "Tfu498zP9f2R2XzL91awY684b18X6DcR" })

    try:
        tag_creator_validator(mock_request)
        assert False

    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
