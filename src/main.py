from fastapi import FastAPI

from src.routes import router

app = FastAPI(title="test_task")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
