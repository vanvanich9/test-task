from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.ping import router as ping_router
from api.v1.images.persons import router as images_persons_router
from core.config import settings

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    debug=settings.debug,
)

app.include_router(router=ping_router, prefix='/api/ping', tags=['Common'])
app.include_router(
    router=images_persons_router,
    prefix='/api/v1/images/persons',
    tags=['Images', 'Person images'],
)
