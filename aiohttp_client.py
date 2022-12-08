import json

import aiohttp
import asyncio
from dotenv import load_dotenv
import os
import argparse

load_dotenv()

PROTOCOL = os.getenv("PROTOCOL")
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
HOOK = os.getenv("APIHOOK")

parser = argparse.ArgumentParser()
parser.add_argument('-ids', '--articles_ids')
namespace = parser.parse_args()

async def get_records(article_ids):
  async with aiohttp.ClientSession() as session:
    f = bytes(str(article_ids), encoding='utf-8')
    session.headers.add("Content-type", "application/json")
    async with session.post(f'{PROTOCOL}://{SERVER}:{PORT}/{HOOK}/', data=f) as resp:
      print(f"Response status: {resp.status}")
      print('---------------------------------------')
      print(await resp.text())

if __name__ == '__main__':
  if namespace.articles_ids:
    try:
      ids = json.loads(namespace.articles_ids)
      asyncio.run(get_records(ids))
    except:
      print('Argument -ids must be list. Example: [12,123,1234]')
  else:
    print('Missing argument ids')

