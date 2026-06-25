from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.database.models import ReservaDB

def test_crear_reserva_api_y_db(client_con_bd: TestClient, db_session: Session):
    # 1. Preparar el payload JSON
    payload = {
        "cliente_email": "test@correo.com",
        "zona": "VIP",
        "cantidad": 2
    }
    
    # 2. Hacer la petición POST
    response = client_con_bd.post("/reservas/concierto-2026", json=payload)
    
    # Aserción 1: Que el código HTTP sea 201
    assert response.status_code == 201
    
    # Aserción 2: Consulta SQLAlchemy a la base de datos
    # Verificamos que el registro efectivamente exista y coincida el email
    reserva_en_db = db_session.query(ReservaDB).filter_by(cliente_email="test@correo.com").first()
    
    assert reserva_en_db is not None
    assert reserva_en_db.cliente_email == "test@correo.com"
    assert reserva_en_db.zona == "VIP"
    assert reserva_en_db.cantidad == 2
    assert reserva_en_db.evento_id == "concierto-2026"
