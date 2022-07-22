from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def say_hello_world():
    return JSONResponse(
        content={
            "msg": "Welcome to Census ML Inference API"
        }
    )