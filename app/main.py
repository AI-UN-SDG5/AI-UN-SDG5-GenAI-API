from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the P for Pluma Generative AI API!"}