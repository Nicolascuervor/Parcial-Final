import uvicorn
from src.database.config import Base, engine
from src.reservas.api import app

if __name__ == "__main__":
    # Crear las tablas en la base de datos al iniciar
    Base.metadata.create_all(bind=engine)
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
