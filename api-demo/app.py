from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


def dummy_function(surface: float, number_of_rooms: Optional[int], address: str) -> int:
    return 20 * number_of_rooms + surface if number_of_rooms is not None else int(surface)


class PropertyInfo(BaseModel):
    address: str
    surface: float
    number_of_rooms: Optional[int] = None


@app.get("/dummy")
def read_dummy():
    return {"result": dummy_function(0, None, "")}


@app.post("/property")
def process_property(info: PropertyInfo):
    result = dummy_function(
        surface=info.surface,
        number_of_rooms=info.number_of_rooms,
        address=info.address,
    )
    return {
        "address": info.address,
        "surface": info.surface,
        "number_of_rooms": info.number_of_rooms,
        "dummy_result": result,
    }
