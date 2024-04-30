import uvicorn
from fastapi import FastAPI
from utils.init_db import create_tables
from router.api import router_region

app = FastAPI()

app.include_router(router_region)


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
