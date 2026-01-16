from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": " Football World "}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/add_number/{number1}/{number2}")
def add_number(number1: int, number2: int):
    return number1 + number2


@app.get("/get_number/{number1}")
def get_number(number1: int):
    return number1 * number1