import asyncio
import logging
from contextlib import asynccontextmanager

import consumer
from database import trips
from fastapi import FastAPI
from router import root_router

logger = logging.getLogger("uvicorn.error")
logger.name = "Main"


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(consumer.consume())
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(root_router)
