import uvicorn
from fastapi import FastAPI
from src.config import settings

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello"}


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
