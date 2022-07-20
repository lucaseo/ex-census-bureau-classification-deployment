# Put the code for your API here.

from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

from .routers.hello_world import router as router_hello_world

def get_application():
    app = FastAPI(title="census_inference_api",
                  version="v0.1",
                  description="Inference API for census dataset (Udacity Project)")
    app.include_router(router_hello_world, prefix='?', tags=['?'])
    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_credentials=False,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )
    return app

app = get_application()
