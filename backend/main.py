import logging
import uvicorn
from fastapi import FastAPI


logging.basicConfig(level=logging.INFO)
app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
