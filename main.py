from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel
import pysondb
import os
from dotenv import load_dotenv

load_dotenv()

db = pysondb.db.getDb(os.getenv("PYSONDB"))

class Item(BaseModel):
  name: str
  description: Union[str, None] = None
  price: float
  tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/")
async def retrieve_items(items: List):
  print(items)
  records = []
  all = db.getAll()
  for item in items:
    if not type(item) is int:
      return {
        "status": "ERROR",
        "message": "Indexes must be integer"
      }
  for item in items:
    [records.append(i) for i in all if i["article_id"] == item]
  return records if len(records) > 0 else {
    "status": "ERROR",
    "message": "No items found"
  }
