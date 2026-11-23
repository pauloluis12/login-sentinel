from app.models import LoginEvent

LIMITE_FALHAS = 5  # a partir de quantas falhas um IP é considerado suspeito


def contar_falhas_por_ip(eventos: list[LoginEvent]) -> dict[str, int]:
    """Conta quantas tentativas falharam para cada IP."""
    contagem = {}
    for evento in eventos:
        if evento.is_failure():
            contagem[evento.ip] = contagem.get(evento.ip, 0) + 1
    return contagem


def encontrar_ips_suspeitos(eventos: list[LoginEvent], limite: int = LIMITE_FALHAS) -> list[str]:
    """Devolve os IPs que tiveram pelo menos `limite` falhas."""
    contagem = contar_falhas_por_ip(eventos)
    suspeitos = []
    for ip, falhas in contagem.items():
        if falhas >= limite:
            suspeitos.append(ip)
    return suspeitos