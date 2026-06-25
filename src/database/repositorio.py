from sqlalchemy.orm import Session
from src.database.models import ReservaDB

class ReservasRepositorio:
    PRECIOS = {
        "VIP": 150000.0,
        "General": 50000.0
    }

    def __init__(self, db: Session):
        self.db = db

    def guardar_reserva(self, evento_id: str, cliente_email: str, zona: str, cantidad: int) -> ReservaDB:
        reserva = ReservaDB(
            evento_id=evento_id,
            cliente_email=cliente_email,
            zona=zona,
            cantidad=cantidad
        )
        self.db.add(reserva)
        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    def calcular_total_evento(self, evento_id: str) -> float:
        reservas = self.db.query(ReservaDB).filter(ReservaDB.evento_id == evento_id).all()
        total = 0.0
        for r in reservas:
            precio = self.PRECIOS.get(r.zona, 0.0)
            total += precio * r.cantidad
        return total
