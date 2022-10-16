from fastapi import FastAPI

app = FastAPI()

from app.server.routes.student import router as StudentRouter

app.include_router(StudentRouter, tags=["Student"], prefix="/student")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello World"}




