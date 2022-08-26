from fastapi import APIRouter

router = APIRouter()


@router.get(path="/items")
def get_items():
    return {
        "message": "hello"
    }
