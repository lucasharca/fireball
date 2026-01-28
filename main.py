from fastapi import FastAPI
from api.routes import dice

app = FastAPI(title="Fireball")

app.include_router(dice.router, prefix="/dice", tags=["Dice"])