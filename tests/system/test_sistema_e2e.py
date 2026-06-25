import os
import httpx

# En docker-compose.test.yml configuramos el puerto 8001
API_URL = os.getenv("API_URL", "http://localhost:8001")

def test_flujo_reserva_e2e():
    evento_id = "sistema-evento-xyz"
    
    # 1. Petición POST real para agregar reserva
    payload = {
        "cliente_email": "cliente-e2e@correo.com",
        "zona": "General",
        "cantidad": 3
    }
    resp_post = httpx.post(f"{API_URL}/reservas/{evento_id}", json=payload)
    assert resp_post.status_code == 201, f"Fallo POST: {resp_post.text}"
    
    # 2. Petición GET real al resumen del evento
    resp_get = httpx.get(f"{API_URL}/reservas/{evento_id}/resumen")
    assert resp_get.status_code == 200, f"Fallo GET: {resp_get.text}"
    
    # 3. Validar el total recaudado
    # Regla: General = 50.000 * 3 = 150.000
    datos = resp_get.json()
    assert datos["total_recaudado"] == 150000.0
