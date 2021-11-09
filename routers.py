from fastapi import FastAPI, Depends, APIRouter, HTTPException
from fastapi.logger import logger
from data_model import Item, ModelType
from dao import Dao

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)
dao = Dao()


@router.get("/{item_id}")
async def read_item(item_id: int, limit: int):
    if item_id in dao.data:
        return await dao.get(item_id)

    raise HTTPException(201, detail="Entity not found")


@router.get("/all_items/{model_type}")
async def get_all_items(model_type: ModelType, limit: int):
    if model_type in (ModelType.supply, ModelType.demand):
        items = await dao.get_all(model_type)
        return {
            "model_type": model_type,
            "items": items,
        }

    return {
        "model_type": ModelType.invalid, 
        "items": [],
    }


@router.post("/")
async def create_items(item: Item):
    return await dao.upsert(item)


@router.put(
    "/{item_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_items(item_id: int):
    # No-op for now
    return await dao.upsert(item_id)
