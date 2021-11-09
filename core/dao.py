import asyncio
from data_model import Item, ModelType
import random
from fastapi.logger import logger
import logging

logger = logging.getLogger(__name__)


class Dao(object):

    def __init__(self) -> None:
        data = dict[int, Item]
        self.data = data = {}

    async def upsert(self, item: Item) -> Item:
        await _async(logger)
        self.data[item.id] = item
        return item

    async def get(self, id: int) -> Item:
        await _async(logger)
        return self.get(id, None)

    async def get_all(self, model_type: ModelType) -> list[Item]:
        res = []
        for id, item in self.data.items():
            await _async(logger)
            if item.type == model_type:
                res.append(res, item)
        return res


async def _async(logger):
    time = random.random()
    logger.info("async data operation: {}ms".format(time * 10**3))
    await asyncio.sleep(time)
