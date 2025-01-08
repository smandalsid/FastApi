from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def get_health_check():
    return {"Message": "Application looks healthy"}