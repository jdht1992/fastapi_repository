import uvicorn
from fastapi import FastAPI
from utils.init_db import create_tables

app = FastAPI()


@app.get("/")
async def welcome():
    return {
        "message": "welcome"
    }

@app.on_event("startup")
def on_startup() -> None:
    """
    Initializes the database tables when the application starts up.
    """
    create_tables()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
