import glob
import os
import uvicorn
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


DATA_DIR = "data"
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_path():
    paths = glob.glob(os.path.join(DATA_DIR, '*.json'))
    return os.path.join(DATA_DIR, f"{len(paths) + 1}.json")


@app.post('/save')
async def saver(data: Request):
    data = await data.json()
    path = get_path()
    with open(path, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999)
