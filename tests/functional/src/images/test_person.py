from http import HTTPStatus

import pytest

from tests.functional.testdata.images.person import (
    TEST_HANDS_ABOVE_HEAD_IMAGE_1_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_1_RESPONSE,
    TEST_HANDS_ABOVE_HEAD_IMAGE_2_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_2_RESPONSE,
    TEST_HANDS_ABOVE_HEAD_IMAGE_3_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_3_RESPONSE,
    TEST_HANDS_ABOVE_HEAD_IMAGE_4_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_4_RESPONSE,
    TEST_HANDS_ABOVE_HEAD_IMAGE_5_REQUEST,
    TEST_HANDS_ABOVE_HEAD_IMAGE_5_RESPONSE,
    TEST_HANDS_ABOVE_HEAD_NOT_IMAGE_REQUEST,
    TEST_HANDS_ABOVE_HEAD_NOT_IMAGE_RESPONSE)
from tests.functional.utils.schemas import Request, Response

MAX_ERROR = 0.0001


@pytest.mark.asyncio()
@pytest.mark.parametrize("request_data, expected_response", [
    (TEST_HANDS_ABOVE_HEAD_IMAGE_1_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_1_RESPONSE),
    (TEST_HANDS_ABOVE_HEAD_IMAGE_2_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_2_RESPONSE),
    (TEST_HANDS_ABOVE_HEAD_IMAGE_3_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_3_RESPONSE),
    (TEST_HANDS_ABOVE_HEAD_IMAGE_4_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_4_RESPONSE),
    (TEST_HANDS_ABOVE_HEAD_IMAGE_5_REQUEST, TEST_HANDS_ABOVE_HEAD_IMAGE_5_RESPONSE),
    (TEST_HANDS_ABOVE_HEAD_NOT_IMAGE_REQUEST, TEST_HANDS_ABOVE_HEAD_NOT_IMAGE_RESPONSE),
])
async def test_hands_above_head(make_request, request_data: Request, expected_response: Response):
    response: Response = await make_request(
        '/api/v1/images/persons/hands-above-head', method='POST', **request_data.model_dump()
    )

    assert response.status == expected_response.status
    if response.status == HTTPStatus.OK:
        assert abs(response.body['confidence'] - expected_response.body['confidence']) <= MAX_ERROR
    else:
        assert response.body['detail'] == expected_response.body['detail']
