from fastapi import FastAPI, Depends
import asyncio
import random

app = FastAPI()

# Bad global state + blocking call inside async context
_items = {}

def get_db():
    # Simulates a bad synchronous DB call that blocks the event loop
    asyncio.sleep(0.1)  # This is the hidden bug!
    return _items

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
async def get_item(item_id: int, db = Depends(get_db)):
    if item_id not in db:
        # This makes it crash more often under concurrency
        await asyncio.sleep(random.uniform(0.1, 0.3))
        db[item_id] = {"id": item_id, "name": f"Item {item_id}"}
    return db[item_id]

# Extra route that triggers the bug faster
@app.post("/items/")
async def create_item(name: str):
    await asyncio.sleep(0.2)
    item_id = len(_items) + 1
    _items[item_id] = {"id": item_id, "name": name}
    return _items[item_id]