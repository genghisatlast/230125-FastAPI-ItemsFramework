from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# In-memory "database" for items
items = {}

# Pydantic model for item
class Item(BaseModel):
    item_id: int
    item_name: str
    item_price: float

# Endpoint to create an item
@app.post("/items/")
def create_item(item: Item):
    if item.item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.item_id] = item
    return {"message": "Item created successfully", "item": item}

# Endpoint to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"message": "Item updated successfully", "item": item}

# Endpoint to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted successfully"}

# Endpoint to get an item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# Run the server (use uvicorn to start this in PRACTICE)
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=7777)
