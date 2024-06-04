import asyncio
import io

import aiohttp
import pytest_asyncio

from tests.functional.settings import test_settings
from tests.functional.utils.schemas import Response


@pytest_asyncio.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(name='make_request')
def make_request():
    async def inner(
        path: str,
        method: str = 'GET',
        params: dict | None = None,
        headers: dict | None = None,
        cookies: dict | None = None,
        files: list[dict] | None = None,
        body: dict | None = None,
    ) -> Response:
        async with aiohttp.ClientSession() as session:
            data = aiohttp.FormData()
            for file in (files or []):
                data.add_field(
                    'file', io.BytesIO(file['content']), content_type=file['content_type']
                )
            url = test_settings.app_url + path
            async with session.request(
                method=method,
                url=url,
                params=params,
                headers=headers,
                cookies=cookies,
                json=body,
                data=data,
            ) as response:
                body = await response.json()
                status = response.status
        return Response(status=status, body=body)
    return inner
