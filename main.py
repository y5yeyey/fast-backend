from fastapi import Depends, FastAPI
from routers import router

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello fast-backend Applications!"}
