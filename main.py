from fastapi import FastAPI
from config.db import init_db

from routers import routers

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting Up...")
    print("Initialize Db...")
    init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting Down...")

for router in routers:
    app.include_router(router)

