from fastapi import FastAPI, APIRouter

from app.items import items_view

app = FastAPI()

main_router = APIRouter()
main_router.include_router(items_view.router)


app.include_router(main_router)
