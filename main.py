from fastapi import FastAPI

from routers.instagram import router as instagram_router


app = FastAPI()

app.include_router(instagram_router)
