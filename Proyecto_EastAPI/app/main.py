from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def root():
    return{"Mensaje": "Bienvenido desde la API"}
