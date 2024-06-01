from http import HTTPStatus

from tests.functional.utils.schemas import Response

PING_RESPONSE = Response(status=HTTPStatus.OK, body={'ping': 'pong!'})
