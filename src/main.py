import fastapi
from src.shob_parallel_workflow import pwf

app = fastapi.FastAPI()

@app.get("/{orderId}")
async def index(orderId: int):
    return {
        "info": pwf(orderId),
    }