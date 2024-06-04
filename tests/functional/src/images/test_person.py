import pytest

from tests.functional.testdata.images.person import (
    TEST_HANDS_ABOVE_HEAD_IMAGE_1_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_1_RESPONSE,
    TEST_HANDS_ABOVE_HEAD_IMAGE_2_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_2_RESPONSE,
    TEST_HANDS_ABOVE_HEAD_IMAGE_3_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_3_RESPONSE,
    TEST_HANDS_ABOVE_HEAD_IMAGE_4_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_4_RESPONSE)
from tests.functional.utils.schemas import Request, Response

MAX_ERROR = 0.0001


@pytest.mark.asyncio()
@pytest.mark.parametrize("request_data, expected_response", [
    (TEST_HANDS_ABOVE_HEAD_IMAGE_1_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_1_RESPONSE),
    (TEST_HANDS_ABOVE_HEAD_IMAGE_2_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_2_RESPONSE),
    (TEST_HANDS_ABOVE_HEAD_IMAGE_3_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_3_RESPONSE),
    (TEST_HANDS_ABOVE_HEAD_IMAGE_4_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_4_RESPONSE),
])
async def test_hands_above_head(make_request, request_data: Request, expected_response: Response):
    response: Response = await make_request(
        '/api/v1/images/persons/hands-above-head', method='POST', **request_data.model_dump()
    )

    assert response.status == expected_response.status
    assert response.body['number'] == expected_response.body['number']

    for confidence_value in response.body['confidence']:
        assert min(
            abs(another_confidence_value - confidence_value)
            for another_confidence_value in expected_response.body['confidence']
        ) <= MAX_ERROR

    for confidence_value in expected_response.body['confidence']:
        assert min(
            abs(another_confidence_value - confidence_value)
            for another_confidence_value in response.body['confidence']
        ) <= MAX_ERROR
