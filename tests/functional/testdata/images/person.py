from http import HTTPStatus

from tests.functional.settings import test_settings
from tests.functional.utils.schemas import Request, Response

TEST_HANDS_ABOVE_HEAD_IMAGE_1_PATH = (
    test_settings.base_dir /
    "functional" /
    "testdata" /
    "images" /
    "data" /
    "test_hands_above_head_image_1.jpg"
)
with open(TEST_HANDS_ABOVE_HEAD_IMAGE_1_PATH, "rb") as file:
    TEST_HANDS_ABOVE_HEAD_IMAGE_1_REQUEST = Request(
        files=[{"content": file.read(), "content_type": "image/jpeg"}]
    )
TEST_HANDS_ABOVE_HEAD_IMAGE_1_RESPONSE = Response(
    status=HTTPStatus.OK,
    body={"confidence": 0.811675488948822},
)

TEST_HANDS_ABOVE_HEAD_IMAGE_2_PATH = (
    test_settings.base_dir /
    "functional" /
    "testdata" /
    "images" /
    "data" /
    "test_hands_above_head_image_2.jpg"
)
with open(TEST_HANDS_ABOVE_HEAD_IMAGE_2_PATH, "rb") as file:
    TEST_HANDS_ABOVE_HEAD_IMAGE_2_REQUEST = Request(
        files=[{"content": file.read(), "content_type": "image/jpeg"}]
    )
TEST_HANDS_ABOVE_HEAD_IMAGE_2_RESPONSE = Response(
    status=HTTPStatus.NOT_FOUND,
    body={"detail": "Hands above head not found."}
)

TEST_HANDS_ABOVE_HEAD_IMAGE_3_PATH = (
    test_settings.base_dir /
    "functional" /
    "testdata" /
    "images" /
    "data" /
    "test_hands_above_head_image_3.jpg"
)
with open(TEST_HANDS_ABOVE_HEAD_IMAGE_3_PATH, "rb") as file:
    TEST_HANDS_ABOVE_HEAD_IMAGE_3_REQUEST = Request(
        files=[{"content": file.read(), "content_type": "image/jpeg"}]
    )
TEST_HANDS_ABOVE_HEAD_IMAGE_3_RESPONSE = Response(
    status=HTTPStatus.OK,
    body={"confidence": 0.6746120452880859},
)

TEST_HANDS_ABOVE_HEAD_IMAGE_4_PATH = (
    test_settings.base_dir /
    "functional" /
    "testdata" /
    "images" /
    "data" /
    "test_hands_above_head_image_4.jpg"
)
with open(TEST_HANDS_ABOVE_HEAD_IMAGE_4_PATH, "rb") as file:
    TEST_HANDS_ABOVE_HEAD_IMAGE_4_REQUEST = Request(
        files=[{"content": file.read(), "content_type": "image/jpeg"}]
    )
TEST_HANDS_ABOVE_HEAD_IMAGE_4_RESPONSE = Response(
    status=HTTPStatus.NOT_FOUND,
    body={"detail": "Hands above head not found."}
)

TEST_HANDS_ABOVE_HEAD_IMAGE_5_PATH = (
    test_settings.base_dir /
    "functional" /
    "testdata" /
    "images" /
    "data" /
    "test_hands_above_head_image_5.jpg"
)
with open(TEST_HANDS_ABOVE_HEAD_IMAGE_5_PATH, "rb") as file:
    TEST_HANDS_ABOVE_HEAD_IMAGE_5_REQUEST = Request(
        files=[{"content": file.read(), "content_type": "image/jpeg"}]
    )
TEST_HANDS_ABOVE_HEAD_IMAGE_5_RESPONSE = Response(
    status=HTTPStatus.BAD_REQUEST,
    body={"detail": "Too many hands above head(-s)."}
)

TEST_HANDS_ABOVE_HEAD_IMAGE_6_PATH = (
    test_settings.base_dir /
    "functional" /
    "testdata" /
    "images" /
    "data" /
    "test_hands_above_head_image_6.jpg"
)
with open(TEST_HANDS_ABOVE_HEAD_IMAGE_6_PATH, "rb") as file:
    TEST_HANDS_ABOVE_HEAD_IMAGE_6_REQUEST = Request(
        files=[{"content": file.read(), "content_type": "image/jpeg"}]
    )
TEST_HANDS_ABOVE_HEAD_IMAGE_6_RESPONSE = Response(
    status=HTTPStatus.NOT_FOUND,
    body={"detail": "Hands above head not found."}
)

TEST_HANDS_ABOVE_HEAD_NOT_IMAGE_PATH = (
    test_settings.base_dir /
    "functional" /
    "testdata" /
    "images" /
    "data" /
    "test_hands_above_head_not_image.txt"
)
with open(TEST_HANDS_ABOVE_HEAD_NOT_IMAGE_PATH, "rb") as file:
    TEST_HANDS_ABOVE_HEAD_NOT_IMAGE_REQUEST = Request(
        files=[{"content": file.read(), "content_type": "text/plain"}]
    )
TEST_HANDS_ABOVE_HEAD_NOT_IMAGE_RESPONSE = Response(
    status=HTTPStatus.BAD_REQUEST,
    body={"detail": "Not image."}
)
