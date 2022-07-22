# uvicorn main:app --host 0.0.0.0 --port 80 --reload

import uvicorn
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

from api_src.routers.hello_world import router as router_hello_world
# from .routers.hello_world import router as router_hello_world

def get_application():
    app = FastAPI(title="census_inference_api",
                  version="v0.1",
                  description="Inference API for census dataset (Udacity Project)")
    app.include_router(router_hello_world)
    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_credentials=False,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )
    return app

app = get_application()


if __name__ == "__main__":
    uvicorn.run(app="app:app",
                host="127.0.0.1",
                port=8000,
                reload=True)

