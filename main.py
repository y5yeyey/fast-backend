"""Main application"""

import logging
from fastapi import FastAPI
from core.routers import router

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    """Entrypoint of a FastAPI service"""
    logger.info("bootstrapped service")
    return {"message": "Hello fast-backend Applications!"}
