from fastapi import FastAPI

app = FastAPI(
    title="Knowledge API",
    version="0.1.0"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

