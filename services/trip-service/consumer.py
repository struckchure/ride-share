import json
import logging

import aio_pika
from database import Database

queue_name = "cats_queue"

logger = logging.getLogger("uvicorn.error")
logger.name = "RabbitMQ"


async def consume():
    global connection, channel
    try:
        logger.info(f"Consuming `{queue_name}`")
        connection = await aio_pika.connect_robust(
            "amqp://default_user:default_pass@localhost:5672/default_vhost",
        )
        channel = await connection.channel()

        queue = await channel.declare_queue(queue_name, durable=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    data = json.loads(json.loads(message.body.decode())["data"])
                    logger.info(f"Received {data}", dict.keys(data))

                    Database.update({"id": int(data["trip"]), "status": "InProgress"})

    except Exception as e:
        logger.error(f"RabbitMQ consumer error: {e}")
    finally:
        if connection.is_closed:
            return
        await connection.close()
