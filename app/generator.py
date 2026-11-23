import random
from datetime import datetime, timedelta

from app.models import LoginEvent

USUARIOS = ["ana", "bruno", "carla", "diego"]
IPS_NORMAIS = ["192.168.0.10", "192.168.0.11", "192.168.0.12"]
IP_ATACANTE = "203.0.113.66"

def gerar_eventos(quantidade_normal: int = 50, tentativas_ataque: int = 30) -> list[LoginEvent]:
    """Cria tentativas de login falsas: acessos normais e um ataque de força bruta."""
    agora = datetime.now()
    eventos = []

    for _ in range(quantidade_normal):
        eventos.append(LoginEvent(
            username=random.choice(USUARIOS),
            ip=random.choice(IPS_NORMAIS),
            success=random.random() < 0.9,
            timestamp=agora - timedelta(minutes=random.randint(0, 60)),
        ))

    for i in range(tentativas_ataque):
        eventos.append(LoginEvent(
            username="admin",
            ip=IP_ATACANTE,
            success=False,
            timestamp=agora - timedelta(seconds=i * 10),
        ))

    return eventos


