from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Planet(BaseModel):
    id: int
    name: str


@app.post("/planets/", response_model=Planet)
async def create_planet(planet: Planet):
    return planet
