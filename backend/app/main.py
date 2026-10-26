from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def message():
    return {"message": "Bienvenido a MediTurno"}


@app.get("/health")
def status():
    return {"status": "Activo"}